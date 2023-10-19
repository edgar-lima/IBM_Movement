###Liberando pacotes
import pandas as pd
import numpy as np

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
        self.hrs= (self.mass*eq[0]**eq[1])/111320
        self.id = Individuo.agente_id

    def __repr__(self):
        return f"{self.id}"



### Fazendo testes de criacao do individuo
a= [10.7,0.703]
b= [0.044, 0.634]
c= [943.5,1.055]

dad2= [dad.iloc[1,0], dad.iloc[1,1],dad.iloc[1,2]]
dad3= [dad.iloc[1,0], "F",dad.iloc[1,1], -0.5023,0.800]
ag= Individuo(dad3,a,b,c)

ag
## Fazendo teste com individuo nao orientado 
ag2= IndNoriented(dad3, a,b,c)




