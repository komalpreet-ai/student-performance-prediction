import pandas as pd

# Load the student dataset
data = pd.read_csv("student_data.csv")

# Display the dataset
print(data)

# Display basic information
print("\nDataset Information:")
print(data.info())