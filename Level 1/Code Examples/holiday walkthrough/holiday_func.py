def calculate_flight_cost(city_flight):
    """
    Calculate the cost of a flight based on the destination city

    Args (parameters):
        city_flight (str): the destination city

    Returns:
        float: the cost of the flight (rands)
    """

    flight_costs_dict = {
       "cpt": 1500,
       "jhb": 600,
       "pmb": 800,
       "pe": 560,
       "rsb": 200,
       "pta": 150,
       "pot": 450
    }

    # converting input to lowercase for case-insensitive matching
    city_flight = city_flight.lower()

    # return the cost if city exists in our dictionary
    return flight_costs_dict.get(city_flight, 500)  # default value if city is not in dictionary


def calculate_hotel_cost(num_nights):
    """ 
    Calculate the total hotel cost based on number of nights
    """

    # base cost / rate per night
    price_per_night = 125.50

    # Apply discount for longer days
    if num_nights >= 7:
        # 25% discount for stays of 7+ days
        return (num_nights * price_per_night) - (num_nights * price_per_night * 0.25)
    elif num_nights >= 3:
        # 5% discount for stays 3 - 6 days
        return (num_nights * price_per_night) - (num_nights * price_per_night * 0.05)
    else:
        # no discount for short stays
        return num_nights * price_per_night


def calculate_car_rental(rental_days):
    """ 
    calculate the total cost of car rental based of number of days rented
    """

    # Base cost / rate per day
    daily_rate = 750

    # calculate base cost
    total_cost = daily_rate * rental_days

    # apply discount for rentals of 5+ days
    if rental_days >= 7:
        total_cost -= 100   # R100 discount / off
    elif rental_days >= 3:
        total_cost -= 25    # R25 discount / off

    return total_cost


def calculate_activity_cost(activities):
    """
    calculate the total cost of activities

    Args (parameters):
        actvities (list): list of activities

    Returns:
        float: the cost of all activities
    """

    activity_prices_dict = {
        "sightseeing": 250,
        "surfing": 300,
        "bungie": 150,
        "gameDrive": 100,
        "quadbiking": 700,
        "ziplining": 350,
        "paintBalling": 200,
        "hiking": 50
    }

    total_cost = 0

    # [gameDrive, hiking, BUNGIE, Surfing]

    for activity in activities:
        activity = activity.lower()  # converting user input to lowercase

        # add cost if activity was triggered and exists
        total_cost += activity_prices_dict.get(activity, 30)       # default if activity not found

    return total_cost


# MAIN FUNCTION THAT CALLS ALL THE OTHER FUNCTIONS
def holiday_cost(city_flight, num_nights, rental_days, activities):
    """
    calculate the total holiday cost by combining (sum) all individual costs

    Args:
        city_flight (str): user's desitination city
        num_nights (int): user's number of nights
        rental_days (int): number of days for car rental
        activities (list): list of planned activities

    Returns:
        returning total cost of the holiday

    """

    # call each function and get results to sum up total
    flight_cost = calculate_flight_cost(city_flight)
    hotel_stay = calculate_hotel_cost(num_nights)
    car_hire = calculate_car_rental(rental_days)
    activities_cost = calculate_activity_cost(activities)

    print('\n------------------------------------------')
    print(f"flight to {city_flight}: R{flight_cost}")
    print(f"Hotel ({num_nights} nights): R{hotel_stay}")
    print(f"Car Rental ({rental_days} days): R{car_hire}")
    print(f"Activites Selected\n{activities}: R{activities_cost}")
    print('------------------------------------------\n')

    # Calculate the total cost
    total_holiday_cost = flight_cost + hotel_stay + car_hire + activities_cost

    return total_holiday_cost
