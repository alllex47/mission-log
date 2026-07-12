# Day 2: 30 Days of python programming

# Exercises: Level 1
'''
1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py - filename is day02.py
2. Write a python comment saying 'Day 2: 30 Days of python programming
3. Declare a first name variable and assign a value to it
4. Declare a last name variable and assign a value to it
5. Declare a full name variable and assign a value to it
6. Declare a country variable and assign a value to it
7. Declare a city variable and assign a value to it
8. Declare an age variable and assign a value to it
9. Declare a year variable and assign a value to it
10. Declare a variable is_married and assign a value to it
11. Declare a variable is_true and assign a value to it
12. Declare a variable is_light_on and assign a value to it
13. Declare multiple variable on one line
'''

first_name = 'Alex'
last_name = 'Test'
full_name = first_name + ' ' + last_name
country = 'Romania'
city = 'Bucharest'
age = 300
year = 2026
is_married = False
is_true = True
is_light_on = False
home_town, planet = 'Oltenita', 'Earth'

# Exercises: Level 2

# 1. Check the data type of all your variables using type() built-in function

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(home_town), type(planet))

# 2. Using the len() built-in function, find the length of your first name
print(len(first_name))

# 3. Compare the length of your first name and your last name
print(len(first_name) == len(last_name))

# 4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# 5. Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
# 6. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
# 7. Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
# 8. Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
# 9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
# 10. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
# 11. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

print('Num one:', num_one)
print('Num two:', num_two)
print('Num total:', total)
print('Num diff:', diff)
print('Num product:', product)
print('Num division:', division)
print('Num remainder:', remainder)
print('Num exponential:', exp)
print('Num floor division:', floor_division)

'''
12. The radius of a circle is 30 meters.
    Calculate the area of a circle and assign the value to a variable name of area_of_circle
    Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
    Take radius as user input and calculate the area.
'''
area_of_circle = 3.14 * 30 ** 2
circum_of_circle = 2 * 3.14 * 30
print('Area of Circle:', area_of_circle)
print('Circumference of Circle:', circum_of_circle)
radius = float(input('What is the radius of the circle?: '))
circle_area = 3.14 * radius ** 2
print('Radius:', radius)
print('Area:', circle_area)

# 13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

first_name = input('What is your first name?:')
last_name = input('What is your last name?:')
country = input('What is your country?:')
age = int(input('What is your age?:'))

print('First Name:', first_name)
print('Last Name:', last_name)
print('Country:', country)
print('Age:', age)

# 14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')
