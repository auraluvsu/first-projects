import math

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def floor_division(x, y):
    return x // y
def exponentiation(x, y):
    return pow(x, y)
def squareroot(x):
    return math.sqrt(x)
def circle_area(x):
    return math.pi * (x**2)
def baseheight(x, y):
    return x * y
def square_area(x):
    return x ** 2
def trapezoid_area(x, y, z):
    return ((x + y) / 2) * z
def triangle_area(x, y):
    return (x * y) / 2

while True:
    print("Welcome to the calculator! \n")

    #This will take in the operation the user chooses
    operate = int(input(
        """Please choose an operation:
        1. Basic operations
        2. Geometry
        ------------------- \n"""
        ))
    if operate == 1:
        operation = int(input(
            """Please Choose a basic operation:
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            5. Floor Division
            6. Exponentiation
            7. Square root
            8. Minimum and Maximum
            ----------------------- \n"""
            ))

        if operation == 1 or operation == 2 or operation == 3 or operation == 4 or operation == 5:
            num1 = int(input("Now enter first number: \n"))
            num2 = int(input("Now enter second number: \n"))

            #Addition
        if operation == 1:
            sum = add(num1, num2)
            print(f"The sum of these two numbers is: {sum}")

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
            
            #Floor Division
        elif operation == 5:
            floor_quotient = floor_division(num1, num2)
            print(f"The result of this floor division process is: {floor_quotient}")
            
            #Exponents
        elif operation == 6:
            result = exponentiation(num1, num2)
            print(f"The result of expanding the exponent is: {result}")
        
        #Square roots
        elif operation == 7:
            num3 = int(input("Please state the number that is to be rooted \n"))
        if num3 < 0:
            print("Error: the square root of a negative number is not defined")
            continue
            root = squareroot(num3)
            print(f"The square root of {num3} is {root} \n")

        #Minimum input and Maximum output
    elif operation == 8:
        minmaxstr = input("Please input multiple numbers")
        minmaxsplit = minmaxstr.split()
        minmaxint = [int(n) for n in minmaxsplit]
        minimum_var = min(minmaxint)
        maximum_var = max(minmaxint)
        print(f"The minimum is {minimum_var} and the maximum is {maximum_var}")

    if operate == 2:
        geometry = int(input(
            """Please choose a geometry operation
            1. Circle Area
            2. Square Area
            3. Rectangle Area
            4. Parallelogram Area
            5. Trapezoid Area
            6. Triangles
            7. 3D Shapes
            --------------------- \n"""
        ))
    
    
    #Area of a circle
    elif geometry == 1:
        radius = int(input("Please specify the radius: \n"))
        if radius <= 0:
            print("Error: Radius must be a positive number! \n")
            continue
        area_of_circle = circle_area(radius)
        area_of_circle_rounded = round(area_of_circle, 2)
        print(f"The area of your circle is {area_of_circle} or {area_of_circle_rounded}")
    
    #Area of a square
    elif geometry == 2:
        side_of_square = int(input("Enter the length of one side of your square: \n"))
        if side_of_square <= 0:
            print("Error: Please enter a positive number! \n")
            continue
        area_of_square = square_area(side_of_square)
        print(f"The area of your square is {area_of_square}")

    #Area of a rectangle
    elif geometry == 3:
        rec_base = int(input("Enter base of rectangle: \n"))
        rec_height = int(input("Enter height of rectangle: \n"))
        rec_area = baseheight(rec_base, rec_height)
        print(f"The area of your rectangle is {rec_area}")
    
    #Area of a parallelogram
    elif geometry == 4:
        para_base = int(input("Enter the parallelogram base: \n"))
        para_height = int(input("Enter the parallelogram height: \n"))
        para_area = baseheight(para_base, para_height)
        print(f"The area of your parallelogram is {para_area}")
    
    #Area of a trapezoid
    elif geometry == 5:
        trap_topbase = int(input("Enter the trapezoid roof length: \n"))
        trap_bottombase = int(input("Enter the trapezoid base: \n"))
        trap_height = int(input("Enter the trapezoid height: \n"))
        trap_area = trapezoid_area(trap_topbase, trap_topbase, trap_height)
        print(f"The area of your trapezoid is {trap_area}")
    
    #Area of a triangle
    elif geometry == 6:
        triangle_base = int(input("Enter the base of the triangle: \n"))
        triangle_height = int(input("Entyer the height of the triangle"))
        area_of_triangle = triangle_area(triangle_base, triangle_height)
        print(f"The area of your triangle is {area_of_triangle}")



    #Minor error handling
    else:
        print("Please choose a valid operation!")
    
    #This gives the option to loop the calculator or end it
    retry = input("        Calculate new number? \n             Yes or No \n").lower()
    if retry != "yes":
        print("Goodbye!")
        break