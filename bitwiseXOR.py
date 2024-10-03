# Practical use case of how powerful Bitwise Logical Operator (XOR) use case
# Swap value without additional variable
a = 5
b = 2

# a = a ^ b
a^=b
# b = a ^ b
b^=a
# a = a ^ b
a^=b
print(f"a: {a}, b: {b}")
