# def isposible(x,y,a,b):
#    if(x*y == a+b):
#        return print("Yes")
#    else:
#        return print("No")
#
# val = int(input())
# arr = []
# for i in range(val):
#    v = list(map(int,input().split()))
#    arr.append(v)
#
# for i in range(len(arr)):
#    x = arr[i][0]
#    y = arr[i][1]
#    a = arr[i][2]
#    b = arr[i][3]
#    isposible(x,y,a,b)
#
# T, R, G, B = [int(s) for s in input().split(" ")]
# print(T)

# T=int(input())
# for i in range(T):
#    g,p = map(int, input().split())
#    n = int(input())
#    s = [input().split(" ") for j in range(n)]
#    a = sum(int(s[k][0]) for k in range(n))
#    b = sum(int(s[k][1]) for k in range(n))
#    print(min((a*g+b*p),(a*p+b*g)))


# T = int(input())
# result = []
# for i in range(T):
#     cost = input().split(" ")
#     print(cost)
#     n = int(input())
#     print(n)
#     l = [input().split(" ") for j in range(n)]
#     print(l)
#     x = sum(int(rows[0]) for rows in l)
#     print(x)
#     y = sum(int(rows[1]) for rows in l)
#     print(y)
#     min_cost = result.append(min((int(cost[0]) * x + int(cost[1]) * y), ((int(cost[1]) * x + int(cost[0]) * y))))
#     print(min_cost)
# for i in result:
#     print(i)


st = "aabbaaa"
s = list(st)
print(s)
for i in range(len(s)-2):
    if s[i] == s[i+1]:
        s.remove(s[i])
    else:
        continue
print(s)

n = int(input())
arr = list(map(int, input().split()))