class IndMemory(Individuo):
      
      def __init__(self, x,eq,land):
          Individuo.__init__(self, x,eq,land)
          self.percep= self.hrs/2
          self.land= land
          self.xmax= self.land.meta["width"]
          self.ymax= self.land.meta["height"]
          self.Q= np.zeros((3,3))
          self.recomp= {0:-2, 1:7, 2:10}
          
      def movetrain(self):
        teta= np.random.uniform(size= 1)*2*np.pi
        raio= rd.uniform(1,self.hrs)
        xcoord= self.coord[-1][0]+raio*np.cos(teta)
        ycoord= self.coord[-1][1]+raio*np.sin(teta)
        check= self.land.index(xcoord[0],ycoord[0])
            
        if 0>check[0] or check[0]>= self.xmax or 0>check[1] or check[1] >= self.ymax:
          self.coord.append([self.coord[-1][0],self.coord[-1][1]])
    
        else:
          self.coord.append([xcoord[0],ycoord[0]])
              
      def avaliar_celula(self, celula, ocup):
        
        if celula == 0:
          return 0 # Não habitat
            
        elif celula == 1 and ocup>=20*0.5:
          return 1 # habitat acima da metade de k.
            
        else:
          return 2 # habitat abaixo de k.
            
      def avaliar_arredor(self, raster, cen):
        x1= cen["x"]
        y1= cen["y"]
        result= cen
        estado= []
          
        for i in range(len(x1)):
          cel= raster[0,y1[i],x1[i]]
          estado.append(self.avaliar_celula(cel,cen["censo"][i]))
              
        result["Estado"]= estado
        return result
          
      def train(self):
        alpha= 0.1 # Taxa de aprendizado
        gamma= 0.9 # Fator de desconto
        epi= 355 # Número de episódios de treinamento
        epsilon= 0.1 # Probabilidade de acao aleatoria
        land1= self.land.read()
        ocup=[1,100]
        cont= 0
    
        while cont<epi:
          x0,y0= self.land.index(self.coord[-1][0],self.coord[-1][1])  
          self.movetrain()
          x1,y1= self.land.index(self.coord[-1][0],self.coord[-1][1])
          value0= land1[0,y0,x0] # Valor da celula onde estava
          value1= land1[0,y1,x1] # Valor da celula para onde foi
              
          #Avalia o estadado de onde está e para onde foi
          state0= self.avaliar_celula(value0,rd.choice(ocup))
          state1= self.avaliar_celula(value1,rd.choice(ocup))
          
          #Faz o calculo para atualizar a tabela Q
          recompensa= self.recomp[state1]
          self.Q[state0,state1]= self.Q[state0,state1] + alpha * (recompensa + gamma * np.max(self.Q[state1,:])- self.Q[state0,state1])
          cont += 1
          
      def moveM(self,eatual,earredor,catual):
        e= 0.1
        ale= rd.uniform(0,1)
        ale2= rd.uniform(0,1)
        #rmax= np.argmax(Q[eatual]) # Qual ação dá a melhor recompensa
        estmax_disp= np.max(list(set(earredor["Estado"])))
        tes= np.where(earredor["Estado"]==estmax_disp)[0].tolist()
        X= [earredor["x"][indice] for indice in tes]
        Y= [earredor["y"][indice] for indice in tes]
        
        if eatual < estmax_disp and estmax_disp !=0: # estado atual é pior que os estados disponíveis?
          if len(X)>1 and ale>e: #escolhendo a célula de melhor estado mais próxima
            distx= abs(catual[0]- np.array(X))
            disty= abs(catual[1]- np.array(Y))
            euc_dist= (distx+disty)/2
            idfut= np.argmin(euc_dist)
            nova_coord= convert(X[idfut],Y[idfut],self.land.meta["transform"][:])
            self.coord.append([nova_coord[0],nova_coord[1]])

          elif len(X)>1 and ale<=e: # escolha aleatória da célula com melhor estado.
            idfut= rd.sample(range(len(X)),1)[0]
            nova_coord= convert(X[idfut],Y[idfut],self.land.meta["transform"][:])
            self.coord.append([nova_coord[0],nova_coord[1]])
            
          else:# Há apenas uma célula com o melhor estado
            nova_coord= convert(X[0],Y[0],self.land.meta["transform"][:])
            self.coord.append([nova_coord[0],nova_coord[1]])
            
        elif eatual == estmax_disp and estmax_disp == 0:
          if len(X)>1 and ale>e: #escolhendo a célula de melhor estado mais próxima
            distx= abs(catual[0]- np.array(X))
            disty= abs(catual[1]- np.array(Y))
            euc_dist= (distx+disty)/2
            idfut= np.argmax(euc_dist)
            nova_coord= convert(X[idfut],Y[idfut],self.land.meta["transform"][:])
            self.coord.append([nova_coord[0],nova_coord[1]])
            
          elif len(X)>1 and ale<=e: # escolha aleatória da célula com melhor estado.
            idfut= rd.sample(range(len(X)),1)[0]
            nova_coord= convert(X[idfut],Y[idfut],self.land.meta["transform"][:])
            self.coord.append([nova_coord[0],nova_coord[1]])
            
        elif eatual >= estmax_disp and ale2<e:
          self.coord.append([self.coord[-1][0],self.coord[-1][1]])

        elif eatual >= estmax_disp and ale2>e:
          if len(X)>1 and ale>e: #escolhendo a célula de melhor estado mais próxima
            distx= abs(catual[0]- np.array(X))
            disty= abs(catual[1]- np.array(Y))
            euc_dist= (distx+disty)/2
            idfut= np.argmin(euc_dist)
            nova_coord= convert(X[idfut],Y[idfut],self.land.meta["transform"][:])
            self.coord.append([nova_coord[0],nova_coord[1]])

          elif len(X)>1 and ale<=e: # escolha aleatória da célula com melhor estado.
            idfut= rd.sample(range(len(X)),1)[0]
            nova_coord= convert(X[idfut],Y[idfut],self.land.meta["transform"][:])
            self.coord.append([nova_coord[0],nova_coord[1]])
            
          else:# Há apenas uma célula com o melhor estado
            nova_coord= convert(X[0],Y[0],self.land.meta["transform"][:])
            self.coord.append([nova_coord[0],nova_coord[1]])

        else:
          self.coord.append([self.coord[-1][0],self.coord[-1][1]])

