from collections import Counter 
filter_output =list(filter(lambda x: x%5  == 0 and x%25 == 0 , range(100)))
c=Counter(filter_output)
# filter can take only one iterable 
print(filter_output)
print(c)