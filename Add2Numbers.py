def add_numbers(num1, num2):
    return(num1 + num2)

if __name__ == "__main__":
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    result = add_numbers(num1, num2)

    print("The sum of 2 numbers is:",result)

