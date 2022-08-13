# does not contain any duplicates
# {} or set()
# {} -> creates an empty dictionary hence use {'something here'}
# a set is a subset of itself ie a.issubset(a) => true

s1 = {1, 2, 3}
s2 = {8, 9}
# ----------------------------------------insertion in sets----------------------------------------
s1.add(4)
print(s1)
# ----------------------------------------updating the set----------------------------------------
s1.update([5, 6, 7])
print(s1)
# ----------------------------------------deleting from set----------------------------------------
s1.remove(7)
s1.discard(9)
print(s1)
# ----------------------------------------common set operations----------------------------------------
# union
s1.union(s2) # Values which exist in s1 or s2
print(s1 | s2)
# intersection
s1.intersection(s2) # Values which exist in s1 and s2
print(s1 & s2)
# difference btw two sets
s1.difference(s2) # Values which exist in s1 but not in s2
print(s1 - s2)
# symmetric difference
print(s1 ^ s2)
# The union() and intersection() functions are symmetric methods:
s1.union(s2) == s2.union(s1) #=> True
s1.intersection(s2) == s2.intersection(s1) #=> True
s1.difference(s2) == s2.difference(s1) #=> False
# Update the set by adding elements from an iterable/another set.
s1.update() #or |=
# Update the set by keeping only the elements found in it and an iterable/another set.
s2.intersection_update() #or &=
# Update the set by removing elements found in an iterable/another set.
s2.difference_update() #or -=
# Update the set by only keeping the elements found in either set, but not in both.
# s2.symmetric_difference_update() #or ^=
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = int(input())
s = set(map(int,input().split()))
inp1 = int(input())
for _ in range(inp1):
    operation, number = input().split()
    s2 = set(map(int,input().split()))
    if operation == 'intersection_update':
        s.intersection_update(s2)
    elif operation == 'update':
        s.update(s2)
    elif operation == 'symmetric_difference_update':
        s.symmetric_difference_update(s2)
    elif operation == 'difference_update':
        s.difference_update(s2)
print(sum(s))
'''
superset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 23, 45, 84, 78}
s = {1, 2, 3, 4, 5}
s1 = {100 ,11 ,12 }

print(superset-s)
print("len(s):", len(s))
print("len(superset):", len(superset))
print("len(superset-s):", len(superset-s))
print("-----"*3)
print(superset-s1)
print("len(s):", len(s1))
print("len(superset):", len(superset))
print("len(superset-s):", len(superset-s1))

#  to check if a set is a subset of another set
s1 = set(range(5))
s2 = set(range(8))
print(s1<s2)
print(s1.issubset(s2))

# frozenset () -> when we do not want to change the content of a set we use frozen set
l = [12,2,2,3,4,5,6,7,7,8,9]
fs = frozenset(l)
print(fs)

# fs.add(1) -> it wont allow
