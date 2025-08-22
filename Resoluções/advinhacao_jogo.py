'''
    Hora de programar um jogo! Seu código deve gerar um número aleatório dentro de um
    intervalo escolhido pelo próprio jogador, que servirá como resposta, e solicitar que o
    usuário tente adivinhá-lo. A partir da resposta do usuário:
    a. Se o palpite do usuário for errado, o jogo deve informar ao usuário se foi maior ou
    menor que a resposta correta e solicitar um novo chute.
    b. Se o palpite for correto, o jogo deve avisar ao usuário que ele acertou e informar o
    número de tentativas utilizadas.
'''

import random

# Exceção personalizada caso o número máximo seja menor ou igual ao número mínimo de intervalo
class ErrorRange(Exception):

    # Inicializador com o valor mínimo e máximo do intervalo
    def __init__(self, minNumber, maxNumber):
        # Mensagem de exceção personalizada
        defaultMessage = "O número máximo deve ser maior que o número mínimo de intervalo"
        msg = f"{defaultMessage}. \nNúmero máximo: {maxNumber} | Número mínimo: {minNumber}"
        super().__init__(msg)

def play():

    print("\nPara iniciar o jogo, informe o valor mínimo e máximo de intervalo!")

    try:
        # Coleta as informações do usuário
        minNumber = int(input("Valor mínimo para o intervalo:"))
        maxNumber = int(input("Valor máximo para o intervalo:"))
    except ValueError:
        # Exceção para caso o valor não seja inteiro
        print("Por favor, digite apenas números inteiros")
        return 

    # Verifica se o valor mínimo de intervalo é menor que o valor máximo
    if minNumber >= maxNumber:
        # Lança exceção personalizada
        raise ErrorRange(minNumber,maxNumber)
    
    # Pega um número aleatório dentro do intervalo
    randomNumber = random.randint(minNumber, maxNumber)

    # Inicia com 0 tentativas
    attempts = 0

    # Ilustra o intervalo
    print(f"O número sorteado está entre {minNumber} e {maxNumber}")

    # Loop até o jogador acertar o número sorteado
    while True:
        
        print('\n==================================================================\n')

        # Coleta o palpite e exibe a exceção caso não seja um inteiro
        try:
            attempt = int(input("Tente adivinhar o número sorteado:"))  
        except ValueError:
            print("Por favor, digite apenas números inteiros, vamos desconsiderar essa tentativa")
            continue

        # Adiciona uma tentativa
        attempts += 1

        # Validação para caso o jogador informe um número fora do intervalo
        if attempt < minNumber or attempt > maxNumber:
            print("O número inserido está fora do intervalo informado")
            print(f"Tente um número entre {minNumber} e {maxNumber}")
        # Se o palpite for igual ao número sorteado
        elif attempt == randomNumber:
            # Avisa que o usuário acertou, mostra o número de tentativas e sai do loop
            print("Parabéns, você acertou!")
            print(f"Número de tentativas: {attempts}")
            break
        # Se o palpite for maior que o número sorteado
        elif attempt > randomNumber:
            # Informa que o palpite foi maior
            print("Palpite errado!")
            print("Seu palpite foi maior do que o número sorteado, tente novamente")
        # Se o palpite for menor que o número sorteado
        elif attempt < randomNumber:
            # Informa que o palpite foi menor
            print("Palpite errado!")
            print("Seu palpite foi menor do que o número sorteado, tente novamente")

# Variavél auxiliar para verificar se o usuário quer jogar novamente
playAgain = '1'

# Loop para o usuário poder jogar mais de uma vez
while playAgain == '1':
    try:
        play()
    except ErrorRange as e:
        print(e)
    except Exception as e :
        print('Ocorreu um erro ao jogar')
        print(e)

    # Pergunte se o jogador que jogar novamente ou sair
    playAgain = input("\nPara jogar novamente, tecle 1 ou digite qualquer outra tecla para sair: ")

print("Você saiu, obrigado por jogar")