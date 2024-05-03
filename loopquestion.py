# a =[1,5,9,4,66,77,81,96]
# for i in a:
#     print(i)

# a = [11,23,33,64,54]
# i = 0 
# while i < len(a)-1:
#     sum = a[i] + a[i+1]
#     print(sum)
#     i = i + 1 

# i = 0
# sum = 0
# while i < len(a):
#     sum = sum + a[i]
#     print(sum)
#     i = i + 1

# p = 1
# for i in range(1,6,1):
#     p = p * i
#     print(p)

# n = input("no: ")
# p = len(n)
# n = int(n)
# n1 = n
# arm = 0
# while n != 0:
#     arm = arm + (n%10)**p
#     n = n // 10
# if arm == n1:
#     print(n1, "is arm no")
# else:
#     print(n1,"is not arm no")

# patterns:
# r = 1
# while r <=5:
#     c = 1
#     while c <=4:
#         if c == 1 or c == 4 or r == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#         c = c + 1
#     print()
#     r = r + 1

# 2.pattern
# r = 1
# while r<=5:
#     c=1
#     while c<=5:
#         if c==1 or c==5 or c==3 or r==1 or r==5:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#         c = c+1
#     print()
#     r = r +1 

# 3.pattern
# r = 1
# while r<=4:
#     c = 1
#     while c <= r:
#         print("*", end=" ")
#         c = c + 1
#     print()
#     r = r +1
