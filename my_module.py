# my_module.py
#nice function
def reverse_text(text):
    """Reverses the given string."""
    return text[::-1]

def simple_calculator(a, b, operator):
    """Performs basic arithmetic operations."""
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b if b != 0 else "Division by zero error"
    else:
        return "Invalid operator"
