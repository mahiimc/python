numbers = [[1,3,5,7,9],[2,4,6,8,10],[0,-1,2],["1699"],[1699]]
outputlist = [term  for  i in numbers for term in i if isinstance(term,int)]
print(outputlist)
