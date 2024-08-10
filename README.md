# Simple Calculator
## Overview
**Welcome to the Simple Calculator! This is a versatile calculator that can handle a variety of mathematical operations, including basic arithmetic, exponentiation, factorial calculations, square roots, and trigonometric functions. Whether you need to add, subtract, multiply, divide, or perform more complex calculations, this tool has you covered.**

## 🚀 Features
- **Basic Arithmetic:** Addition, subtraction, multiplication, and division.
- **Exponentiation:** Compute the power of a number.
- **Factorial:** Calculate the factorial of an integer.
- **Square Root:** Find the integer square root of a number.
- **Modulo:** Compute the remainder of a division.
- **Trigonometric Functions:** Calculate sine, cosine, and tangent for a given angle.
## 🛠️ How to Use
- **Start the Program:** Run the script to launch the calculator.
- **Choose an Operation:** Select the type of calculation you want to perform by entering the corresponding number.
- **Input Numbers:**
    - For basic arithmetic, exponentiation, factorial, and modulo operations, enter the required numbers when prompted.
    - For trigonometric functions, enter the angle in degrees and select the function (sin, cos, tan).
- **Get Results:** The program will display the result of the calculation.
- **Repeat or Exit**: Choose to perform another calculation or exit the program.
## 📜 Code Breakdown
**calc Class**
- **Initialization:** Sets up the numbers and choice for the operation.
- **evalute() Method:** Performs the calculation based on the selected operation:
    - **Addition:** Adds two numbers.
    - **Subtraction:** Subtracts the second number from the first.
    - **Multiplication:** Multiplies two numbers.
    - **Division:** Divides the first number by the second (handles division by zero).
    - **Exponentiation:** Raises the first number to the power of the second.
    - **Factorial:** Computes the factorial of the first number (only works with non-negative integers).
    - **Square Root:** Computes the integer square root of the first number.
    - **Modulo:** Computes the remainder of the division of the first number by the second.
    - **Trigonometric Functions:** Computes sine, cosine, or tangent based on the given angle.
