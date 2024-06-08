
"Importar las librerias"
from sklearn import datasets, linear_model
import numpy as np
import matplotlib.pyplot as plt

"PREPARAR LA DATA"
boston=datasets.load_diabetes()
print(boston)
print()

"ENTENDER LA DATA"
"Verificar la informacion"
"*******************************"
print("Informacion del dataset")
print(boston.keys())
print()

print("Caracteristicas del dataset")
print(boston.DESCR)
print()

print("Cantidad de datos")
print(boston.data.shape)
print()

print("Mirar en nombre de las columnas")
print(boston.feature_names)
print()




"PREPARAMOS LOS DATOS PARA LA REGRESION POLINOMIAL"
print("Seleciono una columna")
x_svr=boston.data[:,np.newaxis,6]
print(x_svr)

print("selecionamos las etiquetas de los datos y_p")
y_svr=boston.target
print(y_svr)

"GRAFICAMOS A VER COMO SE OBSERVAN LOS DATOS"
plt.scatter(x_svr,y_svr)
plt.show()


"IMPLEMENTAR LA REGRESION POLINOMIAL"
"Separar los datos de entrenamiento y de test"
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x_svr,y_svr,test_size=0.2)
print(x_train)

"DEFINIR EL GRADO DEL POLINOMIO"
from sklearn.svm import SVR
svr = SVR(kernel='linear',C=1.0,epsilon=0.2)

"ENTRENAR EL MODELO"
svr.fit(x_train,y_train)

"REALIZAR LA PREDICCION"
y_pred =svr.predict(x_test)




"Graficar"
plt.scatter(x_test,y_test)
plt.plot(x_test,y_pred,color="red",linewidth=1)
plt.show


print("presicion del algoritmo")
print(svr.score(x_train, y_train))





















