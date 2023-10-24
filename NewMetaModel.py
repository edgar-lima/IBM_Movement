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

ras= "D:\\HD\\Documents\\Edgar\\Doutorado\\IBM_movement\\LandScapes\\L1\\Land10_1.tif"
#ras= "C:\\Users\\Edgar\\Documents\\Python_Scripts\\PDI\\habin3.tif"
dr= 'C:/Users/Edgar/OneDrive - unb.br/IBM_Movement/'
dr + 'population2.xlsx'
teste= rasterio.open(ras)
land= teste
Scinnamomea= [7.5,0.5]# media e desvio padrao
Smaximiliani= [20.5,0.3]
Scaerulescens= [10.3,0.5]
c= [3.252,1.253]# parametros não lineares
ite=100 # numero de iterações

ma= pop(100, 2.5, 0.8, c,teste,dr)
ind= movement(ma,c,teste,"NOri")
land2[0,29,28]



def meta(nind, bs, bsd,eq,ite=100,dr):
  
  mpop= pop(nind,bs,bsd,eq,land,dr)
  land1= land
  land2= land1.read()

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
  #fsave(ind,tratm,trath)
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



####################################    
### Modulo de passeio orientado ###
######################################
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

###Teste pcalculo de kernel 
import numpy as np
from sklearn.neighbors import KernelDensity
dados= "C:\\Users\\Edgar\\OneDrive - unb.br\\IBM_Movement\\teste.xlsx"
dad = pd.read_excel(dados)
dad2= dad[dad["Ind"]==203]
knd= KernelDensity(bandwidth=0.05, kernel='gaussian')
tes= [[0.228639 ,0.940790],[0.381818,0.518182],[0.228639 ,0.940790],[0.381818,0.518182] ]


a=knd.fit(dad2[["Long","Lat"]])


# Criar uma grade de coordenadas para calcular a densidade de probabilidade
x_min, x_max = coordenadas[:, 0].min() - 0.1, coordenadas[:, 0].max() + 0.1
y_min, y_max = coordenadas[:, 1].min() - 0.1, coordenadas[:, 1].max() + 0.1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
grid_coords = np.c_[xx.ravel(), yy.ravel()]

# Calcular a estimativa de densidade de probabilidade para cada ponto na grade
densidade_probabilidade = np.exp(kde.score_samples(grid_coords))
densidade_probabilidade = densidade_probabilidade.reshape(xx.shape)

# Calcular o tamanho da área de vida como a área onde a densidade é maior que um limiar
limiar_densidade = 0.1  # Ajuste este valor conforme necessário
area_vida = np.sum(densidade_probabilidade > limiar_densidade) * (x_max - x_min) * (y_max - y_min) / np.prod(densidade_probabilidade.shape)

print("Tamanho da Área de Vida:", area_vida)


#Pacote para a geracao das paisagens
import pylandstats as pls
teste= nlmpy.randomClusterNN(100,100,p= 0.4)# p é a proporcao de desmatamento
teste= nlmpy.mpd(100,100,h= 0.30)
teste = nlmpy.classifyArray(teste, [0.4, 1-0.4])# [Hloos,Hremanescente]
show(teste)  

pai= pls.Landscape(teste, res= tuple([10,10]),neighborhood_rule= 4)

