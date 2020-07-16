# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:43:34 2020

@author: bisma
"""

import pandas as pd
import numpy as np

datos=pd.read_csv('Datos-354.csv')
df=pd.DataFrame(datos)

#HALLAR LA MEDIA
mediaN = df['nota promedio'].mean()
mediae = df['edad'].mean()
print('LA MEDIA DE LA NOTAS ES:',mediaN)
print('LA MEDIA DE LA EDAD ES:',mediae)

#HALLAR LA MEDIANA
medianan = df['nota promedio'].median()
medianae = df['edad'].median()
print('LA MEDIANA DE LA NOTAS ES:',medianan)
print('LA MEDIANA DE LA EDAD ES:',medianae)

#HALLAR LA DESVIACIÓN ESTANDAR
den = df['nota promedio'].std()
dee = df['edad'].std()
#IMPRIMIENDO LOS DATOS
print('LA DESVIACIÓN ESTANDAR DE LAS NOTAS ES:',den)
print('LA DESVIACIÓN ESTANDAR DE LAS EDAD ES:',dee)