# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    # enter the two numbers
    # convert the entered value to float value
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # execute the two functions
    product = multiply(num1, num2)     # multiplication of two numbers
    quotient = divide(num1, num2)    # division of two numbers

    # print the values
    print("The product is: ", product)
    print("The quotient is: ", quotient)

if __name__ == "__main__":
    main()
