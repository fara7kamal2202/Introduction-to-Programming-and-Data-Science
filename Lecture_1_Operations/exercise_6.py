# ================================
# Exercise: Compound Interest Calculator
# ================================

# Task: Calculate compound interest
# Formula: A = P * (1 + r/n)^(n*t)
# Where:
#   A = final amount
#   P = principal (initial investment)
#   r = annual interest rate (as decimal)
#   n = number of times interest is compounded per year
#   t = number of years

principal = 1000  # Initial investment in dollars
annual_rate = 0.05  # 5% annual interest rate
compounds_per_year = 12  # Monthly compounding
years = 3

# Calculate the final amount
final_amount = principal * (1 + annual_rate / compounds_per_year) ** (compounds_per_year * years)

# Calculate the interest earned
interest_earned = final_amount - principal

# Calculate the effective annual rate
# Formula: EAR = (1 + r/n)^n - 1
effective_annual_rate = (1 + annual_rate / compounds_per_year) ** compounds_per_year - 1

print(f"Initial investment: ${principal:.2f}")
print(f"Final amount after {years} years: ${final_amount:.2f}")
print(f"Interest earned: ${interest_earned:.2f}")
print(f"Effective annual rate: {effective_annual_rate:.2%}")
