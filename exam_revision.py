# x = 10
# y = 31
# word = "python"
# print((x > y) and (((y % 2) == 1) or (word < "boa")))
#
# color = ["red", "blue", "yellow"]
#
# num = 4
# if num > 0:
#     x = 100

# while True:
#     numm = int(input("Enter Number: "))
#     if numm % 2 == 0:
#         break
#     else:
#         print(numm)

square = 2

# def main():
#     square *= square
#     print(square)
#
#
# main()

#
# def greeting(n):
#     for i in range(n):
#         print("Hello World!")
#
#
# greeting(3)

# for n in range(1,6):
#     print(n)

# raw_data = open("wordList.txt", 'r')
# for data in raw_data.readline():
#     notes = data.strip()
#     print(notes)
#
# o_file = open("attendance", 'w')

# counter = 1
# num = int(input("Enter Number: "))
# while num % 2 == 0:
#     return False
# counter = counter + 1

# notes = []
# myFile = open("names.txt",'r')
# for i in myFile:
#     notes.append(i)
# print(notes)
# myFile.close()


# f = open("names.txt", "a")
# f.write("Now the file has more content!")
# f.close()
#
# # open and read the file after the appending:
# f = open("names.txt", "r")
# print(f.read())
#
# a = [1, 2, 3, 4, 5]
# b = [i for i in a if i % 2 == 0]
# print(b)

str1 = input("Enter a word: ")


def isPalidrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


print(isPalidrome(str1))

dictr = {}
dictr.values()
dictr.keys()
myl = list(set(dictr.values()))