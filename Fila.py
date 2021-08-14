class Fila:
    def __init__(self, tamanho):
        self.tamanho =  tamanho
        self.cidades = [None] * self.tamanho
        self.inicio = 0
        self.fim = -1
        self.numeroElementos = 0

    def enqueue(self, cidade):
        if self.fim == self.tamanho -1:
            self.fim = -1
        self.fim += 1
        self.cidades[self.fim] = cidade
        self.numeroElementos +=1

    def dequeue(self):
        temp = self.cidades[self.inicio]
        self.inicio += 1
        if self.inicio == self.tamanho:
            self.inicio = 0
        self.numeroElementos -= 1
        return temp

    def getFirst(self):
        return self.cidades[self.inicio]

    def isEmpty(self):
        return self.numeroElementos == 0

    def isFull(self):
        return self.numeroElementos == self.tamanho