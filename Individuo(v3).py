###Liberando pacotes
import pandas as pd

###Criando a classe individuo
# x: Lista contendo [especie,sexo,Massa,Lat,Long] 
# eqintake:
# eqtbm:
# eqhrs:

class Individuo():
    
    agente_id = 0

    def __init__(self, x,eqintake,eqtbm,eqhrs):
      
        Individuo.agente_id += 1   
           
        self.sp= x[0]
        self.lifestage= "Adult"
        self.sex= x[1]
        self.mass= x[2]
        self.manuenergy= 0
        self.movienergy= 0
        self.repenergy= 0
        self.coord= [[x[3],x[4]]]
        self.intake= self.mass*eqintake[0]**eqintake[1]
        self.tbm= self.mass*eqtbm[0]**eqtbm[1]
        self.hrs= self.mass*eqhrs[0]**eqhrs[1]
        self.id = Individuo.agente_id

    def __repr__(self):
        return f"{self.id}"
    
    def E_Allocation(self):
      pass


### Fazendo testes de criacao do individuo
a= [10.7,0.703]
b= [0.044, 0.634]
c= [943.5,1.055]

dad2= [dad.iloc[1,0], dad.iloc[1,1],dad.iloc[1,2]]
dad3= [dad.iloc[1,0], "F",dad.iloc[1,1], -0.5023,0.800]
ag= Individuo(dad3,a,b,c)

ag
## Fazendo teste com individuo não orientado 
ag2= IndNoriented(dad3, a,b,c)

### Fazendo testes da checagem da celula
a.coord[-1]
lat= a.coord[-1][0]
lon= a.coord[-1][1]
bn2[0,lat,lon]
