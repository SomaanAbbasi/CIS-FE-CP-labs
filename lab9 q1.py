#calculator
#Somaan 101


def add(x, y):
    return (x+y)

def subtract(x, y):
    return (x-y)

def multiply(x, y):
    return (x*y)

def divide(x, y):
    return (x/y)


x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
operator = input("Enter the operation you want to perform (+ - * /):  ")

if operator == '+':
    print(add(x, y))

elif operator == '-':
    print(subtract(x,y))
    
elif operator == '*':
    print(multiply(x,y))

elif operator == '/':
    print(divide(x, y))

else:
    print("Invalid operator entered")