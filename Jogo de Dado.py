"""
Simulador de dado
"""

import random

numero = random.randint(1, 6)
numero1 = random.randint(1, 6)
print('Número do dado do Jogador 1 é {}'.format(numero))
print('Número do dado do Jogador 2 é {}'.format(numero1))
if numero > numero1:
    print('Jogador 1 venceu!')
elif numero == numero1:
    print('Empate!')
else:
    print('Jogador 2 venceu!')
