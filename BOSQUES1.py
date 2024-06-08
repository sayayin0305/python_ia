"BOSQUES - CONJUNTO DE ARBOLES"
" Nueva version"
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

"SELECCIONAR LA COLUMNA"

x_bar=boston.data[:,np.newaxis,9]
print(x_bar)

"ETIQUETAS"
y_bar=boston.target
print(y_bar)

"GRAFICA"
plt.scatter(x_bar,y_bar)
plt.show()

"SEPARAR LOS DATOS TRAIN - TEST "
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_bar, y_bar,test_size=0.2)

"IMPORTAR LA LIBRERIA PARA EL BOSQUE"
from sklearn.ensemble import RandomForestRegressor

"definir el algoritmo"

bar =RandomForestRegressor(n_estimators=100,max_depth=8)

"ENTRENAR EL MODELO"
bar.fit(x_train,y_train)

"REALIZAR LA PREDICCION"
y_pred_bar=bar.predict(x_test)

"GRAFICANDO LA PREDICION Y LOS TEST"

x_grid=np.arange(min(x_test),max(x_test),0.1)
x_grid=x_grid.reshape((len(x_grid),1))
plt.scatter(x_test,y_test)
plt.plot(x_grid,bar.predict(x_grid),color="green",linewidth=2)
plt.show

"presicion del algoritmo de bosque"
print(bar.score(x_train,y_train))
























