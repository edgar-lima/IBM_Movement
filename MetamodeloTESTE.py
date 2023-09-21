import pandas as pd
import random as rd
import numpy as np

import rasterio as rasterio
import os

import matplotlib.pyplot as plt
from rasterio.plot import show

######### Teste

# Carregando os dados do individuo
ed= "C:\\Users\\Edgar\\OneDrive - unb.br\\IBM_Movement\\DadosTeste.xlsx"
dad= pd.read_excel(ed)
print(dad)

dad2= ["Acanthorhynchus tenuirostris","F",9.7,x,y]

# Criando array (paisagem)
  pai= np.array([[[0,0,0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0],
[1,1,1,0,0,0,0,1,1,0],
[1,1,1,0,0,0,0,1,1,0],
[1,1,0,0,0,0,0,0,0,0],
[0,0,0,1,1,1,0,0,0,0],
[0,0,0,1,1,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,0],
[0,0,0,0,0,0,0,1,1,0],]])

# Metamodelo de teste

def meta(ind,land,ite):
  
  cont= 0
  
  while(cont<ite):
      # Checando o ambiente
    respEnvir= land[ind.coord[-1][0], ind.coord[-1][1]]
    print(respEnvir)
      # Caminhando
    ind.move()
    print(ind.coord)
    cont+=1

# Tentativa
x2= ind.coord[-1][0]
y2= ind.coord[-1][1]

land.meta

j, i = gw.coords_to_indices(x2,y2,src)
data = src[:,i,j].data.compute()
respEnvir=data.flatten()[0]

ind.move()
print(ind.coord)

### Testes de trabalho com raster
import geowombat as gw
import rasterio as rasterio
from rasterio.windows import Window
import matplotlib.pyplot as plt
from rasterio.plot import show

ras= "C:\\Users\\Edgar\\Documents\\Python_Scripts\\PDI\\habin.tif"

ras2= "C:\\Users\\Edgar\\Dropbox\\Aula_Modelos\\habnovo.tif"

x,y = -48.953 ,-15.049


teste= rasterio.open(ras)
teste2= rasterio.open(ras2)
show(teste)
show(teste2)
teste2.res

teste.index(x,y)
teste.meta

## Outra forma de retirar os valores das celulas usando as coordenadas
with gw.open(ras) as src:
  j, i = gw.coords_to_indices(x, y, src)
  data = src[0,i,j].data.compute()
  
print(data.flatten())

dad.iloc[:,2]




