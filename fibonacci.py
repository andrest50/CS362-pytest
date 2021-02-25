def fib(term):
    if term < 0:
        error = ValueError("Number should be positive")
        raise error
    if term < 2:
        return term
    num1, num2 = 0, 1
    current_num = 0
    for i in range(2, term+1):
        current_num = num1 + num2
        num1 = num2
        num2 = current_num
    return current_num

def factorial(term):
    total = term
    for i in range(term-1, 0, -1):
        total *= i
    return total