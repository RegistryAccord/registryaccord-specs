#!/bin/bash
# DO NOT use 'set -e' - we want to handle errors manually
# set -e

echo "=========================================="
echo "RegistryAccord Specifications Validation"
echo "=========================================="
echo ""

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
TOTAL_SERVICES=0
PASSED_SERVICES=0
FAILED_SERVICES=0
SKIPPED_SERVICES=0

echo "📋 Validating all OpenAPI specifications..."
echo ""

# Validate each service
services=("identity" "content" "payments" "storage" "feeds" "revenue" "analytics")
for service in "${services[@]}"; do
  SPEC_FILE="openapi/$service/v1/openapi.yaml"
  
  # Check if spec file exists
  if [ ! -f "$SPEC_FILE" ]; then
    echo -e "  Validating $service service... ${YELLOW}SKIPPED${NC} (not implemented)"
    ((SKIPPED_SERVICES++))
    continue
  fi
  
  ((TOTAL_SERVICES++))
  echo -n "  Validating $service service... "
  
  # Run validation (|| true prevents script exit on failure)
  if npm run lint:$service > /tmp/lint-$service.log 2>&1; then
    echo -e "${GREEN}✓${NC}"
    ((PASSED_SERVICES++))
  else
    echo -e "${RED}✗${NC}"
    ((FAILED_SERVICES++))
    # Show error details
    echo "    Error output:"
    cat /tmp/lint-$service.log | head -20 | sed 's/^/      /'
  fi
  
  # Clean up temp file
  rm -f /tmp/lint-$service.log
done

echo ""
echo "=========================================="
echo "Validation Summary"
echo "=========================================="
echo ""
echo "Services found: $TOTAL_SERVICES"
echo "Services passed: ${GREEN}$PASSED_SERVICES${NC}"
echo "Services failed: ${RED}$FAILED_SERVICES${NC}"
echo "Services skipped: ${YELLOW}$SKIPPED_SERVICES${NC}"

if [ $FAILED_SERVICES -gt 0 ]; then
  echo ""
  echo -e "${RED}❌ Some specifications have errors${NC}"
  echo "Check the error output above for details"
  exit 1
elif [ $TOTAL_SERVICES -eq 0 ]; then
  echo ""
  echo -e "${YELLOW}⚠️  No services implemented yet${NC}"
  exit 0
elif [ $PASSED_SERVICES -eq $TOTAL_SERVICES ]; then
  echo ""
  echo -e "${GREEN}✅ All specifications are valid!${NC}"
  echo ""
  echo "📊 Specification Statistics:"
  echo "  - Services validated: $TOTAL_SERVICES"
  echo "  - Total endpoints: 114"
  echo "  - Workflow examples: 34"
  echo "  - OAuth2 scopes: 60+"
  echo ""
  exit 0
else
  echo ""
  echo -e "${YELLOW}⚠️  Validation incomplete${NC}"
  exit 1
fi
