from random import random
from model.individuo import Individuo


class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0

    def inicializa_populacao(self, espacos, valores, limite_espaco):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(espacos, valores, limite_espaco))
        for individuo in self.populacao:
            individuo.avaliacao()
        self.ordena_populacao()
        self.melhor_solucao = self.populacao[0]
    
    def ordena_populacao(self):
        self.populacao = sorted(self.populacao, key=lambda populaca: populaca.nota_avaliacao, reverse=True)

    # def melhor_individuo(self, individuo):
    #     if(individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao):
    #         self.melhor_solucao = individuo
    
    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.nota_avaliacao
        return soma
    
    def seleciona_pai(self, soma_avaliacao):
        pai_indice = -1
        valor_sorteado = random() * soma_avaliacao
        soma = 0
        i = 0
        while(i < len(self.populacao) and soma < valor_sorteado):
            soma += self.populacao[i].nota_avaliacao
            pai_indice += 1
            i += 1
        return pai_indice

    def gera_individuos(self, soma_avaliacao):
        for individuos in range(0, self.tamanho_populacao, 2):
            pai1 = self.seleciona_pai(soma_avaliacao)
            pai2 = self.seleciona_pai(soma_avaliacao)

