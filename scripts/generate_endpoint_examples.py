#!/usr/bin/env python3
"""Generate per-endpoint example files and a metadata map from OpenAPI specs."""
from __future__ import annotations

import json
import re
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, List, Optional

from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[1]
OPENAPI_DIR = ROOT / "openapi"
OUTPUT_DIR = ROOT / "examples" / "generated"
METADATA_FILE = ROOT / "examples" / "examples-map.json"

yaml = YAML(typ="rt")
yaml.preserve_quotes = True
yaml.width = 4096

UUID = "123e4567-e89b-12d3-a456-426614174000"
TRACE_ID = "550e8400-e29b-41d4-a716-446655440000"
API_VERSION = "2025-11-01"
CORRELATION_ID = TRACE_ID


def load_specs() -> List[Path]:
    return sorted(OPENAPI_DIR.glob("*/v1/openapi.yaml"))


def slugify(path: str) -> str:
    slug = path.strip("/")
    slug = slug.replace("/", "-")
    slug = slug.replace("{", "").replace("}", "")
    slug = re.sub(r"[^a-zA-Z0-9\-]", "-", slug)
    return slug or "root"


def resolve_ref(doc: Dict[str, Any], ref: str) -> Dict[str, Any]:
    if not ref.startswith("#/" ):
        raise ValueError(f"Unsupported ref: {ref}")
    parts = ref.lstrip("#/").split("/")
    node: Any = doc
    for part in parts:
        node = node[part]
    return node


def sample_value(schema: Dict[str, Any], doc: Dict[str, Any], seen: Optional[set[str]] = None) -> Any:
    if seen is None:
        seen = set()
    if not schema:
        return None
    if "$ref" in schema:
        ref = schema["$ref"]
        if ref in seen:
            return None
        seen.add(ref)
        target = resolve_ref(doc, ref)
        return sample_value(target, doc, seen)
    if "example" in schema:
        return deepcopy(schema["example"])
    if "default" in schema:
        return deepcopy(schema["default"])
    if "enum" in schema and schema["enum"]:
        return schema["enum"][0]
    if "allOf" in schema:
        merged: Dict[str, Any] = {}
        for part in schema["allOf"]:
            val = sample_value(part, doc, seen.copy())
            if isinstance(val, dict):
                merged.update(val)
        return merged or None
    if "oneOf" in schema:
        return sample_value(schema["oneOf"][0], doc, seen.copy())
    if "anyOf" in schema:
        return sample_value(schema["anyOf"][0], doc, seen.copy())

    schema_type = schema.get("type")
    if not schema_type:
        if "properties" in schema:
            schema_type = "object"
        elif "items" in schema:
            schema_type = "array"
    if schema_type == "object":
        props = {}
        for idx, (name, prop_schema) in enumerate(schema.get("properties", {}).items()):
            props[name] = sample_value(prop_schema, doc, seen.copy())
            if idx >= 4:
                break
        required = schema.get("required", [])
        for req in required:
            if req not in props:
                props[req] = None
        return props
    if schema_type == "array":
        sample = sample_value(schema.get("items", {}), doc, seen.copy())
        return [sample]
    if schema_type == "integer":
        minimum = schema.get("minimum", 1)
        maximum = schema.get("maximum", minimum + 100)
        return minimum if minimum is not None else 1
    if schema_type == "number":
        return schema.get("minimum", 0.0)
    if schema_type == "boolean":
        return True
    if schema_type == "string":
        fmt = schema.get("format")
        if fmt == "uuid":
            return UUID
        if fmt == "email":
            return "builder@example.com"
        if fmt == "date-time":
            return "2025-11-06T12:00:00Z"
        if fmt == "uri":
            return "https://api.registryaccord.com/resource/123"
        if fmt == "duration":
            return "PT1H"
        return schema.get("pattern", "string-value")
    return None


def format_parameter_sample(param: Dict[str, Any], doc: Dict[str, Any]) -> Any:
    schema = param.get("schema", {})
    sample = sample_value(schema, doc)
    name = param.get("name")
    if isinstance(sample, str) and name and name.lower() in {"limit", "page_size"}:
        return 25
    if name and name.lower() in {"after", "before", "cursor"}:
        return "opaqueCursor123"
    if name and name.lower() == "id":
        return UUID
    if sample is None:
        if schema.get("type") == "integer":
            return 1
        if schema.get("type") == "boolean":
            return True
        return "example"
    return sample


