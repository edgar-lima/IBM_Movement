### Loading libraries
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import numpy as np
from nlmpy import nlmpy
from rasterio.plot import show
import rasterio
import time

# Model parameters:

# nind; Numero de individuos.
# bs: Tamanho corporal medio.
# bsd: Desvio padrao do tamanho corporal.
# eq: Parametros da equacao nao-linear para o calculo do tamanho do home range.
# land: Paisagem já criada.
# aresta: Tamanho da paisagem.
# Ha: Quantidade de habitat na paisagem.
# res: Tamanho do pixel.
# ite: Numero de iteracoes.
# dr: Diretorio em que os dados serão salvos



def meta(nind, bs, bsd,eq, land= None,are= None,res= None, ite= None,dr):
  
  land1= land
  land2= land1.read()
  k= 0
  
### Modulo de passeio aleatorio###  
# Modulo de checagem e movimentacao
  while(k<ite):
    
    lcheck= []
    print(k)
# criando a lista de checagem a cada iteracao    
    for l in ind:
      lcheck.append(l.coord[-1])
      
# Checando a paisagem e a capacidade de suporte    
    for i in range(len(ind)):
      
      lc= land1.index(ind[i].coord[-1][0],ind[i].coord[-1][1])
      respEnvir= land2[0,lc[0], lc[1]]
      #print(respEnvir)
     
      if respEnvir==1:
      
        ocup= [i == ind[0].coord[-1] for i in lcheck]
        ocup2= sum(ocup)
      
        if ocup2 >=20*0.80:
          ind[i].move()
          lcheck[i]= ind[i].coord[-1]
      
      else:
        ind[i].move()
        lcheck[i]= ind[i].coord[-1]
      
    k+= 1
    px= []
    py= []
  
    for p in range(len(lcheck)):
      px.append(lcheck[p][0])
      py.append(lcheck[p][1])
    
    plt.figure(figsize= (8,8))
    show(land)
    plt.scatter(px,py, color= "red")
    plt.show()
    time.sleep(1)


    


### Modulo de passeio orientado###   
  

# testes do metamodelo
ras= "C:\\Users\\Edgar\\Documents\\Python_Scripts\\PDI\\habin2.tif"
dr= 'C:/Users/Edgar/OneDrive - unb.br/IBM_Movement/'
dr + 'population2.xlsx'
teste= rasterio.open(ras)

c= [943.5,1.055]# parametros não lineares
are= [25,25]
land= teste
ite= 10

meta(10, 2.5, 0.8, c,are, 10, dr)
ind= pop(10, 2.5, 0.8, c,teste,dr)

px= []
py= []
for p in range(len(lcheck)):
  px.append(lcheck[p][0])
  py.append(lcheck[p][1]) 

#teste com mapa 
plt.figure(figsize= (8,8))
show(land)
plt.scatter(px,py, color= "red")
plt.show()


#Pacote para a geracao das paisagens
import pylandstats as pls

teste= nlmpy.randomClusterNN(100,100,p= 0.4)# p é a proporcao de desmatamento
teste= nlmpy.mpd(100,100,h= 0.30)
teste = nlmpy.classifyArray(teste, [0.4, 1-0.4])# [Hloos,Hremanescente]
show(teste)  

pai= pls.Landscape(teste, res= tuple([10,10]),neighborhood_rule= 4)


