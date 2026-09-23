# Python Data Types Examples
# This file demonstrates the main built-in data types in Python.

# 1. Integer
age = 25
print("Integer:", age, type(age))

# 2. Float
price = 19.99
print("Float:", price, type(price))

# 3. String
name = "Alice"
print("String:", name, type(name))

# 4. Boolean
is_active = True
print("Boolean:", is_active, type(is_active))

# 5. List (ordered, changeable, allows duplicates)
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print("List:", numbers, type(numbers))

# 6. Tuple (ordered, immutable)
coordinates = (10, 20)
print("Tuple:", coordinates, type(coordinates))

# 7. Set (unordered, unique items)
unique_numbers = {1, 2, 2, 3, 3, 4}
print("Set:", unique_numbers, type(unique_numbers))

# 8. Dictionary (key-value pairs)
student = {"name": "Bob", "age": 21, "grade": "A"}
print("Dictionary:", student, type(student))

# 9. NoneType
result = None
print("None:", result, type(result))

# 10. Complex numbers
complex_number = 3 + 4j
print("Complex:", complex_number, type(complex_number))

# 11. Bytes
byte_data = b"hello"
print("Bytes:", byte_data, type(byte_data))

# Example of type conversion
num_str = "100"
num_int = int(num_str)
print("Converted integer:", num_int, type(num_int))

float_value = float("12.5")
print("Converted float:", float_value, type(float_value))

# Extra example: checking data type
print("Is age an int?", isinstance(age, int))
print("Is name a string?", isinstance(name, str))

# End of file
