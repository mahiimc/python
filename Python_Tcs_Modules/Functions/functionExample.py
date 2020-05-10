
def square(x):
    return x**2;

for i  in range(1,10):
    print(square(i),end=" ")

def greet(name, greetMsg="Good morning"):
    print(name+" "+greetMsg+" !")
    
greet("mahesh");

"""def greet2 (greetMsg="Good Morning !" ,name):   #SyntaxError: non-default argument follows default argument
    print(name+" "+greetMsg)"""
    
def var_length_args (*args):
    for arg in args:
        print(arg , end=" ")

var_length_args("mahesh","mahi","imc")

def kwarg_function (**kwargs):
    for key , value in kwargs.items():
        print("%s == %s"%(key,value))
        
kwarg_function(first="Hello this is mahesh",second="mahesh")

#args and kwargs together

def var_together(*args , ** kwargs):
    print(args)
    print(kwargs)
    
    
var_together("mahesh","mahi",first="mahesh", second="mahi")






