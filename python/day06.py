#Day 6: 30 Days of python programming

# Exercises: Level 1

# 1. Create an empty tuple
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers_tuple = ('John', 'Michael')
sisters_tuple = ('Jane', 'Samantha')
print(brothers_tuple)
print(sisters_tuple)

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers_tuple + sisters_tuple
print(siblings)

# 4. How many siblings do you have?
print(f'How many siblings?: {len(siblings)}')

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# v1
# family_members = list(siblings)
# family_members.append('Trevor')
# family_members.append('Amanda')
# family_members = tuple(family_members)
# print(family_members)

# v2 - I like v2 better, it's cleaner and easier to write
parents_ex5 = ('Trevor', 'Amanda')
family_members = siblings + parents_ex5
print(family_members)

# Exercises: Level 2

# 1. Unpack siblings and parents from family_members
# Used *for siblings because they were the bigger group so it was more efficient to write 2 parents_ variables instead of 4 siblings ones.
*siblings_ex1, parent_1, parent_2 = family_members
print(f'Siblings: {siblings_ex1}.')
print(f'Parents: {parent_1}, {parent_2}.')
# print(type(siblings_ex1))

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apple', 'Pear', 'Banana')
vegetables = ('Cucumber', 'Onion', 'Carrot')
animal_products = ('Eggs', 'Milk', 'Wool')
food_stuff_tp = fruits + vegetables + animal_products

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
number_of_food_items = len(food_stuff_lt)
# even_check = number_of_food_items % 2 #'d out on purpose - only needed it once to check - ODD
middle_index = number_of_food_items // 2
middle_items = food_stuff_lt[middle_index:middle_index + 1]   
print(f'Middle item: {middle_items}.')

# 5. Slice out the first three items and the last three items from food_stuff_lt list
first_three_items, last_three_items = food_stuff_lt[0:3], food_stuff_lt[-3:]
print(f'First three items in the list are: {first_three_items}.\nLast three items in the list are: {last_three_items}.')

# 6. Delete the food_stuff_tp tuple completely
# no point in printing since it returns a NameError
del food_stuff_tp
# print(food_stuff_tp)

# 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
    # Check if 'Estonia' is a nordic country
print(f"Is Estonia a nordic country? - {'Estonia' in nordic_countries}.")

    # Check if 'Iceland' is a nordic country
print(f"Is Iceland a nordic country? - {'Iceland' in nordic_countries}.")
