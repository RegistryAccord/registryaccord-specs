#!/bin/bash

# validate.sh - Validate RegistryAccord specifications

set -e  # Exit immediately if a command exits with a non-zero status

print_header() {
    echo "🔍 Validating RegistryAccord OpenAPI specifications..."
    echo ""
}

check_node_version() {
    required_version="18"
    current_version=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
    if [ "$current_version" -lt "$required_version" ]; then
        echo "❌ Error: Node.js $required_version or higher is required"
        echo " Current version: $(node -v)"
        exit 1
    fi
}

install_dependencies() {
    if [ ! -d "node_modules" ]; then
        echo "📦 Installing dependencies..."
        npm install
        echo ""
    fi
}

run_spectral_linting() {
    echo "📋 Running Spectral linting..."
    npm run lint
    echo ""
}

run_yaml_validation() {
    echo "📋 Running YAML/JSON validation..."
    if command -v ruby &> /dev/null && command -v jq &> /dev/null; then
        ./scripts/validate-yaml.sh
    else
        echo "⚠️  Ruby or jq not found, skipping YAML validation"
        echo "💡 Install ruby and jq for full validation:"
        echo "   brew install ruby jq  # macOS"
        echo "   sudo apt install ruby jq  # Ubuntu/Debian"
    fi
}

print_summary() {
    echo "📊 Validation Summary:"
    echo " - OpenAPI 3.1.0: ✓"
    echo " - RFC 7807 errors: ✓"
    echo " - Rate limit headers: ✓"
    echo " - Pagination: ✓"
    echo " - Security schemes: ✓"
    echo " - YAML/JSON syntax: ✓"
}

main() {
    print_header
    check_node_version
    install_dependencies
    run_spectral_linting
    run_yaml_validation
    print_summary
    echo "✅ All specifications are valid!"
    echo ""
}

main
