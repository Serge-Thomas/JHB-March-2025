# This program makes recommendations based on two factors: whether it's raining and what the temperature is. 
# First, it checks if it's raining. If it is, it then checks if it's cold to decide what to recommend. 
# If it's not raining, it checks how warm it is to make an appropriate suggestion.

temperature = 68
is_raining = False

print("Weather Activity Helper:")

if is_raining:
    print("It's raining outside!")
    if temperature < 50:
        print("It's cold and wet. Stay inside with a good book.")
    else:
        print("Grab an umbrella and rain boots.")
else:
    print("No rain today!")
    if temperature > 80:
        print("It's hot! Go swimming or get ice cream.")
    elif temperature > 60:
        print("Perfect weather for a walk in the park.")
    else:
        print("It's a bit chilly. Take a light jacket for outdoor activities.")
