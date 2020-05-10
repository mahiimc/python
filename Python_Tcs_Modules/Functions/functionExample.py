def square(x):
    return x**2;

for i  in range(1,10):
    print(square(i),end=" ")

def greet(name, greetMsg="Good morning"):
    print(name+" "+greetMsg+" !")
    
greet("mahesh");

def greet2 (greetMsg="Good Morning !" ,name):   #SyntaxError: non-default argument follows default argument
    print(name+" "+greetMsg)
