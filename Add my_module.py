def reverse_text(text):
    """Reverse the input text"""
    return text[::-1]

def simple_calculator(num1, num2, operation):
    """Perform basic calculations"""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return "Invalid operation"
