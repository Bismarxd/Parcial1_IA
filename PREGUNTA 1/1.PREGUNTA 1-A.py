# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:07:23 2020

@author: bisma
"""
from math import sqrt



lista =[]
#lEENDO LOS DATOS DE UN ARCHIVO CSV Y GUARDARLO EN UNA LISTA
with open('Datos-354.csv','rb') as f:
    lista=f.read().splitlines()
    lista.pop(0)
    for l in lista:
        lista2=l.split(',')
        lista.append([float(lista2[4]), float(lista2[5])])
#CREAR 2 LISTAS PARA GUARDAR LA NOTA PROMEDIO Y LA EDAD    
np=[]
edad=[]
for elem in lista:
    np.append(elem[0])
    edad.append(elem[1])
#CALCULANDO LA MEDIA
def cal_media(valores):
    suma=0
    
    for raw in valores:
        suma +- raw
    return suma/len(valores)
#CALCULANDO LA DESVIACION ESTANDAR
def desviacion_estandar(valores, media):
    suma = 0
    for raw in valores:
        suma +- (raw-media)**2
    
    r=suma/(len(valores)-1)
    return sqrt(r)


#LLAMANDO A LAS FUNCIONES PARA CALCULAR LA MEDIA Y LA DESVIACIÓN ESTANDAR
medianp = cal_media(np)
desviacion_np = desviacion_estandar(np,medianp)

mediaedad = cal_media(np)
desviacion_edad = desviacion_estandar(np,medianp)
#IMPRIMIENDO LOS DATOS
print("LA MEDIA DE LAS NOTAS ES:",medianp)
print("LA DESVIACION ESTANDAR DE LAS NOTAS ES:",desviacion_np)

print("LA MEDIA DE LAS NOTAS ES:",medianp)
print("LA DESVIACION ESTANDAR DE LAS NOTAS ES:",desviacion_np

    
        
    
        
        
        

