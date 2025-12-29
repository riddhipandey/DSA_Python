print("Practice Python language")

day = 2

if day == 1:
    print(f"This is my day {day} of practice")
else:
    print("Resting today!!!")


# Q1. Write a program that asks the user for their name and age,then prints a sentence like:
name = input("Enter your name ")
age = input("Enter your age ")
print(f"Hello {name}! You are {age} years old.")

# Q2 Take two numbers as input from the user and print their sum,difference,product,and quotient.
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print(f"Sum of {a} and {b} is = {a+b}")
print(f"difference of {a} and {b} is = {a-b}")
print(f"Product of {a} and {b} is = {a*b}")
print(f"Quotient of {a} and {b} is = {int(a/b)}")

#Q3 Ask the user to enter two integers and one float. Convert them all to floats and print their average.
a = int(input("Enter first interger "))
b = int(input("Enter 2nd Integer "))
c = float(input("Enter 3rd value as float "))
print(f"Average of {a}, {b} and {c} is = {(a+b+c) /3}")

#Q4 The user enters a string containing a number(e.g. "45",).Convert it to: an integer •a float• a string again Print all three values with their types
a = input("Enter a value " )
a_int = int(a)
a_float = float(a_int)
a_str = str(a_float)
print(f"{a} integer value is {a_int} and its tye is {type(a_int)}")
print(f"{a} float value is {a_float} and its tye is {type(a_float)}")
print(f"{a} string value is {a_str} and its tye is {type(a_str)}")

# Q5 Evaluate and print the result of the following expression:
x = 10+3*2**2
print(x)

# Q6 Write a program to SWAP values of two numbers entered by the user
a = int(input("Enter first value "))
b = int(input("Enter second value "))
a,b = b,a
# a = a^b
# b = a^b
# a = a^b
print(f"Swaped values of a and b are {a} , {b}")

#Q7 Ask the user for a temperature in Celsius(string input). Convert it to float,then calculate and print temperature in Fahrenheit.
# Conversion formula:Fahrenheit Temp = (CelsiusTemp∗(9/5))+32
temp_c = float(input("Enter temperature in Celsius "))
temp_f = (temp_c*9/5)+32
print(f"Fahrenheit Temp = {temp_f}")

#Q8 Take the radius(r)as user input and print the area. Use the formula :π*rpow2 (valueofπ=3.14)
r = float(input("Enter radius of the circle : "))
print(f"Area of cirecle with radius {r} = {3.14*r**2}")

#Q9 Ask the user for:Principal(P),Rate(R),Time(T). Convert all to float and compute simple interest SI=(P∗R∗T)/100
p = float(input("Enter principle amount : "))
r = float(input("Enter Rate : "))
t = float(input("Enter Time in year : "))
print(f"Simple interest for Principle {p}, Rate {r} and Time {t} is = {(p*r*t)/100}")

#Q10 Take a decimal number as input(like 45.78) and output its: integerpart-45 • fractional part .78
a = float(input("Enter a decimal value "))
float_part = round(a - int(a), 2)
print(f"{a}'s integer part is {int(a)} and float part if {a%int(a)}")
print(f"{a}'s integer part is {int(a)} and float part if {float_part}")