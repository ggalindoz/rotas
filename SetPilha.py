class Pilha:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.cidades = [None] * self.tamanho
        self.topo = -1

    def push(self, cidade):
        if not Pilha.pilhaCheia(self):
            self.topo +=1
            self.cidades[self.topo] = cidade
        else:
            print("Pilha cheia")

    def pop(self):
        if not Pilha.isEmpty(self):
            cidadeTopo = self.cidades[self.topo]
            self.topo -= 1
            return cidadeTopo
        else:
            print("Pilha vazia")
            return None

    def getTopo(self):
        return self.cidades[self.topo]

    def isEmpty(self):
        return (self.topo == -1)

    def pilhaCheia(self):
        return (self.topo == self.tamanho -1)