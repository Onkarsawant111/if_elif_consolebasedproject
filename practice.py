# string methods in python

# 1.concat
# a = "hello"
# b = " world"
# print(a+b)

# 2.Length of str
# a = "onkar"
# print(len(a))

# 3.Indexing
# a = "onkar"
# print(a[0])
# print(a[5])
# print(a[2])

# 4.slicing
# a = "onkar"
# print(a[1:3])
# print(a[2:])
# print(a[:2])
# print(a[-3:-1])

# String functions
# 1.endswith()
# a = "onkar"
# print(a.endswith("m"))
# 2.capitalize()
# print(a.capitalize())
# print(a.replace("onkar","GM"))
# print(a.find("t"))
# b = "apple"
# print(b.count("p"))

# practice q)
# a = input("fname: ")
# print(len(a))

# nesting if:
amount = int(input("Amount: "))
if amount%100==0:
    if amount>=500:
        notes = amount//500
        print("500 notes are ",notes)
        amount = amount%500
    if amount >= 200:
        notes = amount//200
        print("200 notes are ",notes)
        amount = amount%200
    if amount>=100:
        notes = amount//100
        print("100 notes are ",notes)
else:
    print('Please put value in multiple of 100')

