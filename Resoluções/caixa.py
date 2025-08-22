'''
    Um caixa eletrônico tem disponível apenas notas de R$ 5, R$ 20 e R$ 50. Crie um
    algoritmo que recebe como entrada o valor que se deseja sacar e retorne a menor
    quantidade de notas que o compõem, especificando a quantidade de cada nota.
    Atenção para os casos em que a entrada não é divisível pelo valor notas disponíveis.
    Ex1: para um saque de R$ 25, o algoritmo retornaria que são 2 notas, uma de 5 e uma
    de 20.
    Ex2: para um saque de R$ 175, o algoritmo retornaria que são 5 notas, três de 50, uma
    de 20 e uma de 5.
'''

# Exceção personalizada para tratar saques que não podem ser divididos por 5
class ErrorWithdrawal(Exception):

    # Inicializador com o valor mínimo e máximo do intervalo
    def __init__(self):
        # Mensagem de exceção personalizada
        defaultMessage = "Só temos disponíves notas de R$5,00, R$20,00 e R$50,00.\nPor favor insira um valor que possa ser divisível por R$5,00."
        super().__init__(defaultMessage)

# Bloco try para tratar exceções
try:
    # Captura a entrada do usuário
    withdrawal = input('Insira o valor que deseja sacar:').strip()
    
    # Contador para verificar mais facilmente a quantidade das notas
    counter= {
        '5':0,
        '20':0,
        '50':0
    }
    '''
        Parse para float e substituição da virgula por ponto, 
        para ficar com formatação em português e aceitar os dois tipos de entrada
    '''
    withdrawal = float(withdrawal.replace(',','.'))

    # Valida se o valor é divisível
    if withdrawal % 5 != 0:
        raise ErrorWithdrawal()
    
    # Loop para contar as notas enquanto for maior que 0
    while withdrawal > 0:

        # Veriica a possibilidade de remover a quantia do maior para o menor
        # Se puder remover 50, remove e acrescenta 1 ao contador de 50
        if withdrawal >= 50:
            withdrawal -= 50
            counter['50'] += 1
        # Se puder remover 20, remove e acrescenta 1 ao contador de 20
        elif withdrawal >= 20:
            withdrawal -= 20
            counter['20'] += 1
        # Se puder remover 5, remove e acrescenta 1 ao contador de 5
        elif withdrawal >= 5:
            withdrawal -= 5
            counter['5'] += 1
        # Caso não seja possível remover, o valor é inferior a 5, sai do loop
        else:
            break
    
    # Apresenta o resultado
    print(f'Quantidade de notas de R$50,00: {counter["50"]}')
    print(f'Quantidade de notas de R$20,00: {counter["20"]}')
    print(f'Quantidade de notas de R$5,00: {counter["5"]}')
    
    # Exibe o total de notas usadas
    total_notes = counter["50"] + counter["20"] + counter["5"]
    print(f"Total de notas usadas: {total_notes}")

# Captura a exceção do tipo ValueError, caso o usuário digite alguma entrada inválida (Ex: 'Teste') 
except ErrorWithdrawal as e:
    print(e)

except ValueError as e:
    # Apresenta mensagem exclusiva para esse tipo de exceção
    print('O valor informado é invalido')
    print(e)

# Captura outras possíveis exceções
except Exception as e:
    print('Ocorreu um erro no processamento, tente novamente mais tarde')
    print(e)
