# relative ==> file name "example.txt"
# absolute ==> explicit location of file "C:\Users\smugh\OneDrive\Desktop\Work\Code Examples\file IO\example.txt"

# Explicit
file = open("example.txt", "r")
print(file)
file.close()

# Implicit
with open("example.txt", "r") as file:
    pass
    # perform file operations
# file is automatically closed outside the block