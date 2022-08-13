# A tuple is an immutable, ordered collection of objects. Python’s creator intended tuples for heterogenous data.
# Tuples are Python's way of packaging heterogeneous pieces of information in a composite object.
# Immutable Tuples
# they are quicker to access compared to list
# occupy lesser space compare to list

from sys import getsizeof
t1, l = ('one', 'two'), ['one', 'two']
print('size of a tuple in bytes->', getsizeof(t1))
print('size of a list in bytes->', getsizeof(l))
# ------------------------------------ sorted   ------------------------------------
# The function returns a list with the items of tuple sorted in ascending order.
t = tuple([11,2,2,2,2,2,3,3])
print(sorted(t))
# ------------------------------------ count  ------------------------------------
print(t.count(2))
# ------------------------------------ index  ------------------------------------
print(t.index(11))
# ------------------------------------ del  ------------------------------------
s = (1,2,3)
print(s)
del s
# print(s) => NameError: name 's' is not defined
# ------------------------------------ How to add an element to a tuple?  ------------------------------------
# Since tuples are immutable, elements cannot be added/modified/deleted from a tuple.

# ------------------------------------How to Sort List Of Tuples By Second Element------------------------------------
lang_listtuple= [('C#',9), ('Go',7), ('Basic',8), ('Python',6)]
lang_listtuple.sort(key = lambda l:l[1])
print(lang_listtuple)


