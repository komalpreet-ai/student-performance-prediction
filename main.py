import pandas as pd

# Load the student dataset
data = pd.read_csv("student_data.csv")

# Display the dataset
print(data)

# Display basic information
print("\nDataset Information:")
print(data.info())

# Show first 5 students
print("\nFirst 5 rows:")
print(data.head())

# Show column names
print("\nColumns:")
print(data.columns)

# Show basic statistics
print("\nStatistics:")
print(data.describe())

# Separate input features and target
X = data[["Study_Hours", "Attendance", "Previous_Marks", "Assignments"]]
y = data["Final_Marks"]

print("\nInput Features:")
print(X)

print("\nTarget:")
print(y)