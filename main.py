
# Create a list
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("Original list:", my_list)

# Alter the contents of the list
my_list[1] = 'blueberry'  # Replace 'banana' with 'blueberry'
my_list.append('fig')     # Add 'fig' to the end of the list
my_list.remove('cherry')  # Remove 'cherry' from the list
print("Modified list:", my_list)

# Extract one item from the list and save it as a variable
extracted_item = my_list.pop(2)  # Remove and return the item at index 2
print("Extracted item:", extracted_item)
print("List after extraction:", my_list)

# Store the value in a dictionary with a key pointing to it
my_dict = {'fruit': extracted_item}
print("Dictionary after storing extracted item:", my_dict)

# Add more key and value pairs to the dictionary
my_dict['vegetable'] = 'carrot'
my_dict['grain'] = 'rice'
my_dict['protein'] = 'chicken'
print("Dictionary after adding more key-value pairs:", my_dict)

# Retrieve and print the stored dictionary value by accessing it with a key
stored_value = my_dict['fruit']
print("Retrieved value using the 'fruit' key:", stored_value)

