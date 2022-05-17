
list2 = [2, 3, 4, 5, 2]

# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
def test_distinct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False


print(test_distinct(list2))

# Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies. 

words = "Joel is Kanyi"
word_list = words.split()

word_freq = [word_list.count(n) for n in word_list]

print("String:\n {} \n".format(words))
print("List:\n {} \n".format(str(word_list)))
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))

# Write a Python program to find the digits which are absent in a given mobile number.
def absent_digits(n):
    all_nums = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    n = set([int(i) for i in n])
    n = n.symmetric_difference(all_nums)
    n = sorted(n)
    return n


print(absent_digits([0,7,0,6,0,0,3,8,9,1]))

primes = [1] * 500000
primes[0] = 0

# Write a Python program to print the number of prime numbers which are less than or equal to a given integer.
for i in range(3, 1000, 2):
    if primes[i // 2]:
        primes[(i * i) // 2::i] = [0] * len(primes[(i * i) // 2::i])

print("Input the number(n):")
n = int(input())
if n < 4:
    print("Number of prime numbers which are less than or equal to n.:", n - 1)
else:
    print("Number of prime numbers which are less than or equal to n.:", sum(primes[:(n + 1) // 2]) + 1)


# Write a Python program that accepts six numbers as input and sorts them in descending order.
print("Input six integers:")
nums = list(map(int, input().split()))
nums.sort()
nums.reverse()
print("After sorting the said ntegers:")
print(*nums)

# Write a Python program which reads a text (only alphabetical characters and spaces.) and prints two words. The first one is the word which occurs most frequently in the text. The second one is the word which has the maximum number of letters.
import collections
print("Input a text in a line.")
text_list = list(map(str, input().split()))
sc = collections.Counter(text_list)
common_word = sc.most_common()[0][0]
max_char = ""
for s in text_list:
    if len(max_char) < len(s):
        max_char = s
print("\nMost frequent text and the word which has the maximum number of letters.")
print(common_word, max_char)

# Given a list of numbers and a number k, write a Python program to check whether the sum of any two numbers from the list is equal to k or not.
def check_sum(nums, k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k:
                return True
    return False
print(check_sum([12, 5, 0, 5], 10))
print(check_sum([20, 20, 4, 5], 40))
print(check_sum([1, -1], 0))
print(check_sum([1, 1, 0], 0))