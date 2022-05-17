# the for loop
for i in range(0, 10):
    print(i, end=" ")
print("\n")

# step 5
for x in range(0, 100, 5):
    print(x, end=" ")
print("\n")

# While loop

numb = 1
while numb <= 5:
    print(numb, end=" ")
    numb += 1
print("\n")

print("Choose one option for mpesa services")
print("1: Send Money")
print("2: Withdraaw")
print("3: Deposit")
print("4: Quit")

while True:
    num = int(input("Enter an option: "))
    if num == 1:
        print("'Send Money")
    elif num == 2:
        print("Withdraw")
    elif num == 3:
        print("Deposit")
    elif num == 4:
        break
    else:
        print("Invalid option")
