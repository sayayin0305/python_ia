"REGRESION POLINOMIAL"

"IMPORTAMOS LAS LIBRERAS"
from sklearn import datasets, linear_model
import numpy as np
import matplotlib.pyplot as plt

"PREPARAR LA DATA"
boston=datasets.load_diabetes()
print(boston)
print()

"ENTENDIMIENTO DE LA DATA"
"Verificar la informacion del dataset"
"************************************"
print("informacion del dataset")
print(boston.keys())
print()

print("Caracterisdias del dataset")
print(boston.DESCR)
print()

print("Candidad de datos del dataset")
print(boston.data.shape)
print()

print("mirar el no,bre de las columnas")
print(boston.feature_names)
print()



"PREPARAMOS LOS DATOS PARA LA REFRESION POLINOMIAL"
"seleccionaremos 1 columna la 9 nivel de azucar"
print("datos seleccionados de la columna")
x_p=boston.data[:,np.newaxis,9]
print(x_p)

"definir las etiquetas para estos datos y_p"
print("Etiquetas de los datos")
y_p=boston.target
print(y_p)

"GRAFICAMOS LAS VARIABLES"
plt.scatter(x_p,y_p)
plt.show()

"######################### IMPLEMANTACION DEL REGRESION POLINOMIAL #######################"
"SEPARAMOS LOS DATOS DE ENTRENAMIENTO Y DE PRUEBA PARA PROBAR LOS ALGORITMOS"

print("Separando datos de entrenamineto y prueba")
from sklearn.model_selection import train_test_split
x_train_p,x_test_p,y_train_p,y_test_p = train_test_split(x_p,y_p,test_size=0.2)
print(x_train_p)



"se debe definir el grado del polinomio o caracteriasticas polinomiales"
"IMPORTAMOS LA LIBREARIA POLINOMIAL"

from sklearn.preprocessing import PolynomialFeatures

"Grado del polinomio"
poli_reg= PolynomialFeatures(degree=2)

"SE TRANSFORMAN LAS CARACTERISTICAS EXISTENTES EN CARACTERISTICAS DE MAYOR GRADO"
x_train_poli=poli_reg.fit_transform(x_train_p)
x_test_poli=poli_reg.fit_transform(x_test_p)

"DEFINIMOS EL ALGORITMOS PARA EL MODELO"
pr=linear_model.LinearRegression()

"ENTRENNO EL MODELO"
pr.fit(x_train_poli, y_train_p)

"REALISAMOS LA PREDICCION"

Y_pred_pr=pr.predict(x_test_poli)

"Graficamos"
plt.scatter(x_test_p,y_test_p)
plt.plot(x_test_p,Y_pred_pr,color='red',linewidth=3)
plt.show



"DATOS DE LOS POLINOMIAL"

"Calculamos el valor de los coeficientes"
print("coeficientes")
coefi=pr.coef_
print(coefi)
print("interssecion")
print(pr.intercept_)

print("presicion del algoritmo")
print(pr.score(x_train_poli, y_train_p))

"MODELO LOGRADO"

print("y=",str(coefi[1])+" X1",str(coefi[2])+ " X2^2",pr.intercept_)


















