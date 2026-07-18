# Vetor não ordenado

import pandas as pd
import numpy as np

class VetorNaoOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n) - Complexidade linear
    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio.")
        else:
            for i in range(self.ultima_posicao + 1):
                print(f"Índice {i}: {self.valores[i]}")
    
    # O(1) - Complexidade constante
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Capacidade máxima atingida.")
            return

        self.ultima_posicao += 1
        self.valores[self.ultima_posicao] = valor

    # O(n) - Complexidade linear
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] == valor:
                return i
        return -1

    # O(n) - Complexidade linear
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            print("Valor não encontrado.")
            return

        for i in range(posicao, self.ultima_posicao):
            self.valores[i] = self.valores[i + 1]

        self.ultima_posicao -= 1
        print(f"Valor {valor} excluído com sucesso.")


vetor = VetorNaoOrdenado(5) # vetor com capacidade para 5 elementos

vetor.imprime()  # Deve imprimir que o vetor está vazio

vetor.insere(11)

vetor.imprime()  # Deve imprimir o valor 11 no índice 0

vetor.insere(22)
vetor.insere(33)
vetor.insere(44)
vetor.insere(55)

vetor.imprime()  # Deve imprimir os valores 11, 22, 33, 44, 55 no índice 0 a 4

vetor.insere(66)  # Deve imprimir que a capacidade máxima foi atingida

print(f"Índice do valor 33: {vetor.pesquisar(33)}")  # Deve imprimir o índice 2
print(f"Índice do valor 66: {vetor.pesquisar(66)}")  # Deve imprimir -1

vetor.excluir(44)  # Deve imprimir que o valor 44 foi excluído com sucesso

vetor.imprime()  # Deve imprimir os valores 11, 22, 33, 55 no índice 0 a 3
