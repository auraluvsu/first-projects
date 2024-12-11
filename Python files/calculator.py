import math

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def exponentiation(x, y):
    return pow(x, y)
def squareroot(x, y):
    return
while True:
    print("Welcome to the calculator! \n")

    #This will take in the operation the user chooses
    operation = int(input(
        """Please choose an operation:
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Exponentiate
        6. Square root
        ---------------- \n"""
        ))
    
    if operation == 1 or operation == 2 or operation == 3 or operation == 4 or operation == 5:
        num1 = int(input("Now enter first number: \n"))
        num2 = int(input("Now enter second number: \n"))

        #Addition
        if operation == 1:
            sum = add(num1, num2)
            print(sum)

        #Subtraction
        elif operation == 2:
            difference = subtract(num1, num2)
            print(f"The difference between the numbers is: {difference}")
        
        #Multiplication
        elif operation == 3:
            product = multiply(num1, num2)
            print(f"The product of multiplying these numbers is: {product}")

        #Division
        elif operation == 4:
            quotient:float = divide(num1, num2)
            final_quotient = round(quotient, 5)
            print(f"The quotient of these two numbers is: {final_quotient}")

        #Exponents
        elif operation == 5:
            result = exponentiation(num1, num2)
            print(f"The result of expanding the exponent is: {result}")
    
    #Square roots
    elif operation == 6:
        num3 = int(input("Please state the number that is to be rooted \n"))
        root = math.sqrt(num3)
        print(f"The square root of {num3} is {root} \n")
    
    #Minor error handling
    else:
        print("Please choose a valid operation!")
    
    #This gives the option to loop the calculator or end it
    retry = input("        Calculate new number? \n             Yes or No \n").lower()
    if retry != "yes":
        print("Goodbye!")
        break