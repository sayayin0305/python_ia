import pandas as pd
data = pd.DataFrame({
    'name':['Alice','Bob','Charles',None,'David'],
    'age':[30,25,22,None,33],
    'City':['Bogota','Cali','Neiva',None,'Chicago']
    })

print(data)
data.dropna(inplace=True)
print(data)