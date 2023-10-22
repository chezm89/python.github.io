def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y


x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))


sum = add(x,y)
differnce = subtract(x,y)
product = multiply(x,y)
division = divide(x,y)

print(f"The sum of {x} + {y} is {sum}")
print(f"The differnce of {x} - {y} is {differnce}")
print(f"The product of {x} x {y} is {product}")
print(f"{x} / {y} is {int(division)}")










