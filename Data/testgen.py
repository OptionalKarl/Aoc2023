custom_order = {'C': 0, 'A': 1, 'B': 2}

# Define a custom sorting function using the custom_order dictionary
def custom_sort(char):
    return custom_order.get(char, float('inf'))

# Example list of characters
chars = ['B', 'C', 'A', 'B', 'C', 'A']

# Sort the list using the custom sorting function
sorted_chars = sorted(chars, key=custom_sort)

print(sorted_chars)  # Output: ['C', 'C', 'A', 'A', 'B', 'B']