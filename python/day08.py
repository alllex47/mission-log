# Day 8: 30 Days of python programming

# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Rufus'
dog['color'] = 'Yellow'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 2
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Testing',
    'last_name': 'McTest',
    'gender': 'Male',
    'age': 300,
    'marital status': 'Married',
    'skills': ['Python', 'Golf', 'Java','Football'],
    'country': 'USA',
    'city': 'New York',
    'address':{
        'street': 'Flatbush Ave',
        'zipcode': '00000'
        }
}
print(student)
# 4. Get the length of the student dictionary
print(len(student))

# 5. Get the value of skills and check the data type, it should be a list
skills_value = student['skills']
print(skills_value)
print(type(skills_value))

# 6. Modify the skills values by adding one or two skills
student['skills'].append('Basketball')
student['skills'].append('React')
print(skills_value)

# 7. Get the dictionary keys as a list
student_keys_list = list(student.keys())
print(student_keys_list)

# 8. Get the dictionary values as a list
student_values_list = list(student.values())
print(student_values_list)

# 9. Change the dictionary to a list of tuples using items() method
student_tuple = list(student.items())
print(student_tuple)

# 10. Delete one of the items in the dictionary
student.pop('city')
print(student)

# 11. Delete one of the dictionaries
# as always, no need for print since it returns error
del dog