# n = 153
# n1 = n
# arm = 0
# while n != 0:
#     arm = arm + (n%10)**3
#     n = n // 10
# if n1 == arm:
#     print(n1, "is arm no") 
# else:
#     print(n1, "not a arm no")

# n = 153
# n1 = n
# p = len(str(n))
# arm = 0
# for i in range(0,p,1):
#     arm = arm + (n%10)**p
#     n = n // 10
# if n1 == arm:
#     print(n1, "is an armstrong no")
# else:
#     print(n1, "is not an armstrong no")

# a = "onkar sawant"
# for i in a:
#     print(i)

# for i in range(0,len(a),1):
#     print(a[i])

# a = input("name: ")
# b = input("age: ")
# c = input("city: ")

# print("my name is ",a)
# print("my age is ",b)
# print("my city is ",c)

# a = "ABCDEF"
# i = 0
# while i < len(a):
#     sp = 5
#     while sp > i:
#         print(" ", end=" ")
#         sp = sp - 1
#     s = 0
#     while s <= i:
#         print(a[i], end=" ")
#         s = s + 1
#     print()
#     i = i + 1

# a = "A"
# b = "B"
# r = 1
# while r <= 5:
#     c = 1
#     while c <= 5:
#         if r == 1:
#             print(a, end=" ")
#         elif c == 1:
#             print(b, end=" ")
#         c = c + 1
#     print()
#     r = r + 1

# a = "A"
# b = "B"
# m = "C"
# r = 1
# while r <= 5:
#     c = 1
#     while c <= 5:
#         if r == 1 and c == 1:
#             print(m, end=" ")
#         if r == 1:
#             print(a, end=" ")       
#         elif c == 1:
#             print(b, end=" ")
#         c = c + 1
#     print()
#     r = r + 1

# a = "my name is khan"
# i = -1
# l = -(len(a))
# while i >= l:
#     print(a[i], end=" ")
#     i = i - 1

# a = "my name is khan"
# i = 14
# s = ""
# while i >= 0:
#     s = s + a[i]
#     i = i - 1
# print(s)

# a = "my name is khan"
# data = "aeiou"
# v = 0
# sp = 0
# tletters = 0
# i = 0
# while i < len(a):
#     if a[i].lower() in data:
#         v = v + 1
#     elif a[i] != data and a[i] != " ":
#         tletters = tletters + 1
#     else:
#         sp = sp + 1
#     i = i + 1
# print("total no of vowels =", v)
# print("total no of spaces =", sp)
# print("total no of letters =", tletters)

# a = ["onkar","raj","max","tony"]
# i = 0 
# while i < len(a):
#     print(a[i])
#     i = i +1 

# for i in range(len(a)):
#     print(a[i])

# a = [2,45,6,1,39,7,5,4,6,8,8]
# i = 0
# while i < len(a):
#     if a[i]%2 == 0:
#         print(a[i])
#     i = i + 1

# a = [2,45,6,1,39,7,5,4,6,8,8]
# i = 0
# while i < len(a):
#     m = i + 1
#     while m < len(a):
#         if a[i] == a[m]:
#             print(a[i],end=" ")  
#         m = m + 1
#     i = i + 1

# find max and min no in list 

# a = [89,22,3,4449,5]
# max = a[0]
# i = 0
# while i < len(a):
#     if a[i] > max:
#         max = a[i]
#     i = i + 1 
# print(max)

# a = [89,22,3,4449,5,0.5]
# min = a[0]
# i = 0
# while i < len(a):
#     if a[i] < min:
#         min = a[i]
#     i = i + 1 
# print(min)

# find second highest no 

# a = [7,2,3,7,78]
# i = 0 
# max = a[i]
# min = a[i]
# while i < len(a):
#     if a[i] > max:
#         max = a[i]
#     elif a[i] < min:
#         min = a[i]
#     i = i + 1

# j = 0
# n = a[j]
# smax = 0
# while j < len(a):
#     if max > a[j] > min:
#         smax = a[j]
#     j = j + 1

# print(max)
# print(min)
# print(smax)

# print
# * * * * * 
#   * 
#     *
#       *
#         *

# r = 1
# while r <= 5:
#     c = 1
#     while c <= 5:
#         if r == 1:
#             print("*", end=" ")
#         elif (r == 2 and c == 2) or (r == 3 and c == 3) or (r == 4 and c == 4) or (r == 5 and c == 5):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#         c = c + 1
#     print()
#     r = r + 1

# print
#   b
# a   a
# a b a
# a   a

