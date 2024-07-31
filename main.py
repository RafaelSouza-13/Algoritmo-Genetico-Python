from model.produto import Produto
from model.individuo import Individuo

lista_produtos = []
lista_produtos.append(Produto("Geladeira Dako", 0.751, 999.90))
lista_produtos.append(Produto("Iphone 6", 0.0000899, 2911.12))
lista_produtos.append(Produto("TV 55' ", 0.400, 4346.99))
lista_produtos.append(Produto("TV 50' ", 0.290, 3999.90))
lista_produtos.append(Produto("TV 42' ", 0.200, 2999.00))
lista_produtos.append(Produto("Notebook Dell", 0.00350, 2499.90))
lista_produtos.append(Produto("Ventilador Panasonic", 0.496, 199.90))
lista_produtos.append(Produto("Microondas Electrolux", 0.0424, 308.66))
lista_produtos.append(Produto("Microondas LG", 0.0544, 429.90))
lista_produtos.append(Produto("Microondas Panasonic", 0.0319, 299.29))
lista_produtos.append(Produto("Geladeira Brastemp", 0.635, 849.00))
lista_produtos.append(Produto("Geladeira Consul", 0.870, 1199.89))
lista_produtos.append(Produto("Notebook Lenovo", 0.498, 1999.90))
lista_produtos.append(Produto("Notebook Asus", 0.527, 3999.00))
for produto in lista_produtos:
    print(produto.nome)

espacos = []
valores = []
nomes = []
limite = 3

for produto in lista_produtos:
    espacos.append(produto.espaco)
    valores.append(produto.valor)
    nomes.append(produto.nome)

individuo1 = Individuo(espacos, valores, limite)

for i in range(len(lista_produtos)):
    if(individuo1.cromossomo[i] == "1"):
        print(f"Produtos individuo 1: {lista_produtos[i].nome}")
individuo1.avaliacao()
print(f"Avaliacao individuo 1: {individuo1.nota_avaliacao}")
print(f"Espaço utilizado individuo 1: {individuo1.espaco_usado}")


print("Segundo individuo")

individuo2 = Individuo(espacos, valores, limite)
for i in range(len(lista_produtos)):
    if(individuo2.cromossomo[i] == "1"):
        print(f"Produtos individuo 2: {lista_produtos[i].nome}")
individuo2.avaliacao()
print(f"Avaliacao individuo 2: {individuo2.nota_avaliacao}")
print(f"Espaço utilizado individuo 2: {individuo2.espaco_usado}")

lista = individuo1.crossover(individuo2)

individuo1.mutacao(0.05)
individuo2.mutacao(0.05)
