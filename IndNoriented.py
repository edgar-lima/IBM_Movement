###Criando o individuo nao orientado

class IndNoriented(Individuo):
  
    def __init__(self,x,eq,land):
        Individuo.__init__(self,x,eq, land)
        self.land= land
        self.xmax= self.land.meta["width"]
        self.ymax= self.land.meta["height"]
        
    def move(self):
      # Turn angle
      teta= np.random.uniform(size= 1)*2*np.pi
      raio= self.hrs
      xcoord= self.coord[-1][0]+raio*np.cos(teta)
      ycoord= self.coord[-1][1]+raio*np.sin(teta)
      check= self.land.index(xcoord[0],ycoord[0])

      if 0>check[0] or check[0]>= self.xmax or 0>check[1] or check[1] >= self.ymax:
        self.coord.append([self.coord[-1][0],self.coord[-1][1]])

      else:
        self.coord.append([xcoord[0],ycoord[0]])
