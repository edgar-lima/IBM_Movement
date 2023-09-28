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
    time.sleep(0.25)
    
### Modulo de passeio orientado ###
  k= 0
  while(k<ite):
    
    lcheck=[]

    for l in range(len(ind)):
      
      lcheck.append(ind[l].coord[-1])
      
    for i in range(len(ind)):
      
      lc= land1.index(ind[i].coord[-1][0],ind[i].coord[-1][1])
      respEnvir= land2[0,lc[0],lc[1]]
        
      ocup= [v == ind[0].coord[-1] for v in lcheck]
      ocup2= sum(ocup)
        
      if respEnvir == 1 and ocup2 >= 20*0.80:
        
        raio= ind[i].percep
        ponto= Point(ind[i].coord[-1][0],ind[i].coord[-1][1])
        buff= ponto.buffer(raio)
        rec, recorte= mask(land1, [buff],crop= True)
        out_meta= land1.meta
          
        dest= np.where(rec[0,:,:]==1)
        ent= len(dest[0][:].tolist())
        
        if ent != 0:
          
          sel= rd.choice(range(ent))
          rx= dest[0][sel].tolist()
          ry= dest[1][sel].tolist()
          ux= out_meta["transform"][2]
          uy= out_meta["transform"][5]
          resx= out_meta["transform"][0]
          resy= out_meta["transform"][4]
          newx= ux + rx * resx
          newy= uy + ry * resy
            
          ind[i].coord.append([newx,newy])
          lcheck[i]= ind[i].coord[-1]
          
        else:
          
          ind[i].move()
          lcheck[i]= ind[i].coord[-1]
        
      else:
        
        raio= ind[i].percep
        ponto= Point(ind[i].coord[-1][0],ind[i].coord[-1][1])
        buff= ponto.buffer(raio)
        rec, recorte= mask(land1, [buff],crop= True)
        out_meta= land1.meta
          
        dest= np.where(rec[0,:,:]==1)
        ent= len(dest[0][:].tolist())
        
        if ent != 0:
          
          sel= rd.choice(range(ent))
          rx= dest[0][sel].tolist()
          ry= dest[1][sel].tolist()
          ux= out_meta["transform"][2]
          uy= out_meta["transform"][5]
          resx= out_meta["transform"][0]
          resy= out_meta["transform"][4]
          newx= ux + rx * resx
          newy= uy + ry * resy
            
          ind[i].coord.append([newx,newy])
          lcheck[i]= ind[i].coord[-1]
          
        else:
          
          ind[i].move()
          lcheck[i]= ind[i].coord[-1]

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
      time.sleep(1)
    

 
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

ind= pop(25, 2.5, 0.8, c,teste,dr)

### Construindo o individuo que movimenta com memoria




### Depois checar se o ind sai da paisagem
caboco= 0
land1.index(ind[caboco].coord[-1][0],ind[caboco].coord[-1][1])
caboco+=1
land1.meta
######

#Pacote para a geracao das paisagens
import pylandstats as pls

teste= nlmpy.randomClusterNN(100,100,p= 0.4)# p é a proporcao de desmatamento
teste= nlmpy.mpd(100,100,h= 0.30)
teste = nlmpy.classifyArray(teste, [0.4, 1-0.4])# [Hloos,Hremanescente]
show(teste)  

pai= pls.Landscape(teste, res= tuple([10,10]),neighborhood_rule= 4)


