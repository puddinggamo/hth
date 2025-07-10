# Debudding activity - Candy Tang

# section 1 
# dividing by zero is impossible, dividing by 5 is better
x = 10
y = 5
result = x / y
print("Result:", result)

# section 2
# replaced the i for an actual number
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[3+1])

# section 3 
# fixed indent
def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area

radius = 5
print(calculate_area(radius))

# section 4 
# missing colon
def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))

# section 5
# missing colon
for i in range(5):
   print(i)

# Section 6 
# Divided the message from the code
def greet(name):
   return "Hello," + name

print(greet("Alice"))

# Section 7
# indented
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
  sum += number
print("Sum of numbers:", sum)

# Section 8 
# negative
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)
print(factorial(5))

# Section 9 
# peranthesis
name = input("Enter your name: ")
if name == ("Alice" or "Bob"):
   print("Hello, " + name)
else:
   print("Hello, stranger!")

# Section 10
# you cant divdide by 0
def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 5
print(divide_numbers(num1, num2))






