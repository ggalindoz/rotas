from Fila import Fila

class Largura:
    def __init__(self, estadoInicial, estadoObjetivo):
        self.estadoInicial = estadoInicial
        self.estadoObjetivo = estadoObjetivo
        self.encontrou = False
        self.estadoInicial.visitado = True
        self.fronteira = Fila(20)
        self.fronteira.enqueue(estadoInicial)

    def buscar(self):
        first = self.fronteira.getFirst()
        print('Primeiro: {}'.format(first.nome))

        if first == self.estadoObjetivo:
            self.encontrou = True
        else:
            temp = self.fronteira.dequeue()
            print('Desinfileirou: {}'.format(temp.nome))

            for a in first.adjacentes:
                print('Visitado: {}'.format(a.cidade.nome))
                if(a.cidade.visitado == False):
                    a.cidade.visitado == True
                    self.fronteira.enqueue(a.cidade)

            if self.fronteira.numeroElementos > 0:
                Largura.buscar(self)



