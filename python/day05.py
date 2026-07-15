# Day 5: 30 Days of python programming

# Exercises - Level 1

# 1. Declare an empty list
empty_list = []
print(len(empty_list))

# 2. Declare a list with more than 5 items
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']
print(planets)

# 3. Find the length of your list
print(len(planets))

# 4. Get the first item, the middle item and the last item of the list
first_planet = planets[0]
middle_planet = planets[3]
last_planet = planets[-1]
print(f'First planet: {first_planet}, Middle planet: {middle_planet}, Last planet: {last_planet}.')

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Alex', 27, 1.93, 'Not Married', 'Earth']
print(mixed_data_types)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[3]
last_company = it_companies[-1]
print(f'First Company: {first_company}, Middle Company: {middle_company}, Last Company: {last_company}.')


# 10. Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Nvidia')
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(4, 'OpenAI')
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = it_companies[3].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;  '
it_companies_joined_ex14 = '#;  '.join(it_companies)
print(it_companies_joined_ex14)

# 15. Check if a certain company exists in the it_companies list.
company_exists_ex15 = 'Anthropic' in it_companies
print(company_exists_ex15)

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
it_companies_first3 = it_companies[0:3]
print(it_companies_first3)

# 19. Slice out the last 3 companies from the list
it_companies_last3 = it_companies[-3:]
print(it_companies_last3)

# 20. Slice out the middle IT company or companies from the list
print(it_companies[4:5])

# 21. Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# 22. Remove the middle IT company or companies from the list
# switched from pop to delete 
del it_companies[3:5]
print(it_companies)

# 23. Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies
# print(it_companies) - raises NameError - del worked

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
'''v1
front_end.extend(back_end)
print(front_end)
'''

#v2 - I know this duplicates the back end list if v1 wasn't #'d out, I left it just for the exercise
development = front_end + back_end
print(development)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = development.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

# Exercises - Level 2

# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    # Sort the list and find the min and max age
ages.sort()
min_age, max_age = ages[0], ages[-1]
print(f'Min age: {min_age}, Max age: {max_age}.')

    # Add the min age and the max age again to the list
ages.insert(0, min_age)
ages.append(max_age)
print(ages)

    # Find the median age (one middle item or two middle items divided by two)
#reused number_of_ages on purpose
#median_age depends on the list being sorted
number_of_ages = len(ages)
middle_index = number_of_ages // 2
median_age = (ages[middle_index - 1] + ages[middle_index]) / 2
print(median_age)

    # Find the average age (sum of all items divided by their number )
sum_ages = sum(ages)
average_ages = sum_ages / number_of_ages
print(average_ages)

    # Find the range of the ages (max minus min)
range_ages = max_age - min_age
print(range_ages)

    # Compare the value of (min - average) and (max - average), use abs() method
min_distance = abs(min_age - average_ages)
max_distance = abs(max_age - average_ages)
print(f'Min distance: {min_distance}, Max distance: {max_distance}')
print(f'Is the min distance from the average higher than the max distance from the average? {min_distance > max_distance}. By {abs(min_distance - max_distance)}')

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
# 2. Find the middle country(ies) in the countries list
number_of_countries = len(countries)
# even_check = number_of_countries % 2 - #'d out on purpose - only needed it once to check - ODD
middle_index = number_of_countries // 2
print(f'Middle country: {countries[middle_index]}')

# 3. Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = countries[:middle_index + 1] # Odd list - one more country in first half
second_half = countries[middle_index + 1:]
print(first_half)
print(second_half)
# 4. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries_ex4 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us, *scandic = countries_ex4
print(ch)
print(ru)
print(us)
print(scandic)