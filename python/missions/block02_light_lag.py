# Mission 1 - Light-lag calculator (variables + operators)
    # Store the Sun-Mars distance in km, divide by the speed of light, print how many minutes a signal from a Mars rover takes to reach Earth. 
    # Then do Jupiter and Neptune.

# The prompt says Sun-Mars distance, but a rover signal travels from Mars to Earth.
# I am using average Earth-planet distances because that matches the actual signal path.

# Constants
# All distances are averages and approximations
# sun_mars_distance_km = 228000000 - added just because it was in the prompt - never used
earth_mars_distance_km = 225000000
earth_jupiter_distance_km = 714000000
earth_neptune_distance_km = 4400000000
light_speed_kms = 299792

#Signal calculated in minutes
earth_mars_signal_minutes = (earth_mars_distance_km / light_speed_kms) / 60
print(f'A signal from a Mars rover takes {earth_mars_signal_minutes:.2f} minutes to reach Earth.')

earth_jupiter_signal_minutes = (earth_jupiter_distance_km / light_speed_kms) / 60
print(f'A signal from a Jupiter orbiter takes {earth_jupiter_signal_minutes:.2f} minutes to reach Earth.') # Jupiter and Neptune are gas giants - they can't have rovers

earth_neptune_signal_minutes = (earth_neptune_distance_km / light_speed_kms) / 60
print(f'A signal from a Neptune orbiter takes {earth_neptune_signal_minutes:.2f} minutes to reach Earth.')
