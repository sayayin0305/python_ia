import numpy as np
import pandas as pd

# Leer el archivo CSV en un DataFrame
df = pd.read_csv("C:\\Users\\Jorge\\ejer_py\\acsv\\saya.csv")

# Imprimir el DataFrame
print("dataframe")
print(df)

print("Imprimir información sobre los valores faltantes")
# Imprimir información sobre los valores faltantes
print(df.isnull())

