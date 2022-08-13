#  use a dictionary because lookups are faster
#  Use a dictionary if you want to count occurrences of something. Like the number of pets in a home.
d0 = dict()
d1 = {'a': 1}
print(d1)
# ---------------------------------- dictionary comprehension ----------------------------------
d3 = {val: k for k, val in d1.items()}
print(d3)
d = {i:j for i in range(2) for j in range(2)}
print(d)
# ----------------------------------- inserting a k-v pair in dic ----------------------------------
d1['b'] = 2
print(d1)
# ---------------------------------- deleting a k-v pair from dic ----------------------------------
del d1['b']
print(d1)

# wipes out all the data in a dictionary
# d1.clear()

# ---------------------------------- updating a k-v pair from dic ----------------------------------
d2 = {'z':10}
d1.update(d2)
print(d1)
# ---------------------------------- get keys , values and k-v pairs in a dict -------------------------
for i in d1.items():
    print(i)
for i,j in d1.items():
    print(i,j)
for i in d1.values():
    print(i)
for i in d1.keys():
    print(i)
# ----------------------------------- default dict  -----------------------------------------------------------
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print(i)
# ------------------------------ Dictionary comprehension -----------------------------------------------------

l = ['one','two','three']
m = [1,2,3]
d = {k:v for k,v in zip(l,m)}
print(d)

