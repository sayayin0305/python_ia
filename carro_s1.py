import pandas as pd
import matplotlib.pyplot as plt

#leyendo el dataset
data = pd.read_csv("c:\\users\\jorge\\ejer_py\\acsv\\car\\car.csv",header=None)
#poniendo encabezados al dataset
data.columns=['precio','mantenimiento','puertas','npersonas','maletero','seguridad','evaluacion']
print(data)

#imprimir los primeros 10 datos del dataset
print("Primeros 10 registros")
print(data.head(10))

print("Ultimos 15 registros del dataset")
#imprimir los ultimos 15 datos
print(data.tail(15))

print("Ultimos 15 registros aleatoreo del dataset")
#imprimir los 15 registros randomicamente
print(data.sample(15))

print("mostrar la cantidad de registros y la cantidad de atributos")
print(data.shape)

print("mostrar la cantidad de datos")
print(data.size)

print("mostrar los primeros 10 precios")
print(data['precio'].head(10))

print("mostrar los ultimos  10 datos de la categoria del atributo seguridad")
print(data['seguridad'].tail(10))

print("mostrar 10 datos de la categoria del atributo seguridad en forma randomica")
print(data['seguridad'].sample(10))

print("mostrar los rangos que tiene un atributo")
print(data['seguridad'][:3])

print("mostrar conjunto de datos")
print(data[['precio','seguridad','evaluacion']].tail())

print("Mostrar la cantidad de datos por cada categoria de un atributo")
print(data['evaluacion'].value_counts())

print("mostrar los datos ordenados por la categoria de un atributo")
print(data['evaluacion'].value_counts().sort_index(ascending=True))

print("asignar a una variable")

evalua=data['evaluacion'].value_counts().sort_index(ascending=True)
print(evalua)

print("mostrar la variable en forma de grafica")
evalua.plot(kind="bar")

print("mostrar los valores unicos que tiene un atributo")
print(data['precio'].unique())

print("Remplazar los valores-texto por numeros")
data['precio'].replace(('vhigh','high','med','low'),(4,3,2,1),inplace=True)
print(data['precio'].unique())

gprecio=data['precio'].value_counts()
colores=['red','blue','yellow','pink']
gprecio.plot(kind="bar",color=colores)
plt.title("PRECIO DE LOS AUTOS")
plt.xlabel("precios")
plt.ylabel("autos")


segu=data['seguridad'].unique()
print(segu)
cant=data['seguridad'].value_counts()
print(cant)

etiqueta=['low','med','high']
size=[576,576,576]
colores=['red','yellow','pink']
plt.pie(size,labels=etiqueta,colors=colores,startangle=180,shadow=True,explode=(0,0,0))
plt.title("NIVELES DE SEGURIDAD",fontsize=10)
plt.axis("off")
plt.legend(loc="best")
plt.show()














