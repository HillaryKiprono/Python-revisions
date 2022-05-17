# try statement
try:
    readFile = open("wordList.txt", 'r')
    numDependent = int(input("Enter number: "))
    age = numDependent + 20
    print(age)
except:
    print("You didnt enter a number")
finally:
    # close files that were opened
    readFile.close()
