data_list = []
data_in_file = open("wordList.txt",'r')
for line in data_in_file:
    if line.startswith("x"):
        data_list.append( line.strip())
#data_in_file.close()
print(data_list)

# Using list comprehension
new_list = [line.strip() for line in data_in_file if line.startswith("v")]
print(new_list)

data_in_file.close()