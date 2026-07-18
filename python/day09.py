# Day 9: 30 Days of python programming

# Exercises: Level 1

# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
'''
    Output:
    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.
'''
user_age = int(input('Enter your age: '))
if user_age >= 18:
    print('You are old enough to learn to drive.')
else:
    print(f"You need {18 - user_age} more years to learn to drive.")

# 2. Compare the values of my_age and your_age using if … else.
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
'''
    Enter your age: 30
    You are 5 years older than me.
'''

my_age = 25
your_age = int(input('Enter your age: '))
if my_age > your_age:
    if my_age - your_age == 1:
        print(f"I am {my_age - your_age} year older than you.")
    else:
        print(f"I am {my_age - your_age} years older than you.")
elif my_age == your_age:
    print('We have the same age.')

else:
    if your_age - my_age == 1:
        print(f"You are {your_age - my_age} year older than me.")
    else:
        print(f"You are {your_age - my_age} years older than me.")

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
'''
    Enter number one: 4
    Enter number two: 3
    4 is greater than 3
'''
number_one = int(input('Enter number one: '))
number_two = int(input('Enter number two: '))
if number_one > number_two:
    print(f"{number_one} is greater than {number_two}.")
elif number_two > number_one:
    print(f"{number_two} is greater than {number_one}.")
else:
    print(f"{number_one} is equal to {number_two}.")


# Exercises: Level 2

# 1. Write a code which gives grade to students according to theirs scores:
'''sh
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
'''
student_score = int(input('Enter your score: '))
if student_score < 0 or student_score > 100:
    print('Your score is not valid. Try again.')
elif student_score <= 59:
    print('Your grade is F.')
elif student_score <= 69:
    print('Your grade is D.')
elif student_score <= 79:
    print('Your grade is C.')
elif student_score <= 89:
    print('Your grade is B.')
else:
    print('Your grade is A.')

# 2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring. June, July or August, the season is Summer
# Old version - used list first then switched to dict
# autumn = ['September', 'October', 'November']
# winter = ['December', 'January', 'February']
# spring = ['March', 'April', 'May']
# summer = ['June', 'July', 'August']

seasons = {
    'September': 'Autumn',
    'October': 'Autumn',
    'November': 'Autumn',
    'December': 'Winter',
    'January': 'Winter',
    'February': 'Winter',
    'March': 'Spring',
    'April': 'Spring',
    'May': 'Spring',
    'June': 'Summer',
    'July': 'Summer',
    'August': 'Summer'
}

user_month = input('Enter your month: ').title()
if user_month in seasons:
    print(f"The season of {user_month} is {seasons[user_month]}.")
else:
    print('You did not enter a month. Try again.')

# 3. The following list contains some fruits:
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
# I added .lower at input level to make sure every input will be lowercased so it is compared to the actual items in the list
user_fruit = input('Enter your fruit: ').lower()
if user_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(user_fruit)
    print(f"{user_fruit} has been added to the list of fruits: {fruits}")

# Exercises: Level 3

# 1. Here we have a person dictionary. Feel free to modify it!

person = {
    'first_name': 'Testing',
    'last_name': 'McTest',
    'age': 300,
    'country': 'USA',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# A. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills = person['skills'] # Variable reused in B.
    if len(skills) % 2 == 1:
        print(f"Person has skills. Middle skill is {skills[len(skills)//2]}.")
    else:
        print(f"Person has skills. Middle skills are {skills[len(skills)//2-1]} and {skills[len(skills)//2]}.")
else:
   print('Person has no skills.')

# B. Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in skills:
        print(f"{person['first_name']} {person['last_name']} knows Python.") # I have used two different {} because if 'first_name' and 'last_name where in the same {} then the output was a tuple.
    else:
        print(f"{person['first_name']} {person['last_name']} doesn't know Python.")
else:
    print(f"{person['first_name']} {person['last_name']} doesn't have any skills.")

# C. If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

if 'skills' in person:
    skills_set = set(person['skills'])
    if skills_set == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
        print('He is a backend developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print('He is a fullstack developer')
    else:
        print('unknown title')  # intentional lowercase, no dot
else:
    print("He doesn't have any skills.")

# D. If the person is married and if he lives in Finland, print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.

if person['country'] == 'Finland' and person['is_married']:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
else:
    print(f"{person['first_name']} {person['last_name']} either does not live in Finland or is not married.")