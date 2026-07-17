# Mission 3 - Moon math (sets)
# Make sets of Jupiter's 4 Galilean moons and Saturn's 5 biggest moons. 
# Practice union, intersection (spoiler: empty — prove it in code), and adding a newly "discovered" moon.


# Four Galilean moons: Io, Europa, Ganymede, Callisto
galilean_moons = {'Io', 'Europa', 'Ganymede', 'Callisto'}
print(galilean_moons)

# Saturn's five biggest moons: Titan, Rhea, Iapetus, Dione, Tethys
saturn_biggest_moons = {'Titan', 'Rhea', 'Iapetus', 'Dione', 'Tethys'}
print(saturn_biggest_moons)


# Union
unified_moons = galilean_moons.union(saturn_biggest_moons) # The 4 Galilean moons + Saturn's five biggest moons 
print(unified_moons)

# Intersection
print(galilean_moons.intersection(saturn_biggest_moons)) # returns set() - no shared moons - explanation below
print(f"Do Jupiter and Saturn share any moons? - {not galilean_moons.isdisjoint(saturn_biggest_moons)}")

# Add the 6th biggest Saturn moon
saturn_biggest_moons.add('Enceladus') # Adding Enceladus to the set of Saturn's biggest moons
print(saturn_biggest_moons)