# Day 7: 30 Days of python programming

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
# 1. Find the length of the set it_companies
print(f"Length of it_companies set is: {len(it_companies)}.")

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['OpenAI', 'Anthropic', 'Nvidia'])
print(it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('OpenAI')
print(it_companies)

# 5. What is the difference between remove and discard
# Remove returns an error if item not found in set so need to check beforehand if item exists - discard doesn't raise any errors
# it_companies.remove('Meta') - #'d out to not raise KeyError
it_companies.discard('Meta')
print(it_companies)

# Exercises: Level 2

# 1. Join A and B
C = A.union(B)
print(C)
# 2. Find A intersection B

print(A.intersection(B))
# 3. Is A subset of B
print(f"Is A subset of B? - {A.issubset(B)}.")

# 4. Are A and B disjoint sets
print(f"Are A and B disjoint sets? - {A.isdisjoint(B)}.")

# 5. Join A with B and B with A
A_B_union = A.union(B)
B_A_union = B.union(A)
print(A_B_union)
print(B_A_union)

# 6. What is the symmetric difference between A and B
print(f"The symmetric difference between A and B is: {A.symmetric_difference(B)}.")

# 7. Delete the sets completely
# No sense in printing - returns NameError
del A, B

# Exercises: Level 3
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
age_list_length = len(age)
age_set_length = len(age_set)
print(f"List length: {age_list_length}, Set length: {age_set_length}")
print(f"Is the length of the list bigger than the length of the set? {age_list_length > age_set_length}. By how much? {abs(age_list_length - age_set_length)}")

# 2. Explain the difference between the following data types: string, list, tuple and set
# Text is a string data type. Any type of text written in single, double or triple quotes is a string
string_ex = 'This is a string'
print(type(string_ex))

# List is a collection of data, displayed with [ ]. It is ordered and changeable and it allows duplicates.
list_ex = ['Apples', 'Oranges']
print(type(list_ex))

# Tuple is a collection of data, displayed with ( ). It is ordered and unchangeable but it allows duplicates.
tuple_ex = ('Pear', 'Watermelon')
print(type(tuple_ex))

# Set is a collection of data, displayed with { }. It is un-ordered and don't allow changing an element in place.
# It doesn't allow duplicates but it allows new items to be added to a set.
set_ex = {'Garlic', 'Onion'}
print(type(set_ex))

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
sentence_split = sentence.split()
sentence_set = set(sentence_split)
print(f"There are {len(sentence_set)} unique words in the sentence.")
