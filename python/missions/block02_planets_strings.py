# Mission 2 - Planets (strings)
# Take `"mercury venus earth mars jupiter saturn uranus neptune"` — Split it into a list, capitalize each, count letters in each name, find which names contain the letter "u", join them back with " → ".
 

#Default string + capitalization
planets = 'mercury venus earth mars jupiter saturn uranus neptune'
capitalized_planets = planets.title()
print(capitalized_planets)

#Split into list
planets_to_list = capitalized_planets.split()
print(planets_to_list)

#Letter count
print(f'{planets_to_list[0]} has {len(planets_to_list[0])} letters.')
print(f'{planets_to_list[1]} has {len(planets_to_list[1])} letters.')
print(f'{planets_to_list[2]} has {len(planets_to_list[2])} letters.')
print(f'{planets_to_list[3]} has {len(planets_to_list[3])} letters.')
print(f'{planets_to_list[4]} has {len(planets_to_list[4])} letters.')
print(f'{planets_to_list[5]} has {len(planets_to_list[5])} letters.')
print(f'{planets_to_list[6]} has {len(planets_to_list[6])} letters.')
print(f'{planets_to_list[7]} has {len(planets_to_list[7])} letters.')

#U-hunting
print(f'{planets_to_list[0]} has letter \'u\'? - {'u' in planets_to_list[0]}')
print(f'{planets_to_list[1]} has letter \'u\'? - {'u' in planets_to_list[1]}')
print(f'{planets_to_list[2]} has letter \'u\'? - {'u' in planets_to_list[2]}')
print(f'{planets_to_list[3]} has letter \'u\'? - {'u' in planets_to_list[3]}')
print(f'{planets_to_list[4]} has letter \'u\'? - {'u' in planets_to_list[4]}')
print(f'{planets_to_list[5]} has letter \'u\'? - {'u' in planets_to_list[5]}')
print(f'{planets_to_list[6]} has letter \'u\'? - {'u' in planets_to_list[6]}')
print(f'{planets_to_list[7]} has letter \'u\'? - {'u' in planets_to_list[7]}')

#Join with →
planets_joined = ' → '.join(planets_to_list)
print(planets_joined)