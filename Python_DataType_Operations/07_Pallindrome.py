print("-"*100)
print(" Single word Pallindrome :")
print("-"*100)

def isPallindrome(s):
    if len(s) <= 1:
        return True
    if s[0].lower() == s[len(s)-1].lower():
        return isPallindrome(s[1:len(s) -1])
    else:
        return False

inp_var = ["AnnA","Solos"]
#inp_var =

for i in inp_var:
    res = isPallindrome(i)
    if res == 1:
        print(f"the given string {i} is pallindrome")
    else:
        print(f"the given string {i} is not pallindrome")

print("-"*100)
print(" number Pallindrome :")
print("-"*100)

num = input ("Enter the number to be checked for Pallindrome :")
try :
    val = int(num)
    if num == str(num)[::-1]:
        print(f"the given number {num} is a pallindrome")
    else:
        print(f"the given number {num} is not a pallindrome")
except ValueError:
    print("!!! A valid number input is not entered !!!")


