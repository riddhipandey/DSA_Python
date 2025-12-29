# Q1. Write a program that takes string as input. Using conditional statements, calculate the Final tax rate based on these rules:
#If salary<30,000→5% •If salary is 30,000–70,000 →15% • If salary >70,000→25%
salary = int(input("Enter your salary : "))
if salary < 30_000 : 
    print(f"Your tax rate is = {salary*0.05}")
elif salary >= 30_000 and salary <= 70_000 : 
    print(f"Your tax rate is = {salary*0.15}")
else : 
    print(f"Your tax rate is = {salary*0.25}")

#Q2 Write a function that takes two integers a and b and prints all even numbers between them(inclusive)
def print_even_numbers(a, b):
    if(a%2==0):
        print(f"{a},")
        a = a+2
    else:
        a = a+1 
    while(a<=b):
        print(f"{a},")
        a = a + 2

a = int(input("Enter value for a and b : "))
b = int(input())
print_even_numbers(a,b)

# Q3 Write a function that prints digits of a number n, digits n = 312 For eg:,there are 3digits in it 3,1 and 2 & we need to print them.
def print_digits(n):
    while(n>0):
        digit = n%10
        print(f"{digit} ,", end="")
        n = int(n/10)

n = int(input("Enter a number : "))
print_digits(n)

#Q4 Write a function to return the count the number of digits in a number, n.
def count_digits(n):
    count = 0
    while(n>0):
        digit = n%10
        n = int(n/10)
        count += 1

    return count

n = int(input("Enter a number : "))
print(count_digits(n))

#Q5 Write a function to return the sum of digits of a number n.
def sum_of_digits(n):
    sum = 0
    while(n>0):
        digit = n%10
        n = n/10
        sum = sum + digit

    return int(sum)

n = int(input("Enter a number : "))
print(sum_of_digits(n))

#Q6 Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.
for number in range(16):
    if(number % 3 == 0 and number % 5 == 0):
        print(f"{number},", end="")

#Q7  Design a program to continuously input a number n from user & print if it is positive or negative until the user enters “Quit".
while True:
    a = input("Enter a number (or Quit): ")

    if a == "Quit":
        break

    n = int(a)

    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

a = input("Enter a number (or Quit): ")
while a != "Quit":
    if is_int(a):
        n = int(a)
        print("Positive" if n > 0 else "Negative" if n < 0 else "Zero")
    else:
        print("Please enter a valid number!")
    a = input("Enter a number (or Quit): ")

#Q8 Letʼs create a Simple Calculator that performs arithmetic operations.Create a function that performs addition,subtraction,multiplication,ordivision based on the operation parameter.
#Operation parameter can have values '+', '-', '*', '/'

def calculator(a,b,operation):
    if(operation == '+'):
        return a+b
    elif(operation == '-'):
        return a-b
    elif(operation == '*'):
        return a*b
    elif(operation == '/'):
        return a/b
    else:
        print("Invalid operator")

a = int(input("Enter first number"))
b = int(input("Enter 2nd number"))
operation = input("Enter operator")
print(calculator(a,b,operation))

#Q9 Write a function is_prime(n) that returns True if n is a prime number and False otherwise, using a loop.
def is_prime(n):
    if n == 1 or n==2 :
       return True 

    for num in range(2, n, 1):
        if(n%num == 0):
            return False
        
    return True


n = int(input("Enter a number "))
print(is_prime(n))

#Q10 Letʼs create a “Number Guessing Game”. Given a secret number(already decided by you), write a program that asks the user to guess it and prints:
print("Guess the number")
while True:
    a = input("Enter a number (or Quit): ")

    if a == "Quit":
        break

    n = int(a)

    if n > 100:
        print("Too High")
    elif n < 100:
        print("Too Low")
    else:
        print("Correct Ans:")
        break