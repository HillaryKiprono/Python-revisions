
# def anagrams(s1, s2):
#     # convert the strings to lower case and sort them
#
#     myList1 = list(s1)
#     myList1.sort()
#     sortedS1 = "".join(myList1)
#
#     myList2 = list(s2)
#     myList2.sort()
#     sortedS2 = "".join(myList2)
#
#     return sortedS1 == sortedS2
#
#
# def create_key(word):
#     letters = []
#     for c in word:
#         letters.append(c.lower())
#     letters = sorted(letters)
#     return ''.join(letters)
#
#
# def build_dictionary():
#     words_list = []
#     anagramsDictionary = {}
#     raw_word_list = open('wordList.txt', 'r')
#     for line in raw_word_list.readlines():
#         word = line.strip()
#         if word.startswith("v"):
#             words_list.append(word)
#     raw_word_list.close()
#     for word in words_list:
#         key = create_key(word)
#         if key not in anagramsDictionary:
#             anagramsDictionary[key] = []
#         anagramsDictionary[key].append(word)
#     return anagramsDictionary
#
#
# build_dictionary()
#
#
# def find_all_anagrams(listOfWords):
#     anagrams_list = []
#
#     for data_item in listOfWords:
#         for key, values in build_dictionary().items():
#                 print("".join(values))
#
#     return anagrams_list
#
#
# wordsList = ["serve", "rival", "lovely", "caveat", "devote", "irving", "livery", "selves", "latvian", "saviour",
#              "observe", "octavian", "dovetail", "levantine"]
#
# print(find_all_anagrams(wordsList))