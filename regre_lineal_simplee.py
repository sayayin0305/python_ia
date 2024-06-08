import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

#importar la data de sklearn

boston=datasets.load_diabetes()
print(boston)
print('***************************************************')
print('keys')
print(boston.keys())
print('***************************************************')
print('Caracteristicas de la data')
print(boston.DESCR)
print('***************************************************')
print('cantidad de datos')
print(boston.data.shape)
print('NOMBRE DE LAS COLUMNAS')
print(boston.feature_names)
#definir la variable independiente y dependiente
x=boston.data[:,np.newaxis,0]
y=boston.target

#graficar

plt.scatter(x, y)
plt.xlabel("mean area")
plt.ylabel("valor medio")
plt.show

#separar los datos de entrenamiento de los de prueba 80-20
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#definir el algoritmo a utilizar
lr=linear_model.LinearRegression()

#entrenar el modelo
lr.fit(x_train,y_train)

#realizar el entrenamiento
y_pred=lr.predict(x_test)

plt.scatter(x_test,y_test,color="red",label="datos reales")
plt.plot(x_test,y_pred,color="blue",label="Prediccion")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regrecion lineal")
plt.legend()
plt.show

#mostrar la pendente
print("pendiente")
print(lr.coef_)

#calcular la interseccion
print("interseccion")
print(lr.intercept_)

#crear la ecuacion
print("y = ",lr.coef_," X ",lr.intercept_)

#mirar la presicion del modelo
print(lr.score(x_train, y_train))
























