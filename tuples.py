# Write a Python program to create a tuple.
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

# Write a Python program to create a tuple with different data types
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

# Write a Python program to unpack a tuple in several variables
tuplex = 4, 8, 3
print(tuplex)
n1, n2, n3 = tuplex
#unpack a tuple in variables
print(n1 + n2 + n3)
#the number of variables must be equal to the number of items of the tuple
n1, n2, n3, n4= tuplex

# Write a Python program to add an item in a tuple.
tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
#adding items in a specific index
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)
#converting the tuple to list
listx = list(tuplex)
#use different ways to add items in list
listx.append(30)
tuplex = tuple(listx)
print(tuplex)

# Write a Python program to convert a tuple to a string.
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str =  ''.join(tup)
print(str)

# Write a Python program to get the 4th element and 4th element from last of a tuple.
#Get an item of the tuple
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print(tuplex)
#Get item (4th element)of the tuple by index
item = tuplex[3]
print(item)
#Get item (4th element from last)by index negative
item1 = tuplex[-4]
print(item1)