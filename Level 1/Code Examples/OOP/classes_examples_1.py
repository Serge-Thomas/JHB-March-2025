class Dog:
    # Class attribute - shared by all instances
    species = "Canis Familirias"
    
    # Initializer / constructor (special method)
    def __init__(self, name, age):
        # Instance attributes - unique to each instance (object)
        self.name = name
        self.age = age
   
    # Instance Method
    def describe(self):
        return f"{self.name} is {self.age} years old"

    # Instance Method (another one ☝️)
    def speak(self, sound):
        return f"{self.name} says {sound}"


# Creating instances
hulk = Dog("Hulk Ngwenya", 4)
spotty = Dog("Spotty Malote", 2)
danger = Dog("Danger Gevaar", 7)
thaeddeus = Dog("Thaeddeus Ross", 10)

# Accessing attributes
print(hulk.name)
print(danger.age)


# Access or use the methods
print(spotty.describe())
print(thaeddeus.speak("woof"))


# Access a class attributes
print(spotty.species)
print(danger.species)
print(thaeddeus.species)
print(hulk.species)


"""
    The 'self' parameter is a reference
    to the current instance of the class
    and is used to access variables and
    methods associated with the instance.

    It's automatically passed when you call
    an instance method.

    It's invisible, and it acts as an 'i' statement
    which attaches to attributes to that specific
    object
"""
