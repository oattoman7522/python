import random
import pandas as pd

# input number lange
min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))
count = int(input("Enter the number of random numbers to generate: "))


# Random Number
random_age = [random.randint(min_value, max_value) for _ in range(count)]
# random_string = [random.choice('Male', 'Female') for _ in range(count)]
random_gender = [random.choice(['ชาย', 'หญิง']) for _ in range(count)]
random_coffee = [random.choice(['อเมริกาโม่', 'ลาเต้', 'เอสเปสโซ']) for _ in range(count)]

# Calculator
average = sum(random_age)/count
print(f"The average age is: {average}")

# Sample data (replace this with your own data)
data = {
    'Gender': random_gender,
    'Age': random_age,
    'Coffee': random_coffee
    # 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    # 'Car': ['BYD', 'Neta', 'Tesla', 'Deepal']
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Specify the filename for the Excel file
filename = 'sample_data.xlsx'

# Export DataFrame to Excel
df.to_excel(filename, index=False)

print(f"Data has been exported to {filename}")


# Export excel calculator
filename1 = 'calculator.xlsx'
df = pd.DataFrame(average, columns=["average_age"])
df.to_excel(filename1, index=False)
print(f"Calculator export to {filename1}")


# import random

# # Generate a random integer between 1 and 10
# random_number = random.randint(1, 10)
# print(f"Random number between 1 and 10: {random_number}")

# # Generate a random floating-point number between 0 and 1
# random_float = random.random()
# print(f"Random float between 0 and 1: {random_float}")