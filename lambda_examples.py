x = lambda a: a * 10
print(x(5))

y = lambda a, b: a * b
print(y(2, 3))


def myFunc(n):
    return lambda a: a * n


myDoubler = myFunc(2)

print(myDoubler(11))


def tripplerDoubler(n):
    return lambda a: a * n


myTrippler = tripplerDoubler(3)
print(myTrippler(11))
