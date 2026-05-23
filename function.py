# '''def add(a,b):
#     return a+b
# print(add(4,5))'''

# '''def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))'''

# def square(*nums):
#     l1=[]
#     for i in nums:
#         l1.append(i*i)
#     print(l1)
#     l1.clear()

# print(square(2,3,4,5,6))
# print(square(5,6,4,3))


#TO FIND GREATEST OF THREE NUMBERS

def greatest():
        a=int(input("Enter number 1:"))
        b=int(input("Enter number 2:"))
        c=int(input("Enter number 3:"))
        
        if(b<a>c):
            print(a,"is greater")
        if(a<b>c):
            print(b,"is greater")
        if(a<c>b):
             print(c,"is greater")

greatest()