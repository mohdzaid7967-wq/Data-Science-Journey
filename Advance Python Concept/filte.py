numbers = [1, 2, 3, 4, 5, 6]

# Get even numbers using filter
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]

# Equivalent list comprehension:
even_numbers_lc = [x for x in numbers if x % 2 == 0]
print(even_numbers_lc) # Output: [2, 4, 6]

# Example with None as function
values = [0, 1, [], "hello", "", None, True, False]
truthy_values = filter(None, values)
print(list(truthy_values)) # Output: [1, 'hello', True]