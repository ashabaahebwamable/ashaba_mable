


def factorial_iterative(n):
    
    if n < 0:
        return None  
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result



def show_factorial_calculation(n):
    
    if n <= 1:
        return f"{n}! = 1"
    
    steps = []
    for i in range(n, 0, -1):
        steps.append(str(i))
    
    calculation = " × ".join(steps)
    return f"{n}! = {calculation}"

def main():

    print("=" * 55)
    
    
    number = 5
    
    print(f"Finding factorial of {number}:")
    print()
    
    
    print("Step-by-step calculation:")
    print(show_factorial_calculation(number))
    
   
    result_iterative = factorial_iterative(number)
    print(f"\nUsing iterative method: {number}! = {result_iterative}")
    
    
    
   
    print(f"\nVerification: 5! = 5 × 4 × 3 × 2 × 1 = {result_iterative}")
    
    
if __name__ == "__main__":
    main()