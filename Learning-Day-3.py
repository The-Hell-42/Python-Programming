# Day-20
# Date: 10/05/2023
# Completion: Day-23
# Function

# def name(*name):
#     print("Hello,",name[0],name[1],name[2])
#
# print(name("anurag","manish","Bipin"))
#
# def str(*number):
#     for i in str:
#         return i
#
# print(str(10))

# # Default argument
# def name(mname, fname, lname):
#     print("Hello!",fname,mname,lname)
#
# name(mname="Prasad",fname="ANurag",lname="Sah")
#
# def name(*name):
#     print("Hello ",name[0],name[1],name[2])
# name("Anurag","MAnish","Bipin")
#
# def name(**name):
#     print("Hello ",name["fname"],name["lname"])
# name(fname="Anurag",lname="Sah")

# Return Statement
# def sumA(a, b):
#     return (a + b)
# a = int(input("Enter the number : "))
# b = int(input("Enter the number : "))
# print("The sum is : ", sumA(a,b))

# Python List
# lst1 = [1,2,3,4,5,6,7,8,9]
# print(lst1)
# for i in lst1:
#     print(lst1[i:7:2])
# newList = [item for item in lst1 if (item % 2 == 0) in lst1]
# print(newList)
# lst2=[10,11,12,13,14,15]
# lst2.sort(reverse = True)
# print(lst2)


lst1 = [1,3,5,7,9]
lst2 = [2,4,6,8,10]
lst = (lst1 + lst2)
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)