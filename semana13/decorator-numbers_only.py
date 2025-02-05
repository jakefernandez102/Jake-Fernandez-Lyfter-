
def numbers_only(func):
    def wrapper(*args):
        if not all(isinstance(param, (int, float)) for param in args):
            raise ValueError("❌ All parameters must be numbers (int or float).")

        print("✅ All parameters are valid numbers.")
        func(*args)
    return wrapper

@numbers_only
def sum(num1,num2):
    total = 0
    total =  num1 + num2
    print(total)
    return total

sum(1,2)