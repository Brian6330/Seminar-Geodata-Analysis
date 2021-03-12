from math import ceil
# UserAge.py asks for a user's name and age.
# Then it calculates the next decade and the number of years left to reach it.

# Ask user for name
name = input('Please enter your name: ')
print("Welcome", name)

# Ask user for age and cast age to int
age = input('Please enter your age: ')
age = int(age)

#If age below 10, use 10. Otherwise divide by 10
next_tenth = ceil(age / 10)*10
year_gap = next_tenth - age


print(name + " in " + str(year_gap) + " years you'll be " + str(next_tenth) + ".")