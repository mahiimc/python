import collections

dic = {1:"A",2:"B",3:"C"}
lis =collections.Counter([1,2,1,1,2,3,2,4,5,3,4])

print(collections.Counter(lis))
print(lis.most_common())


