# Example 1
# with open("example.txt", "w") as file:
#     file.write("Hello, world!")

# Example 2
# with open("example.txt", "a") as file:
#     file.write("\nHello, world!")

# Example 3
lines = ['fisk', "milk", "sugar"]
with open("examples.txt", "a") as file:
    file.writelines(lines)
