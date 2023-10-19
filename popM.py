
def popM(nind, bs, bsd,eq,land,dr):
  
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
  population2.to_excel(dr+'population2.xlsx')
  #return(population2)

# Criando a populacao (lista de objetos da classe Individuo)
  pop2= []
  
  for i in range(population2.shape[0]):
   
    pop2.append(IndMemory(population2.values[i,:],eq,land))
   
  return(pop2)
