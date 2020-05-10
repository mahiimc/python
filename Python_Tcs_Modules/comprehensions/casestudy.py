rollno = ["B141699","B141517","B141562","B141061"]
cgpa = [7.32,8.3,8.5,9]
names=["Mahesh","Maruthi","Harish","Vijay"]
output = list(zip(rollno,names,cgpa))
for roll,gpa,name in output:
    print("%s\t%s\t%s "%(roll,gpa,name))