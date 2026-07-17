# Mission 4 - Planet database v1 (dicts)
# build a dict of dicts — each planet with `distance_au`, `moons`, `gravity` (relative to Earth).
# Look up values, add Pluto, then delete Pluto (sorry).


# Info
# 1 AU = 149597870700 m OR ~499 light-seconds

planets = {
    'Mercury': {
        'distance_au': 0.39,
        'moons': 0,
        'gravity_relative_to_earth': 0.38,
        },
    'Venus': {
        'distance_au': 0.72,
        'moons': 0,
        'gravity_relative_to_earth': 0.91,
    },
    'Earth': {
        'distance_au': 1,
        'moons': 1,
        'gravity_relative_to_earth': 1.0, # Duh
    },
    'Mars': {
        'distance_au': 1.52,
        'moons': 2,
        'gravity_relative_to_earth': 0.38,
    },
    'Jupiter': {
        'distance_au': 5.20,
        'moons': 101,
        'gravity_relative_to_earth': 2.53,
    },
    'Saturn': {
        'distance_au': 9.58,
        'moons': 285,
        'gravity_relative_to_earth': 1.07,
    },
    'Uranus': {
        'distance_au': 19.22,
        'moons': 29,
        'gravity_relative_to_earth': 0.89,
    },
    'Neptune': {
        'distance_au': 30.05,
        'moons': 16,
        'gravity_relative_to_earth': 1.14,
    }
}

# print(planets.values()) - just for testing - it returns a data dump

# Look up values - is this what you meant?
print(f"How many moons does Jupiter have? - {planets['Jupiter']['moons']}")
print(f"How far away is Neptune? - {planets['Neptune']['distance_au']} AU")
print(f"What is the gravity relative to Earth on Saturn? - {planets['Saturn']['gravity_relative_to_earth']}")

# Adding Pluto
planets['Pluto'] = {
        'distance_au': 39.5,
        'moons': 5,
        'gravity_relative_to_earth': 0.063,
    }
# print(planets) - just for testing - Pluto was added


# Removing Pluto
# I used del because the title said 'delete' but I could have used pop('Pluto') and also popitem() since Pluto was the last item in the dictionary
del planets['Pluto']
# print(planets) - just for testing - Pluto was deleted
