# when to use :
#
# Strings : immutable, allow duplicates, ordered
#

# List : mutable, allow duplicates, ordered , homogeneous
# - Use a list if you need to store the order of something.
#
# Tuple : immutable , allow duplicates , heterogeneous
# - faster reads and iteration and uses lesser space as compared to a list
#
# Set : mutable, no duplicates, unordered.
# it is an unordered collection of unique elements
# use them to make use of intersection,unions,difference and weather a subset of not
#
# Dictionary : mutable, unordered , no duplicates keys
# - use a dictionary because lookups are faster
# - dictionary does not allow duplicate keys.
# - Use a dictionary if you want to count occurrences of something.

from sys import getsizeof
l = [1,2]
print(type(l))
print(getsizeof(l)) # list => 72

t = (1,2)
print(type(t))
print(getsizeof(t)) # tuple => 56

s = {1,2}
print(type(s))
print(getsizeof(s)) # set => 216

d = {1:2}
print(type(d))
print(getsizeof(d)) # dictionary => 232