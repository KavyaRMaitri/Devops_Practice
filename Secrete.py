import os

def add_numbers(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    
    num1 = int(os.environ('num1'))
    num2 = int(os.environ('num2'))
    
    result = add_numbers(num1, num2)
    print("The sum of", num1, "and", num2, "is:", result)
