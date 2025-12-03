#!/usr/bin/env python3
"""Verify every OpenAPI endpoint has a tracked example file and metadata entry."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[1]
OPENAPI_DIR = ROOT / "openapi"
EXAMPLES_MAP = ROOT / "examples" / "examples-map.json"

HTTP_METHODS = {"get", "post", "put", "patch", "delete"}

yaml = YAML(typ="rt")

def load_endpoints() -> Set[Tuple[str, str, str]]:
    endpoints: Set[Tuple[str, str, str]] = set()
    for spec_path in sorted(OPENAPI_DIR.glob('*/v1/openapi.yaml')):
        service = spec_path.parts[-3]
        doc = yaml.load(spec_path.read_text())
        for path, path_item in doc.get('paths', {}).items():
            if not isinstance(path_item, dict):
                continue
            for method, operation in path_item.items():
                if method.lower() not in HTTP_METHODS:
                    continue
                if not isinstance(operation, dict):
                    continue
                endpoints.add((service, path, method.upper()))
    return endpoints

def load_metadata() -> List[Dict[str, Any]]:
    try:
        data = json.loads(EXAMPLES_MAP.read_text())
    except FileNotFoundError:
        raise SystemExit(f"Missing metadata file: {EXAMPLES_MAP}")
    if not isinstance(data, list):
        raise SystemExit("examples-map.json must contain a list")
    return data


def main() -> None:
    endpoints = load_endpoints()
    metadata = load_metadata()

    meta_map: Dict[Tuple[str, str, str], str] = {}
    errors: List[str] = []

    for entry in metadata:
        try:
            service = entry['service']
            path = entry['path']
            method = entry['method'].upper()
            example_rel = entry['example']
        except KeyError as exc:
            errors.append(f"Metadata entry missing field {exc}: {entry}")
            continue
        key = (service, path, method)
        if key in meta_map:
            errors.append(f"Duplicate metadata entry for {service} {method} {path}")
        meta_map[key] = example_rel
        example_path = ROOT / example_rel
        if not example_path.exists():
            errors.append(f"Example file missing: {example_rel}")
        elif example_path.suffix not in {'.yaml', '.yml', '.json'}:
            errors.append(f"Unsupported example extension for {example_rel}")

    missing = sorted(endpoints - meta_map.keys())
    extra = sorted(set(meta_map.keys()) - endpoints)

    for service, path, method in missing:
        errors.append(f"Missing example metadata for {service} {method} {path}")
    for service, path, method in extra:
        errors.append(f"examples-map.json contains stale entry for {service} {method} {path}")

    if errors:
        print("Example metadata validation failed:\n", file=sys.stderr)
        for msg in errors:
            print(f" - {msg}", file=sys.stderr)
        sys.exit(1)

    print(f"Validated {len(endpoints)} endpoints with {len(metadata)} mapped examples.")


if __name__ == "__main__":
    main()
