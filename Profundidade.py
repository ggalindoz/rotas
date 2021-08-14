from SetPilha import Pilha

class Profundidade:
    def __init__(self, estadoInicial, estadoObjetivo):
        self.estadoInicial = estadoInicial
        self.estadoObjetivo = estadoObjetivo

        self.estadoInicial.visitado = True

        self.fronteira = Pilha(20)
        self.fronteira.push(estadoInicial)

        self.encontrou = False

    def buscar(self):
        cidadeTopo = self.fronteira.getTopo()
        print('Cidade que esta no topo da pilha: {}'.format(cidadeTopo.nome))

        if cidadeTopo == self.estadoObjetivo:
            self.encontrou = True
        else:
            for a in cidadeTopo.adjacentes:
                if self.encontrou == False:
                    print('Visitado: {}'.format(a.cidade.nome))
                    if (a.cidade.visitado == False):
                        a.cidade.visitado = True
                        self.fronteira.push(a.cidade)
                        Profundidade.buscar(self)
       