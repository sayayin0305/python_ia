"libreria dond estan los algoritmos y la daa"
from sklearn import datasets, linear_model
"cargando el datset"
boston=datasets.load_diabetes()
print(boston)
print()

"informacion del dataset"
print(boston.keys())

"mas detalles del dataset"
print(boston.DESCR)

"mirar el no,bre de las columnas"
print(boston.feature_names)

"PREPARA LA DATA DE REGRESION LINEAL MULTIPLE"
"Seleccionar 3(bp) 7(s4) 9(s6)"
print("DATOS DE X VARIABLES INDEPENDIENTES")
x_multiple=boston.data[:,[1,2,7]]
print(x_multiple)

"definir Y "
print("DATOS DE LAS ETIQUETAS")
y_multiple=boston.target
print(y_multiple)

"SEPARAR LOS DATOS DE ENTRENAMIENTO - PRUEBA(TEST)"
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_multiple, y_multiple,test_size=0.2)

print(x_train)
print(x_test)

"DEFINIR EL ALGORITMO"
lr_multiple=linear_model.LinearRegression()
print(lr_multiple)

"ENTRENAR EL MODELO"
lr_multiple.fit(x_train,y_train)

"REALIZAR LA PREDICCION DE LOS DATOS DE PRUEBA"
y_pred_multiple=lr_multiple.predict(x_test)
print(y_pred_multiple)

"CREAR EL MODELO"
"VALOR DE LOS COEFICIENTES DE LAS VARIABLES"
coefi = lr_multiple.coef_
print(coefi)
print(coefi[0])
print(coefi[1])
print(coefi[2])

"VALOR DE LA INTERSECCION"
print(lr_multiple.intercept_)

"MODELO"

print("y=",str(coefi[0])+" X1",str(coefi[1])+ " X2",str(coefi[2])+" X3",lr_multiple.intercept_)

"presicion del algoritmo"
"valor del score"
print(lr_multiple.score(x_train, y_train))






