# r = 1 
# while r <= 4:
#     c = 1
#     while c <=3:
#         if (r == 1 and c == 2) or (r == 3 and c == 2):
#             print("b", end=" ")
#         elif ((r == 2 or r == 3 or r == 4) and c == 1) or ((r == 2 or r == 3 or r == 4) and c == 3):
#             print("a", end=" ")
#         else:
#             print(" ", end=" ")
#         c = c + 1
#     print()
#     r = r + 1 

# a = ['rahul','sai', 'max','tony','onkar','kiran']
# b = []
# for i in a: 
#     if "k" in i:
#         b.append(i)
# print(b)

# a = [1,2,3,4,5]
# def mult(val):
#     i = 0
#     m = 1
#     while i < len(val):
#         m = m * a[i]
#         i = i + 1
#     return m 
# print(mult(a))

# a = (1,2,3,44)
# b = list(a)
# i = 0
# while i < len(b):
#     if i == 1:
#         b[i] = 22
#     elif i == 2:
#         b[i] = 33
#     elif i == 3:
#         b[i] = 44
#     i = i + 1
# print(tuple(b))

# a = [15,2,4,56,9,88,35,46,1]
# b = []
# c = []
# for i in a:
#     if i % 2 == 0:
#         b.append(i)
#     else:
#         c.append(i)
# print("even no list is",b)
# print("odd no list is",c)

# a = ["onkar","tony","max","heath","rajesh"]
# b = []
# for i in a:
#     if len(i) >= 5:
#         b.append(i)
# print(b)

# a = "abcxyz"
# b = ''
# i = -1
# while i >= -len(a):
#     b = a[i]
#     print(b, end="")
#     i = i - 1

# d = ['name','age','city']
# d1 = ['rohit','30','thane']
# dic = {}
# for i in range(len(d)):
#     dic[d[i]] = d1[i]
# print(dic)

# dic["indian"]= True
# print(dic)

# a = [i for i in range(1,11,1)]
# print(a)

# a = [i for i in range(1,101,1) if i % 2 == 0]
# print(a)

# import random
# words = ['rahul','lahur','sawant','wasant']
# score = 0
# while True:
#     letters = list(random.choice(words))
#     print('guess the correct word:', "".join(letters))
#     user_word = input("write a correct word or press 'q' to quit : ")
#     if user_word == 'q':
#         break
#     valid = True
#     for i in user_word:
#         if i in letters:
#             letters.remove(i)
#         else:
#             valid = False
#             break
#     if valid and user_word in words:
#         score = score + len(user_word)
#         print(f"your score is : {score}")
#     else:
#         print("wrong word")

# import random
# words = ['rahul','lahur','sawant','wasant']
# score = 0
# while True:
#     letters = list(random.choice(words))
#     l = "".join(letters)
#     print('guess the correct word:', "".join(letters))
#     user_word = input("write a correct word or press 'q' to quit : ").lower()
#     if user_word == 'q':
#         break
#     if user_word != l:
#         valid = True
#         for i in user_word:
#             if i in letters:
#                 letters.remove(i)
#             else:
#                 valid = False
#                 break
#         if valid and user_word in words:
#             score = score + len(user_word)
#             print(f"your score is : {score}")
#         else:
#             print("wrong word")
#     else: 
#         print("------You enter same word that I provided------")
# print(f"Total score = {score}")

# def upper(x):
#     t = ""
#     for i in x:
#         if i != " ":
#             a = ord(i)
#             if a >=97:
#                 a = ord(i)-32
#                 a1 = chr(a)
#                 t = t + a1
#             elif a < 65:
#                 a1 = chr(a)
#                 t = t + a1
#             else:
#                 a1 = chr(a)
#                 t = t + a1
#         elif i == " ":
#             t = t + " "
#     return t
# print(upper("Onkar iS my name and how are you?"))

# def lower(x):
#     t = " "
#     for i in x:
#         if i != " ":
#             a = ord(i)
#             if a < 65:
#                 t = t + i
#             elif a >= 65 and a <= 90:
#                 a = a + 32
#                 a1 = chr(a)
#                 t = t + a1
#             else:
#                 a1 = chr(a)
#                 t = t + a1
#     return t 
            
# print(lower("oNkaR?--..m"))

# def prime(n):
#     i = 2
#     while i < n:
#         r = n % i
#         if r == 0:
#             p = "not prime"
#             break
#         else:
#             p = 'prime'
#         i = i + 1
#     return p
# print(prime(67))

def p(n, i=1):
    print(n)
    if i < n:
        p(n, i + 1)

p(5)
