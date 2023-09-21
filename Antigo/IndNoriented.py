###Criando o individuo não orientado
class IndNoriented(Individuo):
  
    def __init__(self,x, eqintake,eqtbm,eqhrs):
        Individuo.__init__(self,x, eqintake,eqtbm,eqhrs)
        print("criado")
        
    def move(self):
      
      # Turn angle
      teta= np.random.uniform(size= 1)*2*np.pi
      
      # X/Y coordinate (long,lat)
      xcoord= self.coord[-1][0]+self.hrs*np.cos(teta)
      ycoord= self.coord[-1][1]+self.hrs*np.sin(teta)
      self.coord.append([ycoord.tolist(),xcoord.tolist()])
      
      






 
