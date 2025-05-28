

class Calculator:
    
    def add(self, a, b=None, c=None, d=None):
        if b is None:
            return a
        elif c is None:
            return a + b
        elif d is None:
            return a + b + c
        else:
            return a + b + c + d
    
    def multiply(self, *args):
        
        if len(args) == 0:
            return 1
        
        result = 1
        for num in args:
            result *= num
        return result
    
    def power(self, base, exponent=2):
        
        return base ** exponent
    
    def divide(self, a, b=None):
        
        if b is None:
            return 1 / a  # Reciprocal
        else:
            return a / b  # Normal division
    
    def calculate(self, *numbers, operation='sum'):
        
        if not numbers:
            return 0
        
        if operation == 'sum':
            return sum(numbers)
        elif operation == 'product':
            result = 1
            for num in numbers:
                result *= num
            return result
        elif operation == 'average':
            return sum(numbers) / len(numbers)
        elif operation == 'max':
            return max(numbers)
        elif operation == 'min':
            return min(numbers)
        else:
            return f"Unknown operation: {operation}"

class StringProcessor:
    
    
    def format_text(self, text, style=None, length=None):
        
        result = text
        
    
        if style == 'upper':
            result = result.upper()
        elif style == 'lower':
            result = result.lower()
        elif style == 'title':
            result = result.title()
        elif style == 'reverse':
            result = result[::-1]
        
        
        if length is not None:
            if len(result) < length:
                result = result.ljust(length)  
            elif len(result) > length:
                result = result[:length]  
        
        return result
    
   
        

def main():
    
    
    
    calc = Calculator()
    
    print("1. ADD METHOD OVERLOADING:")
    print(f"add(5): {calc.add(5)}")
    print(f"add(5, 3): {calc.add(5, 3)}")
    print(f"add(5, 3, 2): {calc.add(5, 3, 2)}")
    print(f"add(5, 3, 2, 1): {calc.add(5, 3, 2, 1)}")
    
    print("\n2. MULTIPLY METHOD OVERLOADING:")
    print(f"multiply(): {calc.multiply()}")
    print(f"multiply(5): {calc.multiply(5)}")
    print(f"multiply(5, 3): {calc.multiply(5, 3)}")
    print(f"multiply(5, 3, 2): {calc.multiply(5, 3, 2)}")
    print(f"multiply(2, 3, 4, 5): {calc.multiply(2, 3, 4, 5)}")
    
    print("\n3. POWER METHOD OVERLOADING:")
    print(f"power(5): {calc.power(5)}")
    print(f"power(5, 3): {calc.power(5, 3)}")
    print(f"power(2, 8): {calc.power(2, 8)}")
    
    print("\n4. DIVIDE METHOD OVERLOADING:")
    print(f"divide(8): {calc.divide(8)}")
    print(f"divide(8, 2): {calc.divide(8, 2)}")
    print(f"divide(15, 3): {calc.divide(15, 3)}")
    
    print("\n5. CALCULATE METHOD OVERLOADING:")
    print(f"calculate(1, 2, 3, 4, 5): {calc.calculate(1, 2, 3, 4, 5)}")
    print(f"calculate(1, 2, 3, 4, 5, operation='product'): {calc.calculate(1, 2, 3, 4, 5, operation='product')}")
    print(f"calculate(1, 2, 3, 4, 5, operation='average'): {calc.calculate(1, 2, 3, 4, 5, operation='average')}")
    print(f"calculate(1, 2, 3, 4, 5, operation='max'): {calc.calculate(1, 2, 3, 4, 5, operation='max')}")

    
    processor = StringProcessor()
    
if __name__ == "__main__":
    main()