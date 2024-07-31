from random import random

class Individuo:
    def __init__(self, espacos, valores, limite_espaco, geracao=0):
        self.espacos = espacos
        self.valores = valores
        self.limite_espaco = limite_espaco
        self.nota_avaliacao = 0
        self.espaco_usado = 0
        self.geracao = geracao
        self.cromossomos = []
        self.inicializa_cromossomos()
        
    def inicializa_cromossomos(self):
        for i in range(len(self.espacos)):
            if(random() < 0.5):
                self.cromossomos.append("0")
            else:
                self.cromossomos.append("1")
    
    def avaliacao(self):
        nota = 0
        soma_espacos = 0
        for i in range(len(self.cromossomos)):
            if(self.cromossomos[i] == "1"):
                nota += self.valores[i]
                soma_espacos += self.espacos[i]
        
        if(soma_espacos > self.limite_espaco):
            nota = 1
        self.nota_avaliacao = nota
        self.espaco_usado = soma_espacos