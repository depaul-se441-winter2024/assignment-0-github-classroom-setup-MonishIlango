import calculator
import pytest                             # imports pytest dependency

# Test multiplication function
def test_multiply():
    assert calculator.multiply(2, 6) == 12
    assert calculator.multiply(3, 5) == 15
    assert calculator.multiply(5, 2) == 10

# Test division function
def test_divide():
    assert calculator.divide(10, 5) == 2
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(8, 4) == 2
    assert calculator.divide(5, 0) == "Error: Division by zero"

if __name__ == "__main__":
    pytest.main()
