import sys

def add_numbers(num1, num2):
  return num1 + num2

if __name__ == "__main__":
  num1 = float(sys.argv[1])
  num2 = float(sys.argv[2])
   
  result = add_numbers(num1, num2)
  print ("The sum of", num1, "and", num2, "is:", result) 
