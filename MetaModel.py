# Meta-model parameters:
# nind: Number of ind.viduals.
# bs: Mean body size.
# bsd: Standard deviation of body size.
# eq: Non-linear parameters of allometric equation [Y,B].
# ite: Number of iterections.
# dr: Directory to save results.

########################
####### Etapas de testes
########################
ras= "D:\\HD\\Documents\\Edgar\\Doutorado\\IBM_Movement\\LandScapes\\L1\\Land30_1.tif"
#ras= "C:\\Users\\Edgar\\Documents\\Python_Scripts\\PDI\\habin3.tif"
dr= 'C:/Users/Edgar/OneDrive - unb.br/IBM_Movement/'
dr + 'population2.xlsx'
land= rasterio.open(ras)
tes2= "D:HD/Documents/Edgar/Doutorado/IBM_Movement/LandScapes/L1/Land10_1.tif"
padrao= r"Land\d+"
re.findall(r"Land\d+", tes2)[0]

S_cinnamomea= [7.5,0.5]# media e desvio padrao (n= 2).
S_maximiliani= [20.5,0.3]# media e desvio padrao (n= 2).
S_caerulescens= [10.3,0.5]# media e desvio padrao (n= 6).
c= [3.252,1.253]# parametros não lineares
ite=100 # numero de iterações

ma= pop(1, 2.5, 0.8, c,land,dr)
ind= movement(ma,c,land,"NOri")
ind= movement(ma,c,land,"Memo")
ind[0].train()
ind[0].Q
i= ind[0]
del i.coord[1:len(i.coord)]



#############################################
################ Meta-modelo ################
#############################################
def meta(nind, bs, bsd,eq,ite=100,dr):

### Criando a população  
  mpop= pop(nind,bs,bsd,eq,land,dr)
  indNori= movement(mpop,eq,land,"NOri")
  indMemo= movement(mpop,eq,land,"Memo")
  
### Carregando as paisagens
# Será necessário criar um while para selecionar cada um dos tratamentos.
  land1= land.read()
  ind= indNori
  k= 0

###################################
### Modulo de passeio aleatorio####
###################################
# Modulo de checagem e movimentacao
  while(k<ite):
    
    lcheck= []

# criando a lista de checagem a cada iteracao    
    for l in ind:
      lcheck.append(l.coord[-1])

# Checando a paisagem e a capacidade de suporte    
    for i in range(len(ind)):
      
      lc= land.index(ind[i].coord[-1][0],ind[i].coord[-1][1])
      respEnvir= land1[0,lc[1], lc[0]]# linha x coluna
      ocup= [i == ind[0].coord[-1] for i in lcheck]
      ocup2= sum(ocup)
      aleat= rd.choices([0,1],[0.9,0.1])[0]

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
# Gráfico para a conferência do modelo  
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
fsave(ind,tratm,trath)
#######################################    
#### Modulo de passeio com memória ####
#######################################
  ind= indMemo
  k= 0
  while(k<ite):
    lcheck= []
    chlong=[]
    chlat=[]

    for g in range(len(ind)):
      lcheck.append(ind[g].coord[-1])
      trans= land.index(ind[g].coord[-1][0],ind[g].coord[-1][1])
      chlong.append(trans[0])
      chlat.append(trans[1])

#Checagem do estado atual dos indivíduos     
    for i in ind:
      lc= land.index(i.coord[-1][0],i.coord[-1][1])
      respEnvir= land1[0,lc[1],lc[0]]
      ocup= censo(chlong,chlat,lc)
      Eatual= i.avaliar_celula(respEnvir,ocup["censo"][0])
      aleat= rd.choices([0,1],[0.9,0.1])[0]

      ponto = Point(i.coord[-1][0],i.coord[-1][1])
      buff = ponto.buffer(i.hrs)
      rec, recorte = mask(land, [buff], crop=False)
      ocland= censo(chlong,chlat)
      Earredor= i.avaliar_arredor(rec, ocland)
      i.moveM(Eatual,Earredor,lc)
    k+= 1
# Gráfico para a conferência do modelo  
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
fsave(ind,tratm,trath)



