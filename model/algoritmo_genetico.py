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
        self.melhor_solucao = self.populacao[0]
        self.ordena_populacao()
    
    def ordena_populacao(self):
        self.populacao = sorted(self.populacao, key=lambda populaca: populaca.nota_avaliacao, reverse=True)