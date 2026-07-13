# Day 4: 30 Days of python programming

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# 2 versions below - also reused the space variable
training_ex1 = ['Thirty', 'Days', 'Of', 'Python']
result_ex1_v1 = ' '.join(training_ex1)
print(result_ex1_v1)
training_1 = 'Thirty'
training_2 = 'Days'
training_3 = 'Of'
training_4 = 'Python'
space = ' '
result_ex1_v2 = training_1 + space + training_2 + space + training_3 + space + training_4
print(result_ex1_v2)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# 2 versions below
training_ex2 = ['Coding', 'For', 'All']
result_ex2_v1 = ' '.join(training_ex2)
print(result_ex2_v1)
coding_1 = 'Coding'
coding_2 = 'For'
coding_3 = 'All'
space = ' '
result_ex2_v2 = coding_1 + space + coding_2 + space + coding_3
print(result_ex2_v2)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# 4. Print the variable company using print().
print(company)

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut(slice) out the first word of Coding For All string.
first_word = company[0:company.find(' ')]
print(first_word)

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))

# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# 12. Change "Python for Everyone" to "Python for All" using the replace method or other methods.
company_2 = 'Python for Everyone'
print(company_2.replace('Everyone', 'All'))

# 13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies_ex14 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies_ex14.split(', '))

# 15. What is the character at index 0 in the string Coding For All.
index0_ex15 = company[0]
print(index0_ex15)

# 16. What is the last index of the string Coding For All.
print(len(company) - 1)

# 17. What character is at index 10 in "Coding For All" string.
print(company[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
print(company_2[0] + company_2.upper()[7] + company_2[11])

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
print(company[0] + company[7] + company[11])

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
company_3 = 'Coding For All People'
print(company_3.rfind('l'))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# I reuse the sentence variable on purpose
# same as ex 26
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# same as ex 27
start = sentence.find('because')                    # 31 — where the first 'because' begins
end   = sentence.rfind('because') + len('because')  # 47 + 7 = 54 — where the last one ENDS
print(sentence[start:end])

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# same as ex 23
print(sentence.find('because'))

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# same as ex 25
start = sentence.find('because')                    # 31 — where the first 'because' begins
end   = sentence.rfind('because') + len('because')  # 47 + 7 = 54 — where the last one ENDS
print(sentence[start:end])
# OR:
print(sentence[31:54])

# 28. Does 'Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

# 29. Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
spaces_ex30 = '   Coding For All      '
print(spaces_ex30.strip())

'''
31. Which one of the following variables return True when we use the method isidentifier():
    30DaysOfPython
    thirty_days_of_python
'''
variable_ex31_v1 = '30DaysOfPython'
variable_ex31_v2 = 'thirty_days_of_python'
print(variable_ex31_v1.isidentifier())
print(variable_ex31_v2.isidentifier())

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result_ex32 = '# ' .join(python_libraries)
print(result_ex32)

'''
33.Use the new line escape sequence to separate the following sentences.
    I am enjoying this challenge.
    I just wonder what is next.
'''
print('I am enjoying this challenge.\nI just wonder what is next.')
'''
34. Use a tab escape sequence to write the following lines.
    Name      Age     Country   City
    Asabeneh  250     Finland   Helsinki
'''
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')
'''
35. Use the string formatting method to display the following:
    radius = 10
    area = 3.14 * radius ** 2
    The area of a circle with radius 10 is 314 meters square.
'''
radius_ex35 = 10
area_ex35 = 3.14 * radius_ex35 ** 2
formated_string_ex35 = 'The area of a circle with radius {} is {:.0f} meters square.' .format(radius_ex35, area_ex35)
print(formated_string_ex35)
'''
36. Make the following using string formatting methods:
    8 + 6 = 14
    8 - 6 = 2
    8 * 6 = 48
    8 / 6 = 1.33
    8 % 6 = 2
    8 // 6 = 1
    8 ** 6 = 262144
'''
a_ex36 = 8
b_ex36 = 6
print(f'{a_ex36} + {b_ex36} = {a_ex36 + b_ex36}')
print(f'{a_ex36} - {b_ex36} = {a_ex36 - b_ex36}')
print(f'{a_ex36} * {b_ex36} = {a_ex36 * b_ex36}')
print(f'{a_ex36} / {b_ex36} = {a_ex36 / b_ex36:.2f}')
print(f'{a_ex36} % {b_ex36} = {a_ex36 % b_ex36}')
print(f'{a_ex36} // {b_ex36} = {a_ex36 // b_ex36}')
print(f'{a_ex36} ** {b_ex36} = {a_ex36 ** b_ex36}')