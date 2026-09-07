#Python Type Conversion
#contoh 1.0
integer_number = 123
float_number = 1.23
new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))

#contoh 1.2
num_string = '12'
num_integer = 23
print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)
print("Data type of num_string after Type Casting:",type(num_string))
num_sum = num_integer + num_string
print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))

#=======================================================================#
#Python Basic Input and Output
#contoh 2.0
print('Good Morning!')
print('It is rainy today')

#contoh 2.1
# print with end whitespace
print('Good Morning!', end= ' ')
print('It is rainy today')

#contoh 2.2 Example: Print Python Variables and Literals
print('New Year', 2023, 'See you soon!', sep= '. ')
number = -10.6
name = "Programiz"

# print literals
print(5)

# print variables
print(number)
print(name)

#=======================================================================#
#Python Operators

#3.0 Arithmetic operators
x = 10
y = 9
print('x + y = ',x+y)
print('x - y = ',x-y)
print('x * y = ',x*y)
print('x / y = ',x/y)
print('x // y = ',x//y)
print('x ** y = ',x**y)

#3.1 Comparison operators
x = 16
y = 11
print('x > y  is',x>y)
print('x < y  is',x<y)
print('x == y is',x==y)
print('x != y is',x!=y)
print('x >= y is',x>=y)
print('x <= y is',x<=y)

#3.2 Logical operators
x = True
y = False
print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)

#3.3 Identity operators
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)

#3.4 Membership operators
x = 'Hello world'
y = {1:'a',2:'b'}
print('H' in x)
print('hello' not in x)
print(1 in y)
print('a' in y)

#=======================================================================#
#Python if...else Statement
#4.0 Python if Statement
age = int(input("Enter your age: "))
# Check if age is 18 or more
if age >= 18:
    print("Grant access to the website.")
print("Program complete.")

#4.1 Python if…else Statement
age = int(input("Enter your age: "))

if age >= 18:
    print("Grant access.")
else:
    print("Deny access.")

#4.2 Authenticate User Logic Using if...else
# Username and password stored in database
username_db = "admin"
password_db = "sparrow@123"
# Username and password entered by the user
username = input("Enter username: ")
password = input("Enter password: ")
# Check if username & password in database matches user's input
if (username == username_db) and (password == password_db):
    print("Welcome back.")
else:
    print("Access denied.")

#4.3 Python if…elif…else Statement
age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age.")
elif age >= 18:
    print("Grant access.")
else:
    print("Deny access.")

#======================================================================#
#Python for Loop
#5.0 Iterating Through V=(A kebalik) Iist
# A list of three AI models
models = ["Fable", "ChatGPT", "Gemini"]
# Access items of the list one by one
for model in models:
    print(model)
    print("---")

#5.1 Iterating Through a String
language = 'Python'
for x in language:
    print(x)

#5.2 Sum of Natural Numbers
# Initial value of sum is 0
total = 0

# Iterate from i = 1 to 10
for i in range(1, 11):
    total += i   # Add i to total in each step
print(f"Total = {total}")

#=====================================================================#
#Python while Loop
#6.0 Infinite while Loop
number = float(input("Enter a number: "))
while number >= 0.0:
    print(number)

#6.1 Finite while Loop
number = float(input("Enter a number: "))
while number >= 0.0:
    print(number)
    # Take number input again
    number = float(input("Enter another number: "))

#6.2 Print Numbers from 1 to n
n = 10
i = 1
while i <= n:
    print(i)
    i += 1

#6.3 Sum Numbers Until User Enters Zero
total = 0
n = float(input("Enter a number (0 to stop): "))
while n != 0.0:
    total += n
    n = float(input("Enter a number (0 to stop): "))
print(f"Sum: {total}")

#=====================================================================#
#Python break and continue

#7.0 break in while Loop
number = int(input("Enter a number: "))
for i in range(1, 6):
    # Terminate the loop if i equals number
    if i == number:
        break
    print(i)

#7.1 break in while Loop
while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break
    print(f"You entered {number}")

#7.2 continue in for Loop
for i in range(1, 11):
    # Condition to check if a number is even
    if i % 2 == 0:
        continue
    print(i)

#7.3 Sum of Only Positive Numbers
total = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    # Skip negative numbers
    if number < 0:
        continue
    # End the loop if the user enters 0
    if number == 0:
        break
    total += number
print(f"Sum of positive numbers: {total}")

#=====================================================================#
#Python pass Statement

#8.0 pass Statement
is_valid = True
if is_valid:
    pass
else:
    print("Login invalid. Redirect to form.")

#=====================================================================#