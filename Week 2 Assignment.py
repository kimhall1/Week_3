# DSC 510
# Week 2
# Programming Assignment Week 2
# Author Kimberly Hall
# 9/9/2022

# This program is designed to calculate cost of fiber optic cable to be installed

print('Welcome to the price calculator!')

# User will be asked to provide their company name.
company_name = input('Please provide your company name.')

# User will input amount of fiber optic cable needed to be installed, making float for rounding purposes
feet_needed = input('How many feet of cable will you need installed?')
feet_needed = float(feet_needed)
install_cost = 0.87

# Total installation cost is calculated
total_cost = input(feet_needed * install_cost)

# Program prints receipt
print("Below is your receipt")
print("Company Name:"), input(company_name)
print("Feet of fiber to be installed"), input(feet_needed)
print("Cost per foot"), input(install_cost)
print('Total cost in dollars'), input(feet_needed * install_cost)
