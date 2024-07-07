import random
import pandas as pd

def generate_random_numbers(min_value, max_value, number_type, count):
    numbers = []
    for _ in range(count):
        if number_type == 'int':
            numbers.append(random.randint(min_value, max_value))
        elif number_type == 'float':
            numbers.append(random.uniform(min_value, max_value))
        else:
            raise ValueError("Invalid number type. Choose 'int' or 'float'.")
    return numbers

def export_to_excel(numbers, filename):
    df = pd.DataFrame(numbers, columns=["Random Numbers"])
    df.to_excel(filename, index=False)

# Get user input for range, number type, count, and filename
min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))
number_type = input("Enter the number type ('int' or 'float'): ").lower()
count = int(input("Enter the number of random numbers to generate: "))
filename = input("Enter the filename for the Excel file (e.g., 'random_numbers.xlsx'): ")

# Generate random numbers
random_numbers = generate_random_numbers(min_value, max_value, number_type, count)

# Export to Excel
export_to_excel(random_numbers, filename)

print(f"Random {number_type} numbers between {min_value} and {max_value} have been saved to {filename}")