"""Testing using pytest"""
import fibonacci

def test_fibonacci():
    assert fibonacci.fib(0) == 0
    assert fibonacci.fib(2) == 1
    assert fibonacci.fib(4) == 3
    assert fibonacci.fib(5) == 5
    assert fibonacci.fib(7) == 13

def test_factorial():
    assert fibonacci.factorial(1) == 1
    assert fibonacci.factorial(3) == 6
    assert fibonacci.factorial(4) == 24
    assert fibonacci.factorial(5) == 120
    assert fibonacci.factorial(6) == 720

if __name__ == "__main__":
    test_fibonacci()  