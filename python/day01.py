# Day 1 - 30 Days of Python

'''
Exercise: Level 1 (actually level 2 - only doing it in VSCode)

1. Check the python version you are using
checked with python --version
2.Open the python interactive shell and do the following operations. The operands are 3 and 4.
    addition(+)
    subtraction(-)
    multiplication(*)
    modulus(%)
    division(/)
    exponential(**)
    floor division operator(//)
3. Write strings on the python interactive shell. The strings are the following:
    Your name
    Your family name
    Your country
    I am enjoying 30 days of python
4. Check the data types of the following data:
    10
    9.8
    3.14
    4 - 4j
    ['Asabeneh', 'Python', 'Finland']
    Your name
    Your family name
    Your country


Exercise: Level 3

1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
2. Find an Euclidean distance between (2, 3) and (10, 8)

'''
# Level 1 - 2
print(3 + 4)
print(4 - 3)
print(3 * 4)
print(4 % 3)
print(4 / 3)
print(4 ** 3)
print(4 // 3)

# Level 1 - 3
print('Alex')
print('Family Name')
print('Romania')
print('I am enjoying 30 days of python')

# Level 1 - 4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Alex'))
print(type('Family Name'))
print(type('Romania'))

# Level 3 - 1
print(type(10))                                    # int
print(type(9.81))                                  # float
print(type(1 + 2j))                                # complex
print(type('Alex'))                                # str
print(type(True))                                  # bool
print(type([0, 1, 2, 3, 4, 5]))                    # list
print(type(('Earth', 'Mars', 'Jupiter')))          # tuple
print(type({2, 3, 4, 5}))                          # set
print(type({'name': 'Alex', 'country': 'Romania'})) # dict

# Level 3 - 2
x1, y1 = 2, 3
x2, y2 = 10, 8
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(distance)