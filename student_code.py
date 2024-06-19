# Homework Assignment: Inventory Optimization Challenge

# ----------------------------------------------------
# region Assignment Details
# ----------------------------------------------------
# As an inventory manager, you are tasked with optimizing warehouse inventory based on historical sales data.
# Analyze the provided sales data for various products to determine their restocking needs. A product needs
# restocking if its average monthly sales over the last three months exceed its current inventory level.
# Based on your analysis, update the 'restocking_needed' dictionary by setting the value to 1 for products that require
# restocking and 0 for products that do not.
# ----------------------------------------------------

# Provided sales data for analysis - DO NOT ALTER THIS DICTIONARY STRUCTURE
sales_data = {
    'Prod1': ([20, 30, 25], 20),
    'Prod2': ([50, 60, 55], 150),
    'Prod3': ([15, 20, 15], 40),
    'Prod4': ([10, 12, 15], 30)
}

# Initialize the 'restocking_needed' dictionary. Update this based on your analysis.
restocking_needed = {
    'Prod1': 0,  # Update 0 to 1 if restocking is needed, keep as 0 otherwise
    'Prod2': 0,
    'Prod3': 0,
    'Prod4': 0
}

# Your code to analyze 'sales_data' and update 'restocking_needed' goes here.
