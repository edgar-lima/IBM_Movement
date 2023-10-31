# Meta-model parameters:
# nind: Number of ind.viduals.
# bs: Mean body size.
# bsd: Standard deviation of body size.
# eq: Non-linear parameters of allometric equation [Y,B].
# ite: Number of iterections.
# land: A list with path and name of rasters.
# dr: Directory to save results.
# plotmap
# As porcentagens representam a perda de hahabitat e não a quantidade
# de habitat disponível
ras= ["D:HD/Documents/Edgar/Doutorado/IBM_Movement/LandScapes/L1/Land80_1.tif"]
c= [3.252,1.253]# parametros não lineares
S_cinnamomea= [7.5,0.5]# media e desvio padrao (n= 2).
S_maximiliani= [20.5,0.3]# media e desvio padrao (n= 2).
S_caerulescens= [10.3,0.5]# media e desvio padrao (n= 6).
ite=50 # numero de iterações
dr= 'C:/Users/Edgar/OneDrive - unb.br/IBM_Movement/'

MetaModel(10,20.5,0.8,c,ite,ras,dr,True)

def MetaModel(nind, bs,bsd,eq,ite,lands,dr, plotmap= False):
  lsc= rasterio.open(lands[0])
  tabpop= pop(nind,bs,bsd,eq,lsc,dr)

  for i in lands:
    land= rasterio.open(i)
    land1= land.read()
    indNori= movement(tabpop,eq,land,"NOri")
    indMemo= movement(tabpop,eq,land,"Memo")
    trath= re.findall(r"Land\d+", i)[0]
    k= 0
    
    for i in indMemo:
      i.train()
      del i.coord[1:len(i.coord)]
##############################      
### Unoriented model movement.
##############################
    while k< ite:
      lcheck= []
      #print("Entrei no modelo")
      
# creating the checklist for each iteration.      
      for l in indNori:
        lcheck.append(l.coord[-1])
        
# Checando a paisagem e a capacidade de suporte    
      for i in range(len(indNori)):
        lc= land.index(indNori[i].coord[-1][0],indNori[i].coord[-1][1])
        respEnvir= land1[0,lc[1], lc[0]]# row x column
        ocup= [i == indNori[0].coord[-1] for i in lcheck]
        ocup2= sum(ocup)
        aleat= rd.choices([0,1],[0.9,0.1])[0]
        #print(respEnvir)

        if respEnvir == 0:
          indNori[i].move()
          
        elif respEnvir==1 and ocup2 <20*0.5 and aleat==1:
            indNori[i].move()
            #lcheck[i]= indNori[i].coord[-1] 
            
        elif respEnvir == 1 and ocup2 < 20*0.5:
          indNori[i].coord.append([indNori[i].coord[-1][0],indNori[i].coord[-1][1]])

        elif respEnvir==1 and ocup2 >=20*0.5:
            indNori[i].move()
            #lcheck[i]= indNori[i].coord[-1] 
        

            
 Plot map with individuals moving.
        if plotmap == True:
          px= []
          py= []
       
          for p in range(len(lcheck)):
            py.append(lcheck[p][1])
            px.append(lcheck[p][0])
          
          plt.figure(figsize= (15,15))
          show(land)
          plt.scatter(px,py, color= "red")
          plt.show()
          time.sleep(0.005)
          
      k+= 1
    fsave(indNori,"Unoriented",trath,dr)
#######################
### Memory-based model.
#######################
    k=0
    while k<ite:
      lcheck= []
      chlong=[]
      chlat=[]
  
      for g in range(len(indMemo)):
        lcheck.append(indMemo[g].coord[-1])
        trans= land.index(indMemo[g].coord[-1][0],indMemo[g].coord[-1][1])
        chlong.append(trans[0])
        chlat.append(trans[1])
  
#Checagem do estado atual dos indivíduos     
      for i in indMemo:
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

        if plotmap == True:
          px= []
          py= []
       
          for p in range(len(lcheck)):
            py.append(lcheck[p][1])
            px.append(lcheck[p][0])
          
          plt.figure(figsize= (15,15))
          show(land)
          plt.scatter(px,py, color= "red")
          plt.show()
          time.sleep(0.05)

      k+= 1
    fsave(indMemo,"Memory",trath,dr)


    
    
    
    
