## Criando individuo com memoria

class IndMemory(Individuo):
      
      def __init__(self, x,eq,land):
        
          IndNoriented.__init__(self, x,eq,land)
          self.percep= self.hrs/2
          self.land= land
          self.xmax= self.land.meta["width"]
          self.ymax= self.land.meta["height"]
          self.Q= np.zeros((3,3))
          self.recomp= {1:-2, 2:10, 3:7}

      
      def movetrain(self):
        
        teta= np.random.uniform(size= 1)*2*np.pi
        xcoord= self.coord[-1][0]+self.hrs*np.cos(teta)
        ycoord= self.coord[-1][1]+self.hrs*np.sin(teta)
        check= self.land.index(xcoord[0],ycoord[0])

        if 0>check[0] or check[0]>= self.xmax or 0>check[1] or check[1] >= self.ymax:
          self.coord.append([self.coord[-1][0],self.coord[-1][1]])


        else:
          self.coord.append([xcoord[0],ycoord[0]])

      
      
      def train (self):
          alpha = 0.1 # Taxa de aprendizado
          gamma = 0.9 # Fator de desconto
          episodios = 1000 # Número de episódios de treinamento
          epsilon= 0.1 # Probabilidade de acao aleatoria
          land1= land.read()
          ocup= [5,15]
          cont= 0
          
          while cont<episodios:
            
            x0,y0= land.index(self.coord[-1][0],self.coord[-1][1])  
            self.movetrain()
            x1,y1= land.index(self.coord[-1][0],self.coord[-1][1])
            value0= land1[0,y0,x0] # Valor da celula onde estava
            value1= land1[0,y1,x1] # Valor da celula para onde foi
            state0= [] # Estado atual
            state1= [] # Estado futuro
            idx= []
            ocup2= rd.choice(ocup)
                
    # Checando o estado atual
            if value0 == 0:
              state0 =1
    
            elif value0==1 and ocup2 <20*0.50:
              state0=2
    
            elif value0==1 and ocup2 >=20*0.50:
              state0=3
    
    #checando a acao para o estado futuro
            if value1==0:
              state1=1
    
            elif value1==1 and ocup2 <20*0.50:
              state1=2
    
            elif value1==1 and ocup2 >=20*0.50:
              state1=3
    #Calculando estado acao (estado onde estou e para que estado onde eu vou)
            if state0==1 and state1==1:# Zero para zero
              idx= [0,0]
    
            elif state0==1 and state1==2:# Zero para 1 abaixo de 80% de K
              idx= [0,1]
                
            elif state0==1 and state1==3:# Zero para 1 acimaabaixo de 80% de K
              idx= [0,2]
                
            elif state0==2 and state1==1:
              idx= [1,0]
                
            elif state0==2 and state1==2:
              idx= [1,1]
                
            elif state0==2 and state1==3:
              idx= [1,2]
                
            elif state0==3 and state1==1:
              idx=[2,0]
                
            elif state0==3 and state1==2:
              idx= [2,1]
                
            elif state0==3 and state1==3:
              idx= [2,2]
                
            recompensa= self.recomp[state1]
            self.Q[idx[0],idx[1]]= self.Q[idx[0],idx[1]] + alpha * (recompensa + gamma * np.max(self.Q[idx[1],:])- self.Q[idx[0],idx[1]])
            cont += 1

        def action (self):
