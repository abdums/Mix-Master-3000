import random

# Read the list from the file
def read_list_from_file(file_path):
    with open(file_path, 'r') as file:
        items = file.read().splitlines()  # Read lines and remove newline characters
    return items

# Function to print the list in random order
def print_random_order(file_path):
    items = read_list_from_file(file_path)
    random.shuffle(items)  # Shuffle the list in place
    for item in items:
        print(item)

# Define the file path
file_path = '../jumble/list.txt'

# Print the list in random order
print_random_order(file_path)

