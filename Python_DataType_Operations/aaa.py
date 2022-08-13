# i = int(input())
# lis = list(map(int,input().strip().split()))[:i]
# z = max(lis)
# while max(lis) == z:
#     lis.remove(max(lis))
#
# print(max(lis))

# very imp to understand
# def twoSum( nums: list[int], target: int)-> list:
#     d = {}
#     for i, n in enumerate(nums):
#         m = target - n
#         if m in d:
#             return [d[m], i]
#         else:
#             d[n] = i
# print(twoSum([3,4,-3],0))

# import itertools
#
# l = [3,2,1,5,4]
# pair = list(itertools.combinations(l,2))
# print(pair)

# from functools import reduce
# n = 123
# k = 3
# print(reduce(lambda n:n, range(k)))
# #print(reduce(lambda x,y: x+y, range(10)))
print('hi'+"\t"*2+"how are u")
