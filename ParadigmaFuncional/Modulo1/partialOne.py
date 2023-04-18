import operator
from functools import partial
add_um = partial(operator.add, 1)

print(add_um(5))

#Segundo Exemplo Partial
print('\nSegundo Exemplo')
import collections
from operator import attrgetter
pessoa = collections.namedtuple('pessoa', 'nome idade')
pessoas = [pessoa('João', 40), pessoa('Ana', 20), pessoa('Renata', 25)]

print(sorted(pessoas, key=attrgetter('nome')))
print(sorted(pessoas, key=attrgetter('idade')))

#Terceiro Exemplo
print('\n Terceiro Exemplo')
from functools import partial
sort_nome = partial(sorted,key=attrgetter('nome'))
sort_idade = sort_nome = partial(sorted,key=attrgetter('idade'))

print(sort_nome(pessoas))
print(sort_idade(pessoas))