# Strings are immutable
# ie we cannot modify  strings
# s = 'hi'
# s[1] = 'o' #-> it will through a TypeError error
#  Does defining a string twice (associated with 2 different variable names) create one or two objects in memory?
# It only creates one, this helps python save memory when dealing with large strings.
# animal = 'dog' and pet = 'dog'. print(id(animal))=> 4441985688 and print(id(pet))=> 4441985688
# The * is the splat operator, which just means to unpack the elements in an iterable (e.g. map or list).
# '' and " " : both can be used to declare string .
# multiline strings : ''' ''' , how it works internally is it stores a string with hi\nhow are you\nok,bye
# no implicit conversions are available with python <str> + <int> with result in TypeError

# to print ascii value                                                          - ord()
print(ord("a"))
# to print char value out of ascii                                              - chr()
print(chr(65))
# convert to string                                                             - str()
print(str(5))
# print len of a string                                                         - .len()
print(len('hello'))
# partition() splits a string on the first instance of a substring.             - partition()
# A tuple of the split string is returned without the substring removed.
sentence = "If you want to be a ninja"
print(sentence.partition(' want '))#=>('If you', ' want ', 'to be a ninja')
# print min and max of a string                                                 - max(), min()
print(min('1091280345y894379'))
print(max('amsdabkbfdwa'))
#  Check if a string begins with or ends with a specific character              - startswith() , endswith()
city = 'New York'
print(city.startswith('New')) #=> True
print(city.endswith('N')) #=> False
# print the number of a specific character      - count() will return the number of occurrences of a specific character.
print('The first president of the organization..'.count('o'))
# Replace all instances of a substring in a string - .replace()
s = 'hi there'
print(s.replace(" ", "-"))
sentence = 'Sally sells sea shells by the sea shore'
print(sentence.replace('sea', 'mountain'))
#  Reverse the string “hello world”
print(''.join(reversed("hello world")))
print('hello world'[::-1])
# Encode a given string as ASCII
# encode() encodes a string with a given encoding.
# The default is utf-8. If a character cannot be encoded then a UnicodeEncodeError is thrown.
print('Fresh Tuna'.encode('ascii'))#=>b'Fresh Tuna'
# What is the effect of multiplying a string by 3
print('dog' * 3)#'dogdogdog'
# Concatenate two strings
print('string one' + ' ' + 'string two') #=> 'string one string two'

# ------ index --------------
# Find All Indexes of a Character Inside a String With List Comprehensions in Python
string = "This is a string"
char = "i"
indices = [i for i, c in enumerate(string) if c == char]
print(indices)

# to find the second occurrence of a word in a string
s = "today is beautiful and today is everything"
ind = s.find('is') + len('is')
print(ind)
print(s.index('is', ind, len(s)))

# ------ substring --------------
# Search a specific part of a string for a substring
# index() can also be provided with optional start and end indices for searching within a larger string.
print('the happiest person in the whole wide world.'.index('the',10,44))#=> 23
print('the happiest person in the whole wide world.'.index('the'))#=> 0

# Split a string on a specific character
print('not--so--great'.split('--')) #=> ['not', 'so', 'great']

# Check if a string contains a specific substring :
# The in operator will return True if a string contains a substring.
print( 'plane' in 'The worlds fastest plane' ) #=> True
print( 'car' in 'The worlds fastest plane' ) #=> False

# Find the index of the first occurrence of a substring in a string
# There are 2 different functions that will return the starting index, find() and index().
# They have slightly different behaviour.
# find() returns -1 if the substring is not found.
# index() will throw a ValueError.
print('The worlds fastest plane'.find('plane')) #=> 19
print('The worlds fastest plane'.find('car')) #=> -1
print('The worlds fastest plane'.index('plane')) #=> 19
# print('The worlds fastest plane'.index('car')) #=> ValueError: substring not found

#  When would you use splitlines()
sentence = "It was a stormy night\nThe house creeked\nThe wind blew."
print(sentence.splitlines()) #=>['It was a stormy night', 'The house creeked', 'The wind blew.']

# ------ convert/ check capital --------------

# to convert lower to upper and upper to lower in a string we use swap case
# print(''.join([i.lower() if i.isupper() else i.upper() for i in input()]))
# a = "AbcFjbhbU"
# print(a.swapcase())
# print(*map(lambda ch: ch.lower() if ch.isupper() else ch.upper(), input()), sep="")

# to check if each word in a string begins with a capital letter we use istitle()
print('The Hilton'.istitle())
# Capitalize the first character of each word in a string
print('once upon a time'.title())
# Capitalize the first character of a string
'florida dolphins'.capitalize() #=> 'Florida dolphins'

# Check if a string is composed of all lower case characters
print('all lower case'.islower()) #=> True
print('not aLL lowercase'.islower()) # False
print('aPPLE'[0].islower()) #=> True

# Check if a string contains only numbers  - isnumeric() returns True if all characters are numeric.
print('80000'.isnumeric())#=> True)
print('1.0'.isnumeric())#=> False)

# Check if all characters in a string conform to ASCII
print( 'Â'.isascii() )#=> False
print( 'A'.isascii() )#=> True

# Uppercase or lowercase an entire string
sentence = 'The Cat in the Hat'
sentence.upper() #=> 'THE CAT IN THE HAT'
sentence.lower() #=> 'the cat in the hat'

# Uppercase first and last character of a string
animal = 'fish'
animal[0].upper() + animal[1:-1] + animal[-1].upper()#=> 'FisH'

# Check if a string is all uppercase
print('Toronto'.isupper()) #=> False
print('TORONTO'.isupper()) #= True

# Check if all characters in a string are alphanumeric
print('Ten10'.isalnum()) #=> True
print('Ten10.'.isalnum()) #=> False

# -------- id associated operations ----------

# id function returns the id of the memory address associated with a python object
name = "nitesh"
print(id(name))

# How would you confirm that 2 strings have the same identity? ie they are stored at same memory address
# The is operator returns True if 2 names point to the same location in memory.
# 'is' compares the identity ( id() ) where as '=' compares equality of two strings
a = ['python', 'gopher']
b = a
print(a == b) #=> True
print(a is b) #=> True
c = ['python', 'gopher']
print(a == c) #=> True
print(a is c) #=> False

# ------ Interpolation in string ----------
#  there are 3 ways to interpolate strings
name = 'Chris'
# 1. f strings
print(f'Hello {name}')
# 2. % operator
print('Hey %s %s' % (name, name))
# 3. format
print("My name is {}".format(name))

# ----------- whitespaces -----------
string = '  string of whitespace    '
print(string.lstrip()) #=> 'string of whitespace    '
print(string.rstrip()) #=> '  string of whitespace'
print(string.strip()) #=> 'string of whitespace'

# all characters are whitespace characters - isspace() only returns True if a string is completely made of whitespace.
print(''.isspace()) #=> False
print(' '.isspace()) #=> True
print('   '.isspace()) #=> True
print(' the '.isspace()) #=> False
# we can use the above to remove whitespaces from a string
s = "      ni  t e s h   "
print(''.join([ i for i in s if not(i.isspace())]))

# ----------- maketrans() And translate()-------------
# maketrans() creates a mapping from characters to other characters.
# translate() then applies that mapping to translate a string.
# create mapping
mapping = str.maketrans("abcs", "123S")
# translate string
print("abc are the first three letters".translate(mapping))#=> '123 1re the firSt three letterS'

# ----------rfind()-----------
# rfind() is like find() but it starts searching from the right of a string and return the first matching substring.
story = 'The price is right said Bob. The price is right.'
story.rfind('is')#=> 39

# --------remove vowels from a string ----------

string = 'Hello 1 World 2'
vowels = ('a','e','i','o','u')
print(''.join([c for c in string if c not in vowels]))#=> 'Hll 1 Wrld 2'

# ------- recap --------------------------------

# capitalize()  	Converts the first character to upper case
# casefold()    	Converts string into lower case
# center()	        Returns a centered string
# count()	        Returns the number of times a specified value occurs in a string
# encode()	        Returns an encoded version of the string
# endswith()	    Returns true if the string ends with the specified value
# expandtabs()	    Sets the tab size of the string
# find()	        Searches the string for a specified value and returns the position of where it was found
# format()	        Formats specified values in a string
# format_map()	    Formats specified values in a string
# index()	        Searches the string for a specified value and returns the position of where it was found
# isalnum()	        Returns True if all characters in the string are alphanumeric
# isalpha()	        Returns True if all characters in the string are in the alphabet
# isascii()	        Returns True if all characters in the string are ascii characters
# isdecimal()	    Returns True if all characters in the string are decimals
# isdigit()	        Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	        Returns True if all characters in the string are lower case
# isnumeric()	    Returns True if all characters in the string are numeric
# isprintable() 	Returns True if all characters in the string are printable
# isspace()     	Returns True if all characters in the string are whitespaces
# istitle()     	Returns True if the string follows the rules of a title
# isupper()     	Returns True if all characters in the string are upper case
# join()	        Converts the elements of an iterable into a string
# ljust()	        Returns a left justified version of the string
# lower()	        Converts a string into lower case
# lstrip()	        Returns a left trim version of the string
# maketrans()	    Returns a translation table to be used in translations
# partition()	    Returns a tuple where the string is parted into three parts
# replace()	        Returns a string where a specified value is replaced with a specified value
# rfind()	        Searches the string for a specified value and returns the last position of where it was found
# rindex()	        Searches the string for a specified value and returns the last position of where it was found
# rjust()	        Returns a right justified version of the string
# rpartition()	    Returns a tuple where the string is parted into three parts
# rsplit()	        Splits the string at the specified separator, and returns a list
# rstrip()      	Returns a right trim version of the string
# split()	        Splits the string at the specified separator, and returns a list
# splitlines()	    Splits the string at line breaks and returns a list
# startswith()  	Returns true if the string starts with the specified value
# strip()       	Returns a trimmed version of the string
# swapcase()    	Swaps cases, lower case becomes upper case and vice versa
# title()       	Converts the first character of each word to upper case
# translate()   	Returns a translated string
# upper()       	Converts a string into upper case
# zfill()       	Fills the string with a specified number of 0 values at the beginning
