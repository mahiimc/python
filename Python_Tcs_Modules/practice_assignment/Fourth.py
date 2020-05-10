"""4. Write a Python program to accept two strings as input and check if they are identical copy of each other or if 
the second string is a substring of the first string. If they are identical, print "Both the strings are same".
 If the 2nd string is substring of the 1st string, 
print " is a substring of . Please note that the value for String1 and String2 should be printed in place of the holders."""
import re
string_1 = input("String 1 ")
string_2 = input("String 2 ")
if(string_1 == string_2):
    print("Both strings are same")
elif(re.search(string_2, string_1)):
    print("string_2 is a substring of string_1")
else :
    print("Not equal")