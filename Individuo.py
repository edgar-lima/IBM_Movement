###Criando a classe individuo
# x: Lista contendo [especie,sexo,Massa,Lat,Long] 
# eqintake:
# eqtbm:
# eqhrs:

class Individuo():
    
    agente_id = 0

    def __init__(self, x,eq,land):
      
        Individuo.agente_id += 1   
           
        
        self.mass= x[0]
        self.coord= [[x[1],x[2]]]
        #self.intake= self.mass*eqintake[0]**eqintake[1]
        #self.tbm= self.mass*eqtbm[0]**eqtbm[1]
        self.hrs= (self.mass*eq[0]**eq[1])/11131 # 11131 é um metro em graus decimais
        self.id = Individuo.agente_id

    def __repr__(self):
        return f"{self.id}"
