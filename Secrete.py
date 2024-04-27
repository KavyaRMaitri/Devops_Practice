import os

def add_numbers(num1, num2):
        result = float(num1) + float(num2)
        print(f"The result of {num1} + {num2} is: {result}")

if __name__ == "__main__":
    secret_num1 = os.environ.get('Secrete_number1')
    secret_num2 = os.environ.get('Secrete_number2')

    add_numbers(secret_num1, secret_num2)
