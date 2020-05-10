class Employee :
    count=0;
    def __init__(self,name):
        self.name=name
        Employee.count+=1
    
    @classmethod    
    def getCount(cls):
        print("No of Employees : {0}".format(cls.count))
        
        
e1 = Employee("A")
e2 = Employee("B")
e3 = Employee("C")
e1 = Employee("D")
e2 = Employee("E")
e3 = Employee("F")
e3.getCount()