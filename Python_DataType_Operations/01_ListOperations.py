## Lists are mutable and iterable and ordered
# x = [1]
# print(id(x),':',x) #=> 4501046920 : [1]
# x.append(5)
# x.extend([6,7])
# print(id(x),':',x) #=> 4501046920 : [1, 5, 6, 7]

# time complexity
# Insert             : O(n)
# delete             : O(n)
# finding an element : O(1)

## Use a list over dictionary if you need to store the order of something.
## you can store both int and str in a single string ie it allows heterogeneous storage as well homogeneous
# a = [1,'a',1.0,[]]
# a #=> [1, 'a', 1.0, []]

## Do python lists store values or pointers?
# Python lists don’t store values themselves. They store pointers to values stored elsewhere in memory.
# This allows lists to be mutable.

# --------------------- declare a list ---------------------
# 1.
l = list()
# 2.
l1 = [1, 2, 3]
print(l1)
# 3. list comprehension
l2 = [i**2 for i in l1]
print(l2)

# --------------------- insert into the list ---------------------
# the element previously at the specified index is shifted to the right, not overwritten.
l1.insert(4, 100) # insert( position, element to be inserted)
print(l1)

# append : adds one element at the end of list
l1.append(6)
print(l1)
# extend : adds multiple element at the end of the list
l2.extend([11, 12, 13])
print(l2)

# --------------------- slicing in list ---------------------
print(l1[1:3])
print(max(l1))
print(min(l1))
print(sum(l1))

# --------------------- delete from a list ---------------------
l = ['h','i','h','o','w','r','u']
print(l)
# del removes an item from a list given its index.
del l[1]
print('del->', l)
# pop() removes an object by its index and return the popped item and allows using list like a stack.
print('pop->', l.pop(3))
# .remove() removes the first instance of a matching object.
l.remove('h')
print('remove->', l)
# Remove all elements from a list
l.clear()
#del l[:]
print(l)
# --------------------- Faltten a 2D list into 1d using list comprehension ---------------------
l_2d = [[1,2,3,4],[1,24,5,6]]
l_1d = [ val for i in l_2d for val in i]
print(l_1d)
# --------------------- sort ---------------------
# You cannot sort a list with None in it because comparison operators(used by sort()) can’t compare an integer with None
# sort() and reverse() returns none
print(l1)
l1.sort()
print(l1)
# sort oin reverse order
l1.sort(reverse=True)
l1.reverse()
print(l1[::-1])
print(l1)
# reversed() and sorted() returns an iterable of the list in reverse order.
print(sorted([1,2,3,3,6657,98978]))
print(reversed([11,2,3,6567,865]))
# ---------------------list with interpolation---------------------
for i in l1:
    print("the elements in l1 are: {}".format(i))
for i in l2:
    print(f"the elements in the list are {i}")

# --------------------- list to string conversion---------------------
x = ''
for i in l1:
    x += ''.join(str(i))
print(x)

# --------------------- string to list ---------------------
st = "hi there"
t1 = list(st)
print(t1)

# --------------------- count the occurrence ---------------------
from collections import Counter
myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print(Counter(myList))

# using map , lambda and dictionary
x = [ c for c in map(lambda val:{val,myList.count(val)},myList)]
print(x)

# --------------------- loop running through two list---------------------
# A zip object is an iterator of tuples.

name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
age = [1, 2, 2, 6]
z = zip(name, animal, age) # z=> <zip at 0x111081e48>
for name, animal, age in zip(name,animal,age):
    print("%s the %s is %s" % (name, animal, age)) # => Snowball the Cat is 1

# Combine 2 lists into a list of tuples with the zip function
alphabet = ['a', 'b', 'c']
integers = [1, 2, 3]
print(list(zip(alphabet, integers)))

# ------------------ Iterate over both the values in a list and their indices ---
grocery_list = ['flour','cheese','carrots']
for i,val in enumerate(grocery_list):
    print(f"time number {i} is {val}")

# --------------------  Remove duplicates from a list ---------------------------

li = [3, 2, 2, 1, 1, 1]
print(list(set(li)))#=> [1, 2, 3]

# --------------------- Find the index of the 1st matching element -> index() ---

fruit = ['pear', 'orange', 'apple', 'grapefruit', 'apple', 'pear']
print(fruit.index('apple')) #=> 2
print(fruit.index('pear')) #=> 0

# --------------------- Count the occurrence of a specific object in a list ----
pets = ['dog','cat','fish','fish','cat']
pets.count('fish') #=> 2

print(len(pets))

# --------------------- map ----------------------------------------------------
# map() allows iterating over a sequence and updating each value with another function

l = list(range(5))
def multiply_by_5(val):
    return val*5

v = [c for c in map(multiply_by_5, l)]
print(v)
# -------------------lambda and map--------------------------------------

v_lambda = [ c for c in map(lambda val:val*5,l)]
print(v_lambda)

# ------------------- reduce ---------------------------------------------------
# reduce iterates over a sequence and calls the function on every element

from functools import reduce
def subtract(a,b):
    return a - b
numbers = [100,10,5,1,2,7,5]
print(reduce(subtract, numbers)) #=> 70
# -------------------- filter ---------------------------------------------------------------------
# filter() will remove any elements from a sequence on which the function does not return True.

def remove_negative(val):
    return True if val>0 else False
neg_l = [1,-3,6,-90,-36,43]
print([ c for c in filter(remove_negative,neg_l)])
# -------------------- filter and lambda ------------------------------------------------------------
neg_filter = [ c for c in filter(lambda val:val>0,neg_l)]
print(neg_filter)
# -------------------- list to dictionary ------------------------------------------------------
l_d = [1,2,3,34,4,5]
dic_from_list = {i:1 for i in l_d}
print(dic_from_list)
# ------------------- What’s the affect of multiplying a list by an integer ---------------------

l_mul = ['1','2']
print(l_mul*3)

# ------------------ Use a list as a stack ------------------------------------------------------
# You can use append() and pop() to treat a list like a stack. Stacks function per LIFO (last in first out)
# benefit of a stack is that elements can be added and removed in O(1) time
# because the list does not need to be iterated over.

stack = []
stack.append('Jess')
stack.append('Todd')
stack.append('Yuan')
print(stack) #=> ['Jess', 'Todd', 'Yuan']
print(stack.pop()) #=> Yuan
print(stack) #=> ['Jess', 'Todd']
# ------------------  Find the intersection of 2 lists ------------------------------------------------------
a = [1,2,3]
b = [4,2,6]
print(set(a)&set(b))
# ------------------  Find the difference between a set and another set ----------------------------------------
# We can’t subtract lists, but we can subtract sets.
li1 = [1,2,3]
li2 = [2,3,4]
set(li1) - set(li2) #=> {1}
set(li2) - set(li1) #=> {4}

# ---------------- shallow copy and deep copy in lists --------------------------------------------------------
# .copy() can be used to shallow copy a list
# modifying round2 will modify round1 if we don’t create a shallow copy. ie if it was for round1=round2

# Creating a shallow copy does create a new object in memory,
# copy() create reference to original object. If you change copied object - you change the original object.

# Creating a deep copy creates copies of the original objects and points to these new versions.
# Changing new deep copied object doesn't affect original object

from copy import deepcopy
round1 = ['chuck norris', 'bruce lee', 'sonny chiba']
round2 = round1.copy()
round2.remove('sonny chiba')
# round2 = deepcopy(round1)
# round2.remove('sonny chiba')
print(round1) #=> ['chuck norris', 'bruce lee', 'sonny chiba']
print(round2) #=> ['chuck norris', 'bruce lee']
