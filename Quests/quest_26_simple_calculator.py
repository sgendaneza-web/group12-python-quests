def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
      return "Cannot be divided"
    return a/b

num1=float(input("Insert a number: "))
num2=float(input("Insert another number: "))
operation=(input("Insert operation(add,multipy,...): "))

if operation == "add":
    result = add(num1,num2)
elif operation == "subtract":
    result = subtract(num1,num2)
elif operation == "multiply":
    result = multiply(num1,num2)
elif operation == "divide":
    result = divide(num1,num2) 
else:
    result = "Invalid input"

print("Result:", result)                   
