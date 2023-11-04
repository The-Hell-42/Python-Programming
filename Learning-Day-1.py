# Day1
# Date: 9/28/2023
# course : 100Days of Python challenge
# completion : Day 15
# There is need of practise which I will do on Date:10/01/2023

print("Hello World")
print(7*15)

a1 = 12345
print(a1)
harry = 4269
print(harry)
b2 = "Anurag"
print(b2)

# Exercise-1
# Create a calculator


a = int(input("Enter the First Number :"))
o = input("Enther the operator :")
b = int(input("Enter the Second Number :"))
if o == "+":
  ans1 = a + b
  print("Addition of",a,"and",b,"is:", ans1)
elif o == "-":
  ans2 = a - b
  print("Subtraction of",a,"and",b,"is:", ans2)
elif o == "*":
  ans3 = a * b
  print("Multiplication of",a,"and",b,"is:", ans3)
elif o == "/":
  if b != 0:
        ans4 = a / b
        print("Division of", a, "by", b, "is:", ans4)
  else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please enter +, -, *, or /.")
print("Thanks for using the calculator!")
