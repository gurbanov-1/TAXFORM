# Constants for tax calculation
STANDARD_DEDUCTION = 10000.0  # Standard deduction amount
DEPENDENT_DEDUCTION = 3000.0  # Deduction amount per dependent
TAX_RATE = 0.20  # 20% tax rate

def calculate_tax(gross_income, num_dependents):
    """Calculates income tax based on gross income and number of dependents."""
    dependent_deductions = DEPENDENT_DEDUCTION * num_dependents
    net_income = gross_income - STANDARD_DEDUCTION - dependent_deductions
    net_income = max(0, net_income)
    income_tax = net_income * TAX_RATE
    return gross_income, STANDARD_DEDUCTION, dependent_deductions, net_income, income_tax

def main():
    # Step 1: Collect inputs (with validation)
    while True:
        try:
            gross_income = float(input("Enter your gross income: $"))
            if gross_income < 0:
                print("Gross income cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number for gross income.")

    while True:
        try:
            num_dependents = int(input("Enter the number of dependents: "))
            if num_dependents < 0:
                print("Number of dependents cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for dependents.")

    # Step 2: Calculate tax
    gross_income, standard_deduction, dependent_deductions, net_income, income_tax = calculate_tax(gross_income, num_dependents)

    # Step 3: Print results
    print("\n=== Tax Calculation Summary ===")
    print(f"Gross Income: ${gross_income:,.2f}")
    print(f"Standard Deduction: ${standard_deduction:,.2f}")
    print(f"Dependent Deductions: ${dependent_deductions:,.2f}")
    print(f"Net Taxable Income: ${net_income:,.2f}")
    print(f"Income Tax (20%): ${income_tax:,.2f}")

if __name__ == "__main__":
    main()
