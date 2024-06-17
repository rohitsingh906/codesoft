def add(num1, num2):
  """Adds two numbers and returns the sum."""
  return num1 + num2

def subtract(num1, num2):
  """Subtracts two numbers and returns the difference."""
  return num1 - num2

def multiply(num1, num2):
  """Multiplies two numbers and returns the product."""
  return num1 * num2

def divide(num1, num2):
  """Divides two numbers and returns the quotient, handling division by zero."""
  if num2 == 0:
    return "Error: Cannot divide by zero."
  else:
    return num1 / num2

def get_user_input():
  """Gets user input for the first and second numbers."""
  while True:
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      return num1, num2
    except ValueError:
      print("Invalid input. Please enter numbers only.")

def main():
  """Main function to handle user interaction and calculations."""
  print("Welcome to the Simple Calculator!")

  while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
      num1, num2 = get_user_input()
      result = add(num1, num2)
      print(f"{num1} + {num2} = {result}")
    elif choice == '2':
      num1, num2 = get_user_input()
      result = subtract(num1, num2)
      print(f"{num1} - {num2} = {result}")
    elif choice == '3':
      num1, num2 = get_user_input()
      result = multiply(num1, num2)
      print(f"{num1} * {num2} = {result}")
    elif choice == '4':
      num1, num2 = get_user_input()
      result = divide(num1, num2)
      print(result)
    elif choice == '5':
      print("Exiting calculator.")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
