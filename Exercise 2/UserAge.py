from math import ceil
# UserAge.py asks for a user's name and age.
# Then it calculates the next decade and the number of years left to reach it.

# Ask user for name
name = input('Please enter your name: ')
print("Welcome", name)

# Ask user for age and cast age to int
age = int(input('Please enter your age: '))

# If age below 10, use 10. Otherwise divide by 10
next_tenth = 10 * (age // 10) + 10
year_gap = next_tenth - age

print("{}, in {} year(s) you'll be {}. Rocket science !".format (name , year_gap, next_tenth))
