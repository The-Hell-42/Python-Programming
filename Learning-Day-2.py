# Day-10
# Date : 10/04/2023
# completion : Day 10
# Solving example-2 from my note.

# a = input("Enter your name :")
# print("My name is ", a)
#
# x = int(input("Enter the value of x :"))
# y = int(input("Enter the value of y :"))
# print(x*y)
#
# print("The sum is ", x + y)
#

# Day-11
# String
# Example
# name = "Anurag"
# print(name)
# a = """I am a good Boy,
# I think you are to a good boy,
# how are you."""
# print(a)

# name = "Anurag"
# for n in name:
#     print(n)
#

# Example-3
name = "Anurag"
friend = "Rohan"
friend2 = "Manish"
print("Good morning sir!", name)
print(friend)
for n in friend2: #Loop through a string
    print(n)

# Day-12
# String Slicing

# Length of string
fruit = "Mango"
len1 = len(fruit)
print("Mango is a ",len1," letter word")

# String as an array
print(fruit[:3])
print(fruit[4]) #this process of using start and end index is known as slicing.

#Example-4
Fruit = "strawberry"
len2 = len(Fruit)
print(len2)

print(Fruit[1:4])
print(Fruit[:4])
print(Fruit[:5])
print(Fruit[0:-3])
print(Fruit[-1:len(Fruit)-3])
print(Fruit[-4:-1])
print("Example-4 is completed now")


# Day-13
# String Method

def str(identifier):
    strings = {
        'a': "AbcDefgehIJk",
        'b': "   Silver   Spoon  ",
        'c': "hello Programmer !!!!!",
        'd': "Welcome to the console !!!",
        'e': "aabbrrraaaakkadddabra",
        'f': "hello to everyone",
        'g': "Welcome",
        'h': "          ",
        'i': "World Health Organization",
        'j': "RAM"
    }

    return strings.get(identifier, "String not found")


# Example usage:


print(str('a').upper())
print(str('a').lower())
print(str('b').strip)
print(str('c').rstrip)
print(str('b').replace("sp", "M"))
print(str('b').split(" "))
print("Rest of the thing are on note so refer that")


#Day-14
# Conditional Statement

day = int(input("Enter the day of week :"))
if(day == 1):
    print("Today is Sunday")
elif(day == 2):
    print("Today is Monday")
elif(day == 3):
    print("Today is Tuesday")
elif(day == 4):
    print("Today is Wednesday")
elif(day == 5):
    print("Today is Thrusday")
elif(day == 6):
    print("Today is Friday")
elif(day == 7):
    print("Today is Saturday")
else:
    print("Sorry,There's only 7 days in a week")

# Day-17-18-19
# LOOP

for i in name:
    print(i)

for k in range(1,100,5):
    print(k, end=" ")
    if(k == 51):
        break
    else:
        print('Nepal')

hell = 20;
while(hell>0):
    print(hell)
    hell=hell-2
else:
    print("Calculation in  done")