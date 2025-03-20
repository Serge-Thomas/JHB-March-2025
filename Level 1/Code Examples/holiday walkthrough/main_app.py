from holiday_func import holiday_cost

# ============================= MAIN PROGRAM ========================== #

print("🏖️\tHOLIDAY COST CALCULATOR\t 🏖️")
print("-----------------------------------")

# Getting city from user
print("Enter city code only e.g jhb - johannesburg")
print("\ncpt - cape town\njhb - johannesburg\npmb - pietermaritzberg \
\npe - port elizabeth\nrsb - rustenburg\npta - pretoria \npot - potchefstrom\n")

city = input("Enter the city you are flying to: ")

# getting number of nights
while True:
    try:
        nights = int(input("Enter number of nights staying: "))

        if nights <= 0:
            print("Please enter a postive number that is valid")
            continue
        break
    except ValueError:
        print("Please enter a valid number e.g 3")


# getting number of rental days
while True:
    try:
        days = int(input("Enter number of days renting car: "))

        if days < 0:
            print("Please enter a postive number that is valid")
            continue
        break
    except ValueError:
        print("Please enter a valid number e.g 3")

  
# Getting activites
# print("Enter activites seperated by comma (', '): ")

activities_list = []

while True:
    print("Option include\n sightseeing\n surfing\n bungie\n gameDrive\n quadbiking\
\n ziplining\n paintBalling\n hiking")

    activity_input = input("Enter your activites or enter 'stop' to complete: ").lower()
    if activity_input != "stop":
        activities_list.append(activity_input)
    else:
        print(f"Activies recorded: {activities_list}")
        break


# Calling main function HOLIDAY COST
total_user_cost = holiday_cost(city, nights, days, activities_list)


# Display the results
print("🎉 \tHOLIDAY COST SUMMARY \t 🎉")
print("------------------------------------")

print(f"TOTAL COST: R{total_user_cost}")
print("------------------------------------")

print("Thank you for booking with us.")