## Criando individuo com memoria

class IndMemory(Individuo):
      
      def __init__(self,x):
          Individuo.__init__(self,x)
          print("Criado")
