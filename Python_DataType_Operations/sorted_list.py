from sys import argv

def check_sort(lst):
    lst = [argv]
    flag = True
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            flag = False
    return flag

#print(check_sort([1,2,3,4,5]))