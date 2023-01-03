### Criacao dos individuos
import random as rd
import pandas as pd


dados= "C:\\Users\\Edgar\\OneDrive - unb.br\\Doutorado\\CapII\\Dados_analises\\Param.xlsx"
dad = pd.read_excel(dados)
dad.head()

rd.gauss(dad.iloc[0,1], dad.iloc[0,2])


class Agentes():
    
    agente_id = 0

    def __init__(self, x):
        cont= range(x.shape[0])
        i= rd.choice(cont)
        Agentes.agente_id += 1   
           
        self.sp= x.iloc[i,0]
        self.lifestage= "Adult"
        self.sex= rd.choice(["M","F"])
        self.mass= rd.gauss(x.iloc[i,1],x.iloc[i,2] )
        self.manuenergy= 0
        self.movienergy= 0
        self.repenergy= 0
        self.lat= 0
        self.long= 0
        self.inges= (self.mass * 10.7)**0.703
        self.tbm= (self.mass * 4.10)**0.751
        self.id = Agentes.agente_id

    def __repr__(self):
        return f"{self.id}"
        
        
a= Agentes(dad)


##### testes raster
import numpy as np
import rasterio as rasterio
import matplotlib.pyplot as plt
import rasterio.plot as show
import os

path= 'C:\\Users\\Edgar\\Documents\\Python_Scripts\\PDI\\BANQ.tif'

bn= rasterio.open(path)# carregando
bn.meta# mostrando metadados
lg= bn.width
lt= bn.height

bn.

bn2= bn.read()# abrindo o raster como uma matriz
bn2.min()# valor minimo
bn2.max()# valor maximo

# testando idexacao
a= np.array([3, 4])
b= np.array([[3, 4], [9, 7]])
c= np.array([[[3, 4], [9, 7]]])

bn2[0,lt-1,lg-1]# Sequencia de linha x coluna (lat long)

# Teste para checagem do raster
a=[rd.choice(range(lt)), rd.choice(range(lg))]
a
bn2[0,a[0],a[1]]

# Testando rastreamento das coordenadas
d= [1,2]
e= [[1,2],[3,4]]
e.append([50,60])

# idexacao da lista 
e[2]
e[2][0]# lat
e[2][1]# long
e.