def build_example_entry(doc: Dict[str, Any], service: str, path: str, method: str, operation: Dict[str, Any]) -> Dict[str, Any]:
    entry: Dict[str, Any] = {
        "service": service,
        "path": path,
        "method": method.upper(),
        "summary": operation.get("summary"),
    }

    all_params: List[Dict[str, Any]] = []
    def add_params(params: Any) -> None:
        if isinstance(params, list):
            for param in params:
                if not isinstance(param, dict):
                    continue
                all_params.append(param)
    path_item_obj = doc["paths"].get(path, {})
    add_params(path_item_obj.get("parameters"))
    add_params(operation.get("parameters"))

    request: Dict[str, Any] = {}
    path_params = {}
    query_params = {}
    header_params = {}
    for param in all_params:
        location = param.get("in")
        name = param.get("name")
        if not name:
            continue
        sample = format_parameter_sample(param, doc)
        if location == "path":
            path_params[str(name)] = sample
        elif location == "query":
            query_params[str(name)] = sample
        elif location == "header":
            header_params[str(name)] = sample
    if path_params:
        request["pathParams"] = path_params
    if query_params:
        request["queryParams"] = query_params
    if header_params:
        request["headers"] = header_params

    if "requestBody" in operation:
        req_body = operation["requestBody"]
        content = req_body.get("content", {})
        json_body = content.get("application/json") or next(iter(content.values()), None)
        if json_body:
            schema = json_body.get("schema", {})
            request["body"] = sample_value(schema, doc)
    if request:
        entry["request"] = request

    responses = operation.get("responses", {})
    preferred_status = None
    for status in sorted(responses.keys()):
        if status.startswith("2"):
            preferred_status = status
            break
    if not preferred_status and responses:
        preferred_status = next(iter(responses.keys()))
    response_block: Dict[str, Any] = {}
    if preferred_status:
        resp_obj = responses[preferred_status]
        if "$ref" in resp_obj:
            resp_obj = resolve_ref(doc, resp_obj["$ref"])
        response_block["status"] = preferred_status
        if isinstance(resp_obj, dict):
            if "description" in resp_obj:
                response_block["description"] = resp_obj["description"]
            headers = resp_obj.get("headers", {})
            if headers:
                response_block["headers"] = {name: sample_value(defn, doc) if isinstance(defn, dict) else None for name, defn in headers.items()}
            content = resp_obj.get("content", {})
            json_content = content.get("application/json") or next(iter(content.values()), None)
            if json_content and "schema" in json_content:
                response_block["body"] = sample_value(json_content["schema"], doc)
    if response_block:
        entry["response"] = response_block

    return entry


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    metadata: List[Dict[str, str]] = []
    for spec_path in load_specs():
        service = spec_path.parts[-3]
        doc = yaml.load(spec_path.read_text())
        paths = doc.get("paths", {})
        service_dir = OUTPUT_DIR / service
        service_dir.mkdir(parents=True, exist_ok=True)
        for path, path_item in paths.items():
            if not isinstance(path_item, dict):
                continue
            for method, operation in path_item.items():
                if method.lower() not in {"get", "post", "put", "patch", "delete"}:
                    continue
                if not isinstance(operation, dict):
                    continue
                example_data = build_example_entry(doc, service, path, method, operation)
                filename = f"{method.lower()}-{slugify(path)}.yaml"
                example_path = service_dir / filename
                with example_path.open("w") as f:
                    yaml.dump(example_data, f)
                metadata.append(
                    {
                        "service": service,
                        "path": path,
                        "method": method.upper(),
                        "example": str(example_path.relative_to(ROOT)),
                    }
                )
    with METADATA_FILE.open("w") as f:
        json.dump(metadata, f, indent=2)
    print(f"Generated {len(metadata)} endpoint examples across {len(load_specs())} specs.")


if __name__ == "__main__":
    main()
