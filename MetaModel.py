###Liberando pacotes
import pandas as pd
import random as rd
import numpy as np

# x: DataFrame contendo [especie,sexo,massa]
# eqintake:
# eqtbm:
# eqhrs:
# n0: Tamanho da população inicial
# are: Lista indicando o tamanho da paisagem [lin,col]
# pland: Proporcao de habitat na paisagem
# ite: Número de iteracoes

def MetaModel(x,eqintake, eqtbm,eqhrs, n0, are, pland, ite=999):
  
### Criando a matriz de comunidade
  Community= []
  cont1= 0
  
  while (cont1 < n0):
    nsp= range(x.shape[0])
    i_sp= rd.choice(nsp)
    C_sp= x.iloc[i_sp,0]
    C_sex= rd.choice(["M","F"])
    C_mass= rd.gauss(x.iloc[i_sp,1],x.iloc[i_sp,2])
    lat= rd.choice(range(are[0]))
    lon= rd.choice(range(are[1]))
    Community.append([C_sp,C_sex,C_mass,lat,lon])
    cont1 += 1 
  
### Criando DataFrame com os parametros utilizados.
  df_commu= pd.DataFrame(Community, columns= ["Sp", "Sex", "Mass", "lat", "long"])

### Criando a paisagem


## Teste
a1= ["Anisognathus igniventris","F",33,-0.5023,0.800]
col= ["Sp", "Sex", "Mass", "lat", "long"]
a= pd.DataFrame(a1,columns= col)
