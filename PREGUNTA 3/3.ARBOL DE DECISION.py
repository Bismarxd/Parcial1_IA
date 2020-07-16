# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:28:24 2020

@author: bisma
"""

import pandas as pd

#CARGAR EL CSV
dataset = pd.read_csv('Datos-354.csv')
x = dataset.iloc[:,[4,5]].values
y = dataset.iloc[:,6].values

#DIVIDIMOS EL CONJUNTO DE DATOS EN CONJUNTO DE ENTRENAMIENTO Y CONJUNTO DE PRUEBAS
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=0)

#ESTANDARIZAMOS DE ESCALAS
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


#REGRESIÓN LOGISTICA Y ENTRENAMIENTO DEL MODELO
from sklearn.linear_model import LogisticRegression
clasificador = LogisticRegression(random_state = 0)
clasificador.fit(x_train, y_train)

#PREDICCIONES DEL CONJUNTO DE PRUEBAS
y_pred = clasificador.predict(x_test)

#MATRIZ DE CONFUSION
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

score = clasificador.score(x_test, y_test)



#########ARBOL DE DECISION###########
from sklearn.tree import DecisionTreeClassifier
clasificador2 = DecisionTreeClassifier(criterion = 'entropy', random_state= 0)
clasificador2.fit(x_train, y_train)

y_pred_tree = clasificador2.predict(x_test) 
cm2 = confusion_matrix(y_test, y_pred_tree)

score2 = clasificador2.score(x_test, y_test)



















