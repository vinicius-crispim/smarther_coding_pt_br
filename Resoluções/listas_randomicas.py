'''
    Daniel, um programador jovem e cheio de vontade de aprender, precisava incorporar
    em seu código uma função que gerasse numeros aleatorios.
    Daniel queria, contudo, garantir que a função escolhida tivesse uma distribuição
    verdadeiramente aleatória.
    Ele decidiu montar o código conforme a imagem abaixo para testar a função random
    escolhida: em que Random(n) retorna um número inteiro, aleatoriamente, entre 1 e n,
    inclusos.
    A ideia do código era chamar a função randômica 1000 vezes e registrar o resultado
    em uma lista, salvando o valor em "Lista1" caso ele seja maior que 5 ou em "Lista2"
    caso seja menor ou igual.
    Com este experimento, Daniel esperava obter duas listas, cada uma com
    aproximadamente 500 elementos, em que Lista1 teria apenas números de 6 a 10 e
    Lista2 teria apenas números de 1 a 5.
    Ao final do experimento, Daniel verificou o tamanho das listas, e sucesso! Cada lista
    possuía aproximadamente 500 elementos. Ao ver o valor dos elementos, contudo,
    Daniel se surpreendeu.
    Ambas as listas possuíam números de 1 a 10!
    Qual correção deve ser feita no código de Daniel para corrigir este erro de lógica?
'''

''' 
    A correção deve ser feita no if e na adição do novo número na lista, pois o código verifica se
    um número gerado aleatoriamente entre 1 e 10 é maior que 5, se for é gerado outro número aleatório
    entre 1 e 10 e registra na lista1, senão ele gera outro número aleatório para adicionar na lista2.
    Então o código não insere na lista o mesmo número validado no if, é inserido outro valor aleatório de 1 a 10 em
    ambas as listas.
    Para corrigir isso, eu adicionaria o número aleatório em uma variavel antes do if e usaria essa
    variável para verificar no if e também para adicionar nas listas, segue exemplo em python:
'''

import random

count = 0
lista1 = []
lista2 = []
while count < 1000:
    randomNumber = random.randint(1,10)
    if randomNumber > 5:
        lista1.append(randomNumber)
    else:
        lista2.append(randomNumber)
    count = count + 1

print(lista1)

print(lista2)
