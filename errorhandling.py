
def get_valid_number(prompt):
    """Function to keep asking for a valid number until one is provided"""
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Error: Please enter a valid number!")
            print("Try again...")

def divide_numbers():
    
    
    num1 = get_valid_number("Enter the first number: ")
    
   
    while True:
        num2 = get_valid_number("Enter the second number: ")
        try:
            
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            break  
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            print("Please enter a non-zero number for division.")
    
    
    try:
        result = num1 / num2
        print(f"\nResult: {num1} ÷ {num2} = {result}")
        print("Division completed successfully!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



# Main execution
def main():
    
     divide_numbers()
    


if __name__ == "__main__":
    main()