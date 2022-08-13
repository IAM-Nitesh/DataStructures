#Method #1:
#Iterate through the list and keep adding the element for every index in some empty string.

# def listToString(l):
#     temp = ""
#
#     for i in l:
#         temp+=i
#     return temp
#
# print(listToString(['An', 'Apple', 'a', 'day', 'keeps', 'the', 'doc', 'away']))

#Method #2: Using .join() method

# def listToString(l):
#     temp = " "
#     return (temp.join(l))
#
l = ['An', 'Apple', 'a', 'day', 'keeps', 'the', 'doc', 'away']
# print(listToString(l))

#Method #3: Using list comprehension
def list_To_String(l):
    temp = " ".join(str(i) for i in l)
    return temp

print(list_To_String(['An', 'Apple', 'a', 'day', 'keeps', 'the', 'doc', 'away']))

#Method #4: Using map()
#Use map() method for mapping str (for converting elements in list to string) with given iterator, the list.


# using list comprehension
listToStr = " ".join(map(str, l))
print(listToStr)