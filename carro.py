import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv("C:\\Users\\Jorge\\ejer_py\\acsv\\car\\car.csv",header=None)
#print(data)
data.columns=['precio','mantenimiento','puertas','npersonas','Tmaletero','seguridad','evaluacion']
#print(data)
#los primeros 5
print(data.head(5))

#aleatorios
print(data.sample(10))

#ultimos 5 elementos
print(data.tail(5))

#mostrar el total de tuplas y la cantidad de atributos
print(data.shape)

#el total de datos que es la multiplicacion de las filas por las columnas
print(data.size)

#################################################################################
##################################################################################


#mostrar los primeros o los ultimos registros de una columna determinada,o aleatoria
print(data['precio'].head(10))
print(data['seguridad'].tail(6))
print(data['seguridad'].sample(3))

#mostrar los rangos de un atributo
print(data['seguridad'][:3])

#mostrar un conjunto de datos
print(data[['precio','seguridad','evaluacion']].tail())

#mostrar la cantidad de datos de un atributo por cada descripcion del mismo por categorias 
print(data['evaluacion'].value_counts())

#ordenar los datos de acuerdo a los resultados por atributo  por categorias a..z
print(data['evaluacion'].value_counts().sort_index(ascending= True))

#ordenar los datos de acuerdo a los resultados por atributo z..a
print(data['evaluacion'].value_counts().sort_index(ascending= False))

#Asignar un resultado a la variable y despues imprimirla

evalua = data['evaluacion'].value_counts().sort_index(ascending= False)
print('evalucion por medio de variable')
print(evalua)

#################################################################################
##################################################################################

#graficar la variable
print('mostrar la grafica de esa variable')
evalua.plot(kind='bar')

print('mostrar los datos unicos que tiene esa variable')
#mostrar los datos que tiene un atributo sin repetir
print(data['precio'].unique())

#remplazar las categorias de texto a numerico

print('remplazando mejor texto por numeros')
data['precio'].replace(('vhigh','high','med','low'),(4,3,2,1), inplace =True)
print(data['precio'].unique())
print(data)

#hacenmos una grafica con los resultados distribucion de la informacion

grafica_autos_precio = data['precio'].value_counts()
colores=['red','yellow','blue','green']
grafica_autos_precio.plot(kind='bar',color=colores)
plt.title('PRECIO DE AUTOS')
plt.xlabel('precios')
plt.ylabel('autos')

#################################################################################
##################################################################################


#graficar otro atributo con otro tipo de grafica
#1 mosrar cuantas categorias tiene
#2 contar los datos por categoria

segu=data['seguridad'].unique()
print(segu)
canti=data['seguridad'].value_counts()
print(canti)
etiqueta = ['low','med','high']
size=[576,576,576]
colores=['red','yellow','blue']
#explode =[0,0,0]
#plt.pie(size,labels=labels,colors=colores,explode=explode, shadow=True,autopct='%.2%')
plt.pie(size,labels=etiqueta,colors=colores,startangle=180,shadow=True,explode=(0,0,0))
plt.title("NIVELES DE SEGURIDAD", fontsize=10)
plt.axis("off")
plt.legend(loc='best')
plt.show()



























