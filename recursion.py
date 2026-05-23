# # #FIBONACCI
# # def rec(n):
# #     l1=[0,1]
# #     for i in range(n):
# #         l1.append(l1[i]+l1[i+1])
# #     print(l1)

# # rec(9)

# #SUM OF N NATURAL NUMBERS

# def nsum(n):
#     l1=[0]
#     for i in range(n+1):
#         l1.append(l1[i]+i)
#     print(l1[-1])

# nsum(9)

def nsum(n):
    if n==1:
        return 1
    return nsum(n-1)+n

print(nsum(9))