# Packages
import numpy as np
import rasterio as rasterio
import pandas as pd

## Argumentos
# Raster: Raster a ser transfomado.
# val: Valor que se quer retirar e converter a linhas e colunas para coord.


def coordconv(raster,val):
  
  tabras= raster.read()
  resx= raster.meta['transform'][0]# resulucao linhas
  resy= raster.meta['transform'][4]# resulucao colunas
  ox= raster.meta['transform'][2]# coord canto superior direito
  oy= raster.meta['transform'][5]
  
  check= np.where(tabras[0,:,:]==val)# Retira os valores iguais a val
  x= check[0][:].tolist()# Retirando as linhas e salvando numa lista
  y= check[1][:].tolist()# Retirando as colunas e salvando numa lista
  x1=[]
  y1=[]
  print("funcionando")
  
  for i in range(len(x)):
    
    x1.append(ox + x[i] * resx)
    y1.append(oy + y[i] * resy) 
    
  
    
  coord0= pd.DataFrame({"Long":x1, "Lat":y1})
  return(coord0) 
    
    
    
    
