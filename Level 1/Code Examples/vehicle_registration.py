"""
    You need to build a console-based vehicle management system where users can:
    
    ✔ Create different types of vehicles (Car, Motorcycle, Truck).
    ✔ Store vehicle details in a text file (vehicles.txt) for persistence.
    ✔ Load stored vehicles from the file on startup.
    ✔ Display vehicle details dynamically.
    
    
    Store data in a simple format like:
        Car,Toyota,Corolla,2020,Petrol,450
        Motorcycle,Yamaha,R1,2021,Petrol,False
        Truck,Ford,F-150,2018,Diesel,2000
"""


FILE_NAME = "vehicles.txt"

# 🚙 Base class: Vehicle
class Vehicle:
    def __init__(self, brand, model, year, fuel_type):
        """Initialize common attributes for all vehicles."""
        pass

    def start_engine(self):
        """Print a message indicating the engine is starting."""
        pass

    def stop_engine(self):
        """Print a message indicating the engine is stopping."""
        pass

    def describe(self):
        """Return a formatted string with vehicle details."""
        pass

# 🚗 Derived class: Car
class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type, trunk_size):
        """Initialize Car attributes using Vehicle."""
        pass

    def open_trunk(self):
        """Print a message indicating the trunk is opening."""
        pass

# 🏍 Derived class: Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, fuel_type, has_sidecar):
        """Initialize Motorcycle attributes using Vehicle."""
        pass

    def pop_wheelie(self):
        """Print a message that the motorcycle pops a wheelie."""
        pass

# 🚛 Derived class: Truck
class Truck(Vehicle):
    def __init__(self, brand, model, year, fuel_type, cargo_capacity):
        """Initialize Truck attributes using Vehicle."""
        pass

    def load_cargo(self):
        """Print a message indicating cargo is being loaded."""
        pass

# 📂 File Handling Functions
def save_vehicles(vehicles):
    """Save the list of vehicles to a file."""
    pass

def load_vehicles():
    """Load vehicles from a file and return a list."""
    pass

# 🚀 Vehicle Management System
vehicles = load_vehicles()

def add_vehicle():
    """Prompt the user to add a new vehicle."""
    pass

def display_vehicles():
    """Display all stored vehicles and their details."""
    pass

# 🏁 Main program loop
while True:
    print("\nVehicle Management System")
    print("1. Add Vehicle")
    print("2. Display Vehicles")
    print("3. Save and Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        print("Saving data and exiting program...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")