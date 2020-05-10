"""3. Write a Python program to print the multiplication table of a number. The number is to taken as user input.
"""

num = int(input("Num :"))
for i in range(1,11):
    print("%d * %d = %d"%(num,i,num*i))