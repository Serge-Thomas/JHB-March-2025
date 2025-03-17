# file walkthrough

first_last_word_list = []

with open("example.txt", "r+") as file:
    content = file.readlines()
    for line in content:
        line_split = line.strip("\n").split(" ")
        # print(line_split)

        # returnign the first word and last word combined
        # 
        # print(f"{line_split[0]} {line_split[-1]}")
        
        first_last_word_list.append(f"{line_split[0]} {line_split[-1]}")

# print(first_last_word_list)
for item in first_last_word_list:
    print(item)