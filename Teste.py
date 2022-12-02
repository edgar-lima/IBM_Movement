### Criacao dos individuos
import random as rd
import pandas as pd


dados= "C:\\Users\\Edgar\\OneDrive - unb.br\\Doutorado\\CapII\\Dados_analises\\Param.xlsx"
dad = pd.read_excel(dados)
dad.head()

rd.gauss(dad.iloc[0,1], dad.iloc[0,2])


class Agentes():
    
    agente_id = 0

    def __init__(self, x):
        cont= range(x.shape[0])
        i= rd.choice(cont)
        Agentes.agente_id += 1   
           
        self.sp= x.iloc[i,0]
        self.lifestage= "Adult"
        self.sex= rd.choice(["M","F"])
        self.mass= rd.gauss(x.iloc[i,1],x.iloc[i,2] )
        self.manuenergy= 0
        self.movienergy= 0
        self.repenergy= 0
        self.lat= 0
        self.long= 0
        self.inges= (self.mass * 10.7)**0.703
        self.tbm= (self.mass * 4.10)**0.751
        self.id = Agentes.agente_id

    def __repr__(self):
        return f"{self.id}"
        
        
a= Agentes(dad)

