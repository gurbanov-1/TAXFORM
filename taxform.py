# Tax Form Calculator

# Constants for tax calculation
STANDARD_DEDUCTION = 10000  # Standard deduction amount for 2022
DEPENDENT_DEDUCTION = 3000  # Deduction amount per dependent
TAX_RATE = 0.20  # 20% tax rate

# Step 1: Collect inputs
gross_income = float(input("Enter your gross income: $"))
num_dependents = int(input("Enter the number of dependents: "))

# Step 2: Compute income tax
dependent_deductions = DEPENDENT_DEDUCTION * num_dependents
net_income = gross_income - STANDARD_DEDUCTION - dependent_deductions

# Ensure net income isn't negative
net_income = max(0, net_income)
income_tax = net_income * TAX_RATE

# Step 3: Print results
print("\n=== Tax Calculation Summary ===")
print(f"Gross Income: ${gross_income:,.2f}")
print(f"Standard Deduction: ${STANDARD_DEDUCTION:,.2f}")
print(f"Dependent Deductions: ${dependent_deductions:,.2f}")
print(f"Net Taxable Income: ${net_income:,.2f}")
print(f"Income Tax (20%): ${income_tax:,.2f}")

