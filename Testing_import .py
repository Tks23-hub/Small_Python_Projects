import Calculater_python  # This imports your calculator script by its filename (without .py)

print("Testing the imported calculator functions:")

# Test addition
result = Calculater_python.add(5, 3)
print(f"5 + 3 = {result}")

# Test subtraction
result = Calculater_python.subtract(10, 4)
print(f"10 - 4 = {result}")

# Test multiplication
result =Calculater_python.multiply(7, 6)
print(f"7 * 6 = {result}")

# Test division
result = Calculater_python.divide(8, 2)
print(f"8 / 2 = {result}")

# Test division by zero
result = Calculater_python.divide(5, 0)
print(f"5 / 0 = {result}")
