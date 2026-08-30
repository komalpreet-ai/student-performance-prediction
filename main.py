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

from sklearn.model_selection import train_test_split

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining data:")
print(X_train)

print("\nTesting data:")
print(X_test)

from sklearn.linear_model import LinearRegression

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("\nModel trained successfully!")