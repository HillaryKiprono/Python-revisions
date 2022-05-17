# Write a Python program to create a set
print("Create a new set:")
x = set()
print(x)
print(type(x))
print("\nCreate a non empty set:")
n = set([0, 1, 2, 3, 4])
print(n)
print(type(n))
print("\nUsing a literal:")
a = {1,2,3,'foo','bar'}
print(type(a))
print(a)

# Write a Python program to iteration over sets.
#Create a set
num_set = set([0, 1, 2, 3, 4, 5])
for n in num_set:
  print(n, end=' ')
print("\n\nCreating a set using string:")
char_set = set("w3resource")
# Iterating using for loop
for val in char_set:
    print(val, end=' ')

# Write a Python program to add member(s) in a set
#A new empty set
color_set = set()
print(color_set)
print("\nAdd single element:")
color_set.add("Red")
print(color_set)
print("\nAdd multiple items:")
color_set.update(["Blue", "Green"])
print(color_set)

# Write a Python program to remove item(s) from a given set.
num_set = set([0, 1, 3, 4, 5])
print("Original set:")
print(num_set)
num_set.pop()
print("\nAfter removing the first element from the said set:")
print(num_set)

# Write a Python program to remove an item from a set if it is present in the set.
#Create a new set
num_set = set([0, 1, 2, 3, 4, 5])
print("Original set elements:")
print(num_set)
print("\nRemove 0 from the said set:")
num_set.discard(4)
print(num_set)
print("\nRemove 5 from the said set:")
num_set.discard(5)
print(num_set)
print("\nRemove 2 from the said set:")
num_set.discard(5)
print(num_set)
print("\nRemove 7 from the said set:")
num_set.discard(15)
print(num_set)

# Write a Python program to create an intersection of sets
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx & sety
print(setz)

# Write a Python program to create a union of sets.
setc1 = set(["green", "blue"])
setc2 = set(["blue", "yellow"])
print("Original sets:")
print(setc1)
print(setc2)
setc = setc1.union(setc2)
print("\nUnion of above sets:")
print(setc)
setn1 = set([1, 1, 2, 3, 4, 5])
setn2 = set([1, 5, 6, 7, 8, 9])
print("\nOriginal sets:")
print(setn1)
print(setn2)
print("\nUnion of above sets:")
setn = setn1.union(setn2)
print(setn)

# Write a Python program to create set difference.
setc1 = set(["green", "blue"])
setc2 = set(["blue", "yellow"])
print("Original sets:")
print(setc1)
print(setc2)
r1 = setc1.difference(setc2)
print("\nDifference of setc1 - setc2:")
print(r1)
r2 = setc2.difference(setc1)
print("\nDifference of setc2 - setc1:")
print(r2)
setn1 = set([1, 1, 2, 3, 4, 5])
setn2 = set([1, 5, 6, 7, 8, 9])
print("\nOriginal sets:")
print(setn1)
print(setn2)
r1 = setn1.difference(setn2)
print("\nDifference of setn1 - setn2:")
print(r1)
r2 = setn2.difference(setn1)
print("\nDifference of setn2 - setn1:")
print(r2)