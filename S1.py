import os

def add_numbers(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    # Fetching input from Jenkins secrets
    num1 = int(os.environ['secret1'])
    num2 = int(os.environ['secret2'])
    
    # Adding the numbers
    result = add_numbers(num1, num2)
    
    # Printing the output
    print("The sum of", num1, "and", num2, "is:", result)
