### Loading libraries
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import numpy as np
import re
from nlmpy import nlmpy
from rasterio.plot import show
import rasterio
from shapely.geometry import Point
from shapely.geometry import mapping
from shapely.geometry import shape
from rasterio.mask import mask
import time

######################################
### Function to build population table
######################################
# nind; Numero de individuos.
# bs: Tamanho corporal medio.
# bsd: Desvio padrao do tamanho corporal.
# eq: Parametros da equacao nao-linear para o calculo do tamanho do home range.
# land: paisagem.
# dr: Diretorio em que os dados serão salvos

def pop(nind, bs, bsd,eq,land,dr):
  
  population = []
  #res= (land.meta['transform'][4]+land.meta['transform'][4])/2
  #cellsize = res/111320# O denominador é o valor de um metro em graus decimais
  coords= coordconv(land)
  tam= coords.shape
  xyi= range(tam[0])
  
  cont1 = 0

# Criacao da matriz populacao    
  while (cont1 < nind):
    x= rd.choice(xyi)
    y= rd.choice(xyi)
    mass = rd.gauss(bs, bsd)
    #xi= rd.choice(xyi)# sorteia um indexador para tirar o valor da coordenada
    #yi= rd.choice(xyi)# sorteia um indexador para tirar o valor da coordenada
    lat= coords["Lat"][y]
    lon= coords["Long"][x]
    population.append([mass,lon, lat])
    cont1 += 1 
  
  population2= pd.DataFrame(population, columns= ["Massa", "Long", "Lat"])
  population2.to_excel(dr+'population.xlsx')
  return(population2)

########################################################
### Function to create individuals of each movement type
########################################################
def movement(x,eq,land,tmove="NOri"):
  pop2= []
  
  if tmove=="NOri":
    for i in range(x.shape[0]):
      pop2.append(IndNoriented(x.values[i,:],eq,land))
      
  elif tmove=="Ori":
    for i in range(x.shape[0]):
      pop2.append(IndOriented(x.values[i,:],eq,land))
      
  elif tmove=="Memo":
    for i in range(x.shape[0]):
      pop2.append(IndMemory(x.values[i,:],eq,land))
      
  else:
    print("Escolha um dos três tipos de movimentação")

  return(pop2)

##############################################
### Convert cell number to decimal coordenates
##############################################
# x: número da coluna.
# y: número da linha.
# conf: informaçoes sobre o transform do raster.

def convert(x,y, conf):

  ux= conf[2]
  uy= conf[5]
  resx= conf[0]
  resy= conf[4]
  newx= ux + x * resx
  newy= uy + y * resy

  return (newx,newy)

######################################################
### Function to select the coordenates for individuals
######################################################
def coordconv(raster):
  
  tabras= raster.read()
  resx= raster.meta['transform'][0]# resulucao colunas
  resy= raster.meta['transform'][4]# resulucao linhas
  ox= raster.meta['transform'][2]# coord canto superior direito
  oy= raster.meta['transform'][5]
  x= range(raster.meta["width"])
  y= range(raster.meta["height"])

  x1=[]
  y1=[]
  #print("funcionando")
  
  for i in range(len(x)):
    
    x1.append(ox + x[i] * resx)
    y1.append(oy + y[i] * resy) 
    
  
    
  coord0= pd.DataFrame({"Long":x1, "Lat":y1})
  return(coord0) 

#################################
### Fuction to save results table
#################################
# x: lista de individuos
# tratm: tratamento(tipo de movimento)
# trath: tratamento(quantidade de habitat)

def fsave(x,tratm,trath,dr):

  id= []
  long=[]
  lat= []
  ind= x
  for i in ind:
    for l in range(len(i.coord)):
      id.append(i)
      long.append(i.coord[l][0])
      lat.append(i.coord[l][1])
      
  dados= {"Ind":id, "Long":long, "Lat":lat}
  results= pd.DataFrame(dados) 
  results.to_excel(dr+tratm+f"{trath}.xlsx",index=False)

#######################################
### Função para fazer o censo da célula
#######################################
def censo(x,y,indcoor=None):
  spop= []
  
  if indcoor ==None:
    for xi,yi in zip(x,y):
      nid= sum([xi==x2 and yi==y2 for x2,y2 in zip(x,y)])
      spop.append(nid)

  else:
    nid= sum([indcoor[0]==x2 and indcoor[1]==y2 for x2,y2 in zip(x,y)])
    spop.append(nid)
    
    
  result= {"x":x, "y":y, "censo":spop} 
  return result
