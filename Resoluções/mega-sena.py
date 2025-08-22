'''
    Escreva um código para realizar o sorteio da mega-sena, que consiste na seleção de seis
    números diferentes compreendidos entre 1 e 60. Retorne o array contendo os números
    sorteados.
'''

import random

def draw():
    try:

        # Set usado para coleção de itens únicos, para não sortear duas vezes o mesmo número
        numbers = set()

        # Realiza o sorteio enquanto não sortear 6 números diferentes
        while len(numbers) < 6:

            # Adiciona um número entre 1 e 60
            numbers.add(random.randint(1, 60))

        # Retorna os números sorteados
        return list(numbers)
    except Exception as e:
        print('Ocorreu um erro ao realizar o sorteio')
        print(e)
    
# Realizando o sorteio
lottery = draw()

# Apresentando o resultado
print("O resultado do sorteio da Mega-Sena é:")
print("============================================================")
for number in lottery:
    print(number)
print("============================================================")