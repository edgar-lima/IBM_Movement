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

##### testes raster
import numpy as np
import rasterio as rasterio
import matplotlib.pyplot as plt
import rasterio.plot as show
import os

path= 'C:\\Users\\Edgar\\Documents\\Python_Scripts\\PDI\\BANQ.tif'

bn= rasterio.open(path)# carregando
bn.meta# mostrando metadados
lg= bn.width
lt= bn.height


bn2= bn.read()# abrindo o raster como uma matriz
bn2.min()# valor minimo
bn2.max()# valor maximo



##### Descrevendo como deve ser a movimentacao dos indiduos  #######################
##### de acordo com o modelo de movimento aleatorio do Paulo.#######################

# **OBS: Maneira de usar as coordenadas para extrair os indices**
bn.index(-47.76145,-13.93745)


### Distancia media percorrida em um dia em km pelo tamanho da celula.
resol= bn.res #Checar qual eh a resolucao (tamanho da celula) do mapa.
R= resol[0]*6.509/0.909 # multiplicar a resolucao pela divisao de 6.509/0.909.
# R= a distancia media que um individuo anda por dia, no circulo ele representa o raio.
# 6.509/0.909= distância média percorrida por dia em km dividido pelo tamanho da célula.

### Transformando a distancia media que o individuo percorre por dia em km para
### distancia media em graus decimais.
R1=6.509/110 #transformar km em graus decimais 
 
### EScolhendo ao acaso as localizacoes iniciais
ee= bn.bounds # Checando quais sao as coordenadas XYmin e XYmax do mapa.
X= ee[0]+(ee[2]-ee[0])*np.random.uniform(size= 1) # Selecionando ao acaso as localizacoes iniciais de X.
Y= ee[1]+(ee[3]-ee[1])*np.random.uniform(size= 1) # Selecionando ao acaso as localizacoes iniciais de X.

### EScolhendo sistematicamente as localizacoes iniciais.(**OBS: trabalhar nisso depois)
e = [X[0],Y[0]]
ee= teste.bounds

### Esse procedimentos sao necessarios para padronizar as coisas antes de comecar a
### movimentacao. OBS: Pensar como vai ser a melhor maneira de fazer isso. 

### Evitando que o individuo caia fora do mapa.

### Teste aprendizado por reforco
import numpy as np
import tensorflow as tf

### Paisagem 
paisagem = np.array([
    [-1, -1, -1, -1, -1],
    [-1, 0, -1, 0, -1],
    [-1, 0, 0, 0, -1],
    [-1, -1, -1, -1, -1],
    [-1, 0, 0, 0, 1]])

### Tamanho
altura, largura = paisagem.shape

### Parametros
alpha = 0.1  # Taxa de aprendizado
gamma = 0.9  # Fator de desconto
epsilon = 0.1  # Probabilidade de ação aleatoria

# Crie uma tabela Q como uma rede neural em TensorFlow
modelo = tf.keras.Sequential([tf.keras.layers.Input(shape=(altura, largura, 1)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(4)])  # 4 ações possíveis (cima, baixo, esquerda, direita)

# Compile o modelo
modelo.compile(optimizer='adam', loss='mean_squared_error')

# Treinamento dos agentes usando Q-Learning
episodios = 1000

for episodio in range(episodios):
    estado = np.zeros((1, altura, largura, 1))
    x, y = 0, 1  # Posição inicial do agente
    estado[0, x, y, 0] = 1  # Codificação one-hot do estado inicial

    while paisagem[x, y] != 1:  # Enquanto não atingir o objetivo
        if np.random.rand() < epsilon:
            acao = np.random.randint(0, 4)  # Ação aleatória com probabilidade epsilon
        else:
            acao = np.argmax(modelo.predict(estado)[0])  # Escolha ação com base no modelo

        novo_x, novo_y = x, y
        if acao == 0:  # Cima
            novo_x = max(x - 1, 0)
        elif acao == 1:  # Baixo
            novo_x = min(x + 1, altura - 1)
        elif acao == 2:  # Esquerda
            novo_y = max(y - 1, 0)
        else:  # Direita
            novo_y = min(y + 1, largura - 1)

        novo_estado = np.zeros((1, altura, largura, 1))
        novo_estado[0, novo_x, novo_y, 0] = 1

        recompensa = paisagem[novo_x, novo_y]
        target = modelo.predict(estado)
        target[0][0]
        target[0, x, y, acao] = recompensa + gamma * np.max(modelo.predict(novo_estado)[0])

        modelo.fit(estado, target, epochs=1, verbose=0)

        x, y, estado = novo_x, novo_y, novo_estado

# Sem rede neural

import numpy as np
import random

# Defina a paisagem como uma matriz de recompensas (por exemplo, -1 para obstáculos, 0 para espaços vazios, 1 para objetivo)
paisagem = np.array([
    [-1, -1, -1, -1, -1],
    [-1, 0, -1, 0, -1],
    [-1, 0, 0, 0, -1],
    [-1, -1, -1, -1, -1],
    [-1, 0, 0, 0, 1]
])

# Defina o tamanho do ambiente
altura, largura = paisagem.shape

# Taxa de aprendizado
alpha = 0.1

# Fator de desconto
gamma = 0.9

# Número de episódios de treinamento
episodios = 1000

# Tabela Q para armazenar os valores Q
Q = np.zeros((altura, largura, 4))  # 4 ações possíveis (cima, baixo, esquerda, direita)

# Função para escolher uma ação com base na tabela Q e na política epsilon-greedy
def escolher_acao(estado, epsilon):
    if random.uniform(0, 1) < epsilon:
        return random.randint(0, 3)  # Escolha uma ação aleatória com probabilidade epsilon
    else:
        return np.argmax(Q[estado])

# Treinamento dos agentes usando Q-Learning
for episodio in range(episodios):
    estado = (0, 1)  # Posição inicial do agente
    while estado != (4, 4):  # Enquanto não atingir o objetivo
        acao = escolher_acao(estado, epsilon=0.1)  # Escolher ação com base na política epsilon-greedy
        x, y = estado
        if acao == 0:  # Cima
            novo_estado = (max(x - 1, 0), y)
        elif acao == 1:  # Baixo
            novo_estado = (min(x + 1, altura - 1), y)
        elif acao == 2:  # Esquerda
            novo_estado = (x, max(y - 1, 0))
        else:  # Direita
            novo_estado = (x, min(y + 1, largura - 1))
        
        recompensa = paisagem[novo_estado]
        Q[x, y, acao] = (1 - alpha) * Q[x, y, acao] + alpha * (recompensa + gamma * np.max(Q[novo_estado]))
        estado = novo_estado

# Agora a tabela Q contém os valores Q aprendidos
print("Tabela Q:")
print(Q)






