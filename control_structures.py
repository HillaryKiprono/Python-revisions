## and or, not -> evaluates to True or False

print(1 <= 1)
print(1 < 1)
print("car" < "dog")
print("dog" < "dog")
print("Dog" < "dog")
print("fun" in "refunded")

a = 5
b = 4
c = "python"

print((a + b) < (2 * a))
print(len(c) - b) == (a / 2)
# print(c<("good"+b))

list1 = [6, 4, -5, 3.5]
list2 = ["ha", "hi", "he", "hu", "ho"]
list2.sort()
list1.sort()
print(list1)
print(list2)

n = 4
name = "Brandy"
answ = "Y"
print((2 < n) and (n < 6))
print((2 < n) or (n == 6))
print(not (n < 6))
print((answ == "Y") or (answ == "y"))
print(name.startswith("B"))
print(name.endswith("y"))
