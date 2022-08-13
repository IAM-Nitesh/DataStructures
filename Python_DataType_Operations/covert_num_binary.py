import math

# def convert_binary_to_base_ten(num: str):
#     temp = num[::-1]
#     num_return = 0
#     for i in range(len(temp)):
#         if int(temp[i]) in [0,1]:
#             num_return += math.pow(2,i)*int(temp[i])
#             #print(pow(2,i),int(temp[i]))
#     return num_return
#
# print(convert_binary_to_base_ten(("110")))

def convert_base_ten_to_binary(num: int):
    binary_return = []
    ans = []
    power_of_two = [pow(2,i) for i in range(num)]
    while num!=1:
        div = [i for i in power_of_two if num>i]
        ans.append(max(div))
        num = num - max(div)
    return ans

print(convert_base_ten_to_binary((20)))