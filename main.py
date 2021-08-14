from Mapa import Mapa
from Profundidade import Profundidade
from Largura import Largura
import timeit

from Cidade import Cidade
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
mapa = Mapa()
inicio = timeit.default_timer()
profundidade = Profundidade(mapa.portoUniao, mapa.curitiba)
profundidade.buscar()
print('Resultado: {}'.format(profundidade.fronteira.getTopo().nome))
fim = timeit.default_timer()

print ('duracao: %f' % (fim - inicio))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
