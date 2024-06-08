import pandas as pd

data =pd.DataFrame({'name':['Alice','Bob','Charles','Alice','David'],
                    'age':[30,25,22,30,33]})
print(data)
data.drop_duplicates(inplace=True)
print(data)