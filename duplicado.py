import pandas as pd

# Create a DataFrame with missing values
data = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David'],
                   'Age': [30, 25, 22, 30, 33]})

print("DATOS con duplicados")
# Print the DataFrame before removing missing values
print(data)

# Remove rows with missing values using dropna(inplace=True)
data.drop_duplicates(inplace=True)
print("DATOS  sin duplicados")
# Print the DataFrame after removing missing values
print(data)