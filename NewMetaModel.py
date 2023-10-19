### Loading libraries
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import numpy as np
from nlmpy import nlmpy
from rasterio.plot import show
import rasterio
from shapely.geometry import Point
from shapely.geometry import mapping
from shapely.geometry import shape
from rasterio.mask import mask
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
  land3= land2[0]
  ind= pop(100, 2.5, 0.8, c,teste,dr)
  k= 0

### Modulo de passeio aleatorio###  
# Modulo de checagem e movimentacao
  while(k<ite):
    
    lcheck= []
    #print(k)
# criando a lista de checagem a cada iteracao    
    for l in ind:
      lcheck.append(l.coord[-1])

# Checando a paisagem e a capacidade de suporte    
    for i in range(len(ind)):
      
      lc= land1.index(ind[i].coord[-1][0],ind[i].coord[-1][1])
      respEnvir= land2[0,lc[1], lc[0]]# linha x coluna
      #print(respEnvir)
      ocup= [i == ind[0].coord[-1] for i in lcheck]
      ocup2= sum(ocup)
      aleat= rd.choices([0,1],[0.8,0.1])[0]

      if respEnvir == 0:
        ind[i].move()
        lcheck[i]= ind[i].coord[-1]
      
      elif respEnvir==1 and ocup2 >=20*0.50:

          ind[i].move()
          lcheck[i]= ind[i].coord[-1] 
      
      elif respEnvir==1 and ocup2 <20*0.50 and aleat==1:
          ind[i].move()
          lcheck[i]= ind[i].coord[-1] 

      else:
        ind[i].coord.append([ind[i].coord[-1][0],ind[i].coord[-1][1]])
        lcheck[i]= ind[i].coord[-1]
 


      
    k+= 1
    px= []
    py= []
  
    for p in range(len(lcheck)):
      py.append(lcheck[p][1])
      px.append(lcheck[p][0])
    
    plt.figure(figsize= (15,15))
    show(land)
    plt.scatter(px,py, color= "red")
    plt.show()
    time.sleep(0.1)
    
### Modulo de passeio orientado ###
  k= 0
  while(k<ite):
    
    lcheck=[]

    for g in range(len(ind)):
      lcheck.append(ind[g].coord[-1])
      
# etapa de chacagem da paisagem e da acupação das celulas      
    for i in range(len(ind)):
      
      lc= land1.index(ind[i].coord[-1][0],ind[i].coord[-1][1])
      respEnvir= land2[0,lc[1],lc[0]]
      #print(lc)
      tx= []
      ty=[]
      
      for l in lcheck:
        tx.append(int(ind[i].coord[0][0] == l[0])) 
        ty.append(int(ind[i].coord[0][1] == l[1]))

      arx= np.array(tx)
      ary= np.array(ty)
      temp= arx+ary
      temp= np.where(temp>1,1,0)
      ocup= sum(temp)
      aleat= rd.choices([0,1],[0.9,0.1])[0]
      #print(k)

      if respEnvir == 0:
        ind[i].move()
        #lcheck[i]= ind[i].coord[-1]

      
      elif respEnvir==1 and ocup >=20*0.50:
        ind[i].move()
        #lcheck[i]= ind[i].coord[-1]

      elif respEnvir==1 and ocup <20*0.50 and aleat==1:
        ind[i].move()
        #lcheck[i]= ind[i].coord[-1]

      else:
        ind[i].coord.append([ind[i].coord[-1][0],ind[i].coord[-1][1]])
        #lcheck[i]= ind[i].coord[-1]

    k+=1
    px= []
    py= []
      
    for p in range(len(lcheck)):
      
      px.append(lcheck[p][0])
      py.append(lcheck[p][1])
        
    plt.figure(figsize= (8,8))
    show(land)
    plt.scatter(px,py, color= "red")
    plt.show()
    time.sleep(0.1)
    



 
 
# testes do metamodelo
ras= "C:\\Users\\Edgar\\Documents\\Python_Scripts\\PDI\\habin3.tif"
dr= 'C:/Users/Edgar/OneDrive - unb.br/IBM_Movement/'
dr + 'population2.xlsx'
teste= rasterio.open(ras)

c= [943.5,1.055]# parametros não lineares
are= [25,25]
land= teste
ite=1000

meta(10, 2.5, 0.8, c,are, 10, dr)

ind= pop(100, 2.5, 0.8, c,teste,dr)
ind= popM(1, 2.5, 0.8, c,teste,dr)

ind[0].coord
ind[0].train()
ind[0].Q

# método de como deletar as coordenadas e manter só a primeira
del ind[0].coord[1:len(ind[0].coord)]
trem= [1,2,3,4,5,6]
del trem[1:6]

#Pacote para a geracao das paisagens
import pylandstats as pls

teste= nlmpy.randomClusterNN(100,100,p= 0.4)# p é a proporcao de desmatamento
teste= nlmpy.mpd(100,100,h= 0.30)
teste = nlmpy.classifyArray(teste, [0.4, 1-0.4])# [Hloos,Hremanescente]
show(teste)  

pai= pls.Landscape(teste, res= tuple([10,10]),neighborhood_rule= 4)


