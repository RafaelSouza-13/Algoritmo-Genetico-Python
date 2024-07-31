import random

class Individuo:
    def __init__(self, espacos, valores, limite_espaco, geracao=0):
        self.espaco = espacos
        self.valores = valores
        self.limite_espaco = limite_espaco
        self.nota_avaliacao = 0;
        self.geracao = geracao
        self.cromossomos = []
        self.inicializa_cromossomos
        
    def inicializa_cromossomos(self):
        for i in range(self.espacos):
            if(random() < 0.5):
                self.cromossomos.append("0")
            else:
                self.cromossomos.append("1")