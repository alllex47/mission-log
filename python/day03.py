# Day 3: 30 Days of python programming


# 1. Declare your age as integer variable
age = 27
# 2. Declare your height as a float variable
height = 1.93
# 3. Declare a variable that store a complex number
complex_number = 1 + 1j
print(age)
print(height)
print(complex_number)

'''
# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
'''
base = float(input('Enter base of triangle: '))
triangle_height = float(input('Enter height of triangle: '))
area = 0.5 * base * triangle_height
print('The area of the triangle is', area)

'''
# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
    Enter side a: 5
    Enter side b: 4
    Enter side c: 3
    The perimeter of the triangle is 12
'''
side_a = float(input('Enter side a dimension: '))
side_b = float(input('Enter side b dimension: '))
side_c = float(input('Enter side c dimension: '))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is', perimeter)

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
rectangle_length = float(input('Enter rectangle length: '))
rectangle_width = float(input('Enter rectangle width: '))
rectangle_area = rectangle_length * rectangle_width
rectangle_perimeter = 2 * (rectangle_length + rectangle_width)
print('The area of the rectangle is', rectangle_area)
print('The perimeter of the rectangle is', rectangle_perimeter)

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
circle_radius = float(input('Enter circle radius: '))
circle_area = (pi * circle_radius ** 2)
circumference = (2 * pi * circle_radius)
print('The area of the circle is', circle_area)
print('The circumference of the cirlce is', circumference)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
x1_ex8, x2_ex8 =2, 4
y1_ex8 = 2 * x1_ex8 - 2
y2_ex8 = 2 * x2_ex8 - 2
print(y1_ex8)
print(y2_ex8)
m_ex8 = (y2_ex8 - y1_ex8) / (x2_ex8 - x1_ex8)
print(m_ex8)
y_intercept = 2 * 0 - 2
# x-intercept: where the line crosses the x-axis, so y = 0
# solve: 0 = 2x - 2  →  2 = 2x  →  x = 1
x_intercept = 1
x_intercept = 1
print(y_intercept)
print(x_intercept)
# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1_ex9, y1_ex9 = 2, 2
x2_ex9, y2_ex9 = 6, 10

m_ex9 = (y2_ex9 - y1_ex9) / (x2_ex9 - x1_ex9)
distance_ex9 = ((x2_ex9 - x1_ex9) ** 2 + (y2_ex9 - y1_ex9) ** 2) ** 0.5
print(m_ex9)
print(distance_ex9)

# 10. Compare the slopes in tasks 8 and 9.
print(m_ex8 == m_ex9)

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# x=0 → y=9, x=-1 → y=4, x=-2 → y=1, x=-3 → y=0
x = -3
y = x ** 2 + 6 * x + 9
print(y)

#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_python = len('python')
len_dragon = len('dragon')

print(len_python)
print(len_dragon)

print(len_python < len_dragon)
#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon.')

#15. There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon')

#16. Find the length of the text python and convert the value to float and convert it to string
float_python = float(len_python)
print(float_python)
str_python = str(float_python)
print(str_python)

#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number_ex17 = 41
is_even = (number_ex17 % 2 == 0)
print(is_even)

#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division_ex18 = 7 // 3
converted_ex18 = int(2.7)
print(floor_division_ex18 == converted_ex18)

#19. Check if type of '10' is equal to type of 10
type1 = '10'
type2 = 10
print(type(type1) == type(type2))

#20. Check if int('9.8') is equal to 10
 # int('9.8') would crash with ValueError - int() can't parse a string containing a decimal point. Using the float 9.8 instead.
print(int(9.8) == 10)

'''
21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
    Enter hours: 40
    Enter rate per hour: 28
    Your weekly earning is 1120
'''
hours_ex21 = float(input('Enter hours: '))
rate_ex21 = float(input('Enter rate per hour: '))
weekly_earning = hours_ex21 * rate_ex21
print('Your weekly earning is', weekly_earning)

'''
22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
    Enter number of years you have lived: 100
    You have lived for 3153600000 seconds.
'''
years_ex22 = float(input('Enter number of years you have lived: '))
seconds_in_a_year_ex22 = 31536000
seconds_lived_ex22 = years_ex22 * seconds_in_a_year_ex22
print('You have lived for', seconds_lived_ex22, 'seconds.')

'''
23. Write a Python script that displays the following table
    1 1 1 1 1
    2 1 2 4 8
    3 1 3 9 27
    4 1 4 16 64
    5 1 5 25 125
'''
print(1, 1 ** 0, 1 ** 1, 1 ** 2, 1 ** 3)
print(2, 2 ** 0, 2 ** 1, 2 ** 2, 2 ** 3)
print(3, 3 ** 0, 3 ** 1, 3 ** 2, 3 ** 3)
print(4, 4 ** 0, 4 ** 1, 4 ** 2, 4 ** 3)
print(5, 5 ** 0, 5 ** 1, 5 ** 2, 5 ** 3)