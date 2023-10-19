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


bn2= bn.read()# abrindo o raster como uma matriz
bn2.min()# valor minimo
bn2.max()# valor maximo



##### Descrevendo como deve ser a movimentacao dos indiduos  #######################
##### de acordo com o modelo de movimento aleatorio do Paulo.#######################

# **OBS: Maneira de usar as coordenadas para extrair os indices**
bn.index(-47.76145,-13.93745)


### Distancia media percorrida em um dia em km pelo tamanho da celula.
resol= bn.res #Checar qual eh a resolucao (tamanho da celula) do mapa.
R= resol[0]*6.509/0.909 # multiplicar a resolucao pela divisao de 6.509/0.909.
# R= a distancia media que um individuo anda por dia, no circulo ele representa o raio.
# 6.509/0.909= distância média percorrida por dia em km dividido pelo tamanho da célula.

### Transformando a distancia media que o individuo percorre por dia em km para
### distancia media em graus decimais.
R1=6.509/110 #transformar km em graus decimais 
 
### EScolhendo ao acaso as localizacoes iniciais
ee= bn.bounds # Checando quais sao as coordenadas XYmin e XYmax do mapa.
X= ee[0]+(ee[2]-ee[0])*np.random.uniform(size= 1) # Selecionando ao acaso as localizacoes iniciais de X.
Y= ee[1]+(ee[3]-ee[1])*np.random.uniform(size= 1) # Selecionando ao acaso as localizacoes iniciais de X.

### EScolhendo sistematicamente as localizacoes iniciais.(**OBS: trabalhar nisso depois)
e = [X[0],Y[0]]
ee= teste.bounds

### Esse procedimentos sao necessarios para padronizar as coisas antes de comecar a
### movimentacao. OBS: Pensar como vai ser a melhor maneira de fazer isso. 

### Evitando que o individuo caia fora do mapa.

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



