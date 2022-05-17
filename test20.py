def anagrams(s1, s2):
    # convert the strings to lower case and sort them

    myList1 = list(s1)
    myList1.sort()
    sortedS1 = "".join(myList1)

    myList2 = list(s2)
    myList2.sort()
    sortedS2 = "".join(myList2)

    return sortedS1 == sortedS2


print(anagrams("joel","timo"))