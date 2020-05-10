from _functools import reduce
x=32
print(int(reduce(lambda x,y: x*y,[1] if x == 0 else range(1,x+1))))