# Write a Python program to calculate the length of a string.
name = input("Enter your String: ")
print(len(name))

#

"""
Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead the empty string. 
Sample String : 'elephant'
Expected Result : 'elnt'
Sample String : 'ba'
Expected Result : 'baba'
Sample String : 'b'
Expected Result : Empty String
"""

str = input("Enter a string: ")
if len(str) < 2:
    print("Empty String")
else:
    print(str[0:2] + str[-2] + str[-1])


"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. 
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""
str2 = input("Enter a string: ")
if not str2.endswith('ing') and len(str2) >= 3:
    print(str2+"ing")
elif str2.endswith('ing'):
    print(str2+"ly")
elif len(str2) < 3:
    print(str2)

"""
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""
str3 = "abc"
str4 = "xyz"
newStr3 = str3.replace(str3[0:2], str4[0:2])
newStr4 = str4.replace(str4[0:2], str3[0:2])
print(f"{newStr3} {newStr4}")

"""Write a Python program to clone or copy a list"""
counties = ["nakuru", "kiambu", "kisumu", "maasai mara"]
location = counties.copy()
print(location)

"""sum all the items in a list."""
nums = [1,2,3,4]
mySum = sum(nums)
print(mySum)


"""get the largest number from a list """
print(max(nums))

"""get the smallest number from a list"""
print(min(nums))
