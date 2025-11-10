#!/bin/bash

# Validate YAML files in the repository

validate_yaml() {
  local file=$1
  echo "Validating $file..."
  if ruby -e "require 'yaml'; YAML.load_file('$file')" 2>/dev/null; then
    echo "✅ $file is valid YAML"
  else
    echo "❌ $file has YAML syntax errors"
    ruby -e "require 'yaml'; YAML.load_file('$file')" 2>&1
    return 1
  fi
}

# Validate all example YAML files
ERRORS=0
for file in examples/*/*.yaml examples/*/*/*.yaml; do
  if [ -f "$file" ]; then
    if ! validate_yaml "$file"; then
      ERRORS=$((ERRORS + 1))
    fi
  fi
done

# Validate policy YAML files
for file in policies/*.json; do
  echo "Validating $file..."
  if jq empty "$file" 2>/dev/null; then
    echo "✅ $file is valid JSON"
  else
    echo "❌ $file has JSON syntax errors"
    jq empty "$file" 2>&1
    ERRORS=$((ERRORS + 1))
  fi
done

if [ $ERRORS -eq 0 ]; then
  echo "\n✅ All YAML/JSON files are valid!"
  exit 0
else
  echo "\n❌ Found $ERRORS file(s) with syntax errors"
  exit 1
fi
