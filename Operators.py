# Arithmetic Operators

# Arithmetic Operators

# Addition
a = 10
b = 5
sum_result = a + b
print(f"Addition: {a} + {b} = {sum_result}")

# Subtraction
diff_result = a - b
print(f"Subtraction: {a} - {b} = {diff_result}")

# Multiplication
prod_result = a * b
print(f"Multiplication: {a} * {b} = {prod_result}")

# Division
div_result = a / b
print(f"Division: {a} / {b} = {div_result}")

# Floor Division (integer division)
floor_div_result = a // b
print(f"Floor Division: {a} // {b} = {floor_div_result}")


# Modulus (remainder)
mod_result = a % b
print(f"Modulus: {a} % {b} = {mod_result}")

# Exponentiation
exp_result = a ** b
print(f"Exponentiation: {a} ** {b} = {exp_result}")

# Addition: 10 + 5 = 15
# Subtraction: 10 - 5 = 5
# Multiplication: 10 * 5 = 50
# Division: 10 / 5 = 2.0
# Floor Division: 10 // 5 = 2
# Modulus: 10 % 5 = 0
# Exponentiation: 10 ** 5 = 100000

# Assignment Operators

# = (Assignment)
x = 10  # Assigns the value 10 to the variable x

# += (Add and Assign)
x += 5  # Equivalent to x = x + 5
print(f"Add and Assign: x = {x}")

# -= (Subtract and Assign)
x -= 3  # Equivalent to x = x - 3
print(f"Subtract and Assign: x = {x}")

# *= (Multiply and Assign)
x *= 2  # Equivalent to x = x * 2
print(f"Multiply and Assign: x = {x}")

# /= (Divide and Assign)
x /= 4  # Equivalent to x = x / 4
print(f"Divide and Assign: x = {x}")

# %= (Modulus and Assign)
x %= 3 # Equivalent to x = x % 3
print(f"Modulus and Assign: x = {x}")

# //= (Floor Division and Assign)
x = 10
x //= 3  # Equivalent to x = x // 3
print(f"Floor Division and Assign: x = {x}")

# **= (Exponentiation and Assign)
x **= 2  # Equivalent to x = x ** 2
print(f"Exponentiation and Assign: x = {x}")

# &= (Bitwise AND and Assign)
x = 10
x &= 5  # Performs a bitwise AND operation and assigns the result
print(f"Bitwise AND and Assign: x = {x}")


# |= (Bitwise OR and Assign)
x |= 3 # Performs a bitwise OR operation and assigns the result
print(f"Bitwise OR and Assign: x = {x}")

# ^= (Bitwise XOR and Assign)
x ^= 7  # Performs a bitwise XOR operation and assigns the result
print(f"Bitwise XOR and Assign: x = {x}")


# >>= (Right Shift and Assign)
x >>= 1 # Performs a right shift operation and assigns the result
print(f"Right Shift and Assign: x = {x}")

# <<= (Left Shift and Assign)
x <<= 2 # Performs a left shift operation and assigns the result
print(f"Left Shift and Assign: x = {x}")

# Identity Operators
x = 5
y = 5
z = 10

print(x is y)  # Output: True (x and y refer to the same object in memory)
print(x is not z) # Output: True (x and z do not refer to the same object)
print(x is not y) # Output: False

# Membership Operators
my_list = [1, 2, 3, 4, 5]

print(2 in my_list)  # Output: True (2 is present in my_list)
print(6 in my_list)  # Output: False (6 is not present in my_list)
print(2 not in my_list) # Output: False (2 is present, so it's not not in)
print(6 not in my_list) # Output: True