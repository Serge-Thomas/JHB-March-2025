# READING

# Example 1
# with open("example.txt", "r") as file:
    # # read() - return everthing as one string
    # print(file)
    # content = file.read()
    # print(content)
    
    # """
    # output:
    
    # " manchester united is the best team in the premier league
    # new york is a bad city
    # paris is giving zimbabwe
    # c63 is better than an M4
    # messi is the goat "
    
    # """

# Example 2
# with open("example.txt", "r") as file:
#     content = file.readline()
#     print(content)
    
#     """
#     output: 
    
#     " manchester united is the best team in the premier league "
    
#     """

# Example 3
with open("example.txt", "r") as file:
    content = file.readlines()
    # print(content)
    print(content[-1])
    for line in content:
        print(line.strip())
