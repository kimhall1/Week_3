# DSC 510
# Week 3
# Programming Assignment Week 3
# Author Kimberly Hall
# 9/12/2022

# This program is designed to calculate cost of fiber optic cable to be installed

print('Welcome to the price calculator!')

# User will be asked to provide their company name.
company_name = input('Please provide your company name.')

# User will input amount of fiber optic cable needed to be installed, making float for rounding purposes
feet_needed = input('How many feet of cable will you need installed?')
feet_needed = float(feet_needed)
#normal cost per foot
normal_cost = 0.87

if feet_needed > 500:
    install_cost = 0.50
elif feet_needed > 250:
    install_cost = 0.70
elif feet_needed > 100:
    install_cost = 0.80
else:
    install_cost = normal_cost
#Change 1
#Change made: added if else statements to code
#Date of Change: 9/13/2022
#Author: Kimberly Hall
#Change Approved by: Kimberly Hall
#Date moved to production: 9/13/2022

# Total installation cost is calculated
total_cost = input(feet_needed * install_cost)

# Program prints receipt
print("Below is your receipt")
print("Company Name:"), input(company_name)
print("Feet of fiber to be installed"), input(feet_needed)
print("Cost per foot"), input(install_cost)
print('Total cost in dollars'), input(feet_needed * install_cost)
