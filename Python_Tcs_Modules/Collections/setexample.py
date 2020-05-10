setA = {1,2,3,4,5}
setA.add(10)
for i in setA:
    print(i)
    
setB = frozenset({1,2,3,4,5})
setB.add(10);   #frozenset' object has no attribute 'add'
for i  in setB:
    print(i)
