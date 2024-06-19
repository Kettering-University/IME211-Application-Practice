import sys

# Attempt to import the student's script
try:
    import student_code as sc
except ImportError:
    print("Failed to import the student's script.")
    sys.exit(1)

# Expected 'restocking_needed' values based on the provided 'sales_data'
expected_restocking_needed = {
    'Prod1': 1,
    'Prod2': 0,
    'Prod3': 0,
    'Prod4': 0
}

# Compare student's 'restocking_needed' dictionary to the expected values
try:
    for product, need_restock in expected_restocking_needed.items():
        if sc.restocking_needed[product] != need_restock:
            print(f"Mismatch found for {product}. Expected {need_restock}, got {sc.restocking_needed[product]}")
            sys.exit(1)  # Fail if any value doesn't match
    # Pass if all values match
    sys.exit(0)
except Exception as e:
    print(f"Error during comparison: {e}")
    sys.exit(1)  # Fail due to error
