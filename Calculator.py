# Python program of calculator

import math
class calc:
    def __init__(self,num1,num2,choice):
        self.num1 = num1
        self.num2 = num2
        self.choice = choice

    def evalute(self):
        if(self.choice == 1 ):
            print(num1+num2)
        elif(self.choice == 2 ) :
            print(num1-num2)
        elif(self.choice == 3 ) :
            print(num1*num2)
        elif(self.choice == 4 ) :
            if (num2 != 0):
                print(num1/num2)
            else:
                print("anything divided by zero is not defined")
        elif(self.choice == 5 ) :
            print(math.pow(num1,num2))
        elif(self.choice == 6 ) :
            print(math.factorial(int(num1)))
        elif(self.choice == 7 ) :
            print(math.isqrt(int(num1)))
        elif(self.choice == 8 ) :
            print(num1%num2)
        elif(self.choice == 9 ) :
            if num2 == 1:
                print(math.sin(num1))
            elif num2 == 2:
                print(math.cos(num1))
            elif num2 == 3:
                print(math.tan(num1))
            else :
                print("Wrong choice try again")

num1 = 0
num2 = 0
repeat = 'y'
try :
    while repeat == 'y':
        choice = int(input("""Enter choice:
1 : Addition
2 : Subtraction
3 : Multiplication
4 : Division
5 : Exponent
6 : Factorial
7 : SquareRoot
8 : Modulo
9 : Trignometric Functions
"""))
        if (choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 8):
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number : "))
            cal = calc(num1,num2,choice)
            cal.evalute()
        elif (choice == 5):
            try:
                num1 = float(input("Enter base number : "))
                num2 = float(input("Enter Power : "))
                cal = calc(num1,num2,choice)
                cal.evalute()
            except OverflowError:
                print("Number out of range try again")
        elif (choice == 6 or choice == 7):
            num1 = float(input("Enter number : "))
            cal = calc(num1,num2,choice)
            cal.evalute()
        elif (choice == 9):
            num2 = int(input("""Enter choice :
1 : Sin 
2 : Cos  
3 : Tan
"""))
            num1 = int(input("Enter Angle : "))
            cal = calc(num1,num2,choice)
            cal.evalute()
        else :
            print("Wrong choice Try Again")
            break

        repeat = input("Enter y to do it again or n to stop :")
except ValueError:
    print("Wrong input try again")