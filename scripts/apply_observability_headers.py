#!/usr/bin/env python3
"""Ensure every OpenAPI endpoint documents observability headers."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, List

from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[1]
OPENAPI_DIR = ROOT / "openapi"
HTTP_METHODS = {"get", "post", "put", "patch", "delete"}

yaml = YAML(typ="rt")
yaml.preserve_quotes = True
yaml.width = 4096

PARAM_DEFINITIONS: Dict[str, Dict[str, Any]] = {
    "CorrelationId": {
        "name": "X-Correlation-ID",
        "in": "header",
        "required": True,
        "description": "Unique request correlation ID (UUID v4) propagated across services",
        "schema": {
            "type": "string",
            "format": "uuid",
            "example": "550e8400-e29b-41d4-a716-446655440000",
        },
    },
    "TraceParent": {
        "name": "traceparent",
        "in": "header",
        "required": True,
        "description": "W3C Trace Context header for distributed tracing",
        "schema": {
            "type": "string",
            "pattern": "^[0-9a-f]{2}-[0-9a-f]{32}-[0-9a-f]{16}-[0-9a-f]{2}$",
            "example": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
        },
    },
    "TraceState": {
        "name": "tracestate",
        "in": "header",
        "required": False,
        "description": "Optional W3C Trace Context tracestate header for vendor-specific context",
        "schema": {
            "type": "string",
            "maxLength": 512,
            "example": "rojo=00f067aa0ba902b7,congo=t61rcWkgMzE",
        },
    },
}

PARAM_REFS = [f"#/components/parameters/{name}" for name in PARAM_DEFINITIONS.keys()]


def ensure_parameters_list(operation: Dict[str, Any]) -> List[Dict[str, Any]]:
    params = operation.get("parameters")
    if params is None:
        params = []
    if not isinstance(params, list):
        params = [params]
    operation["parameters"] = params
    return params


def has_ref(params: List[Dict[str, Any]], ref: str) -> bool:
    for param in params:
        if isinstance(param, dict) and param.get("$ref") == ref:
            return True
    return False


def main() -> None:
    spec_paths = sorted(OPENAPI_DIR.glob("*/v1/openapi.yaml"))
    if not spec_paths:
        raise SystemExit("No OpenAPI specs found")

    for spec_path in spec_paths:
        doc = yaml.load(spec_path.read_text())
        modified = False
        components = doc.setdefault("components", {})
        component_params = components.setdefault("parameters", {})

        for name, definition in PARAM_DEFINITIONS.items():
            if name not in component_params:
                component_params[name] = deepcopy(definition)
                modified = True

        paths = doc.get("paths", {})
        for path_item in paths.values():
            if not isinstance(path_item, dict):
                continue
            for method, operation in path_item.items():
                if method.lower() not in HTTP_METHODS:
                    continue
                if not isinstance(operation, dict):
                    continue
                params_list = ensure_parameters_list(operation)
                for ref in PARAM_REFS:
                    if not has_ref(params_list, ref):
                        params_list.insert(0, {"$ref": ref})
                        modified = True

        if modified:
            with spec_path.open("w") as fh:
                yaml.dump(doc, fh)
            print(f"Updated observability headers in {spec_path.relative_to(ROOT)}")
        else:
            print(f"No changes needed for {spec_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
