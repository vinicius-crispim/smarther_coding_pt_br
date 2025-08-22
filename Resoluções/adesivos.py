'''
    Um conjunto de caixas é numerado em ordem crescente usando adesivos que contém
    algarismos individuais. Para se numerar a caixa de índice 10, são usados 2 adesivos, por
    exemplo. O orçamento para a aquisição de adesivos é limitado, então deseja-se
    conhecer número máximo de caixas que podem ser numerados, de 1 até um
    determinado valor, sem pular nenhum número na contagem, dado esse limite. Escreva
    um algoritmo que receba o número total de adesivos disponíveis e retorne o número
    máximo de caixas que podem ser numerados.
    Ex: Se há 14 adesivos disponíveis, é possível numerar 11 caixas.
'''
# Exceção personalizada para números negativos
class ErrorSticker(Exception):

    # Inicializador
    def __init__(self):
        # Mensagem de exceção personalizada
        defaultMessage = "Por favor informe um número positivo de adesivos"
        super().__init__(defaultMessage)

counter = 0
box = 0

try:
    # Coleta a entrada do usúario e transforma em inteiro
    stickers = int(input('Informe o número total de adesivos disponíveis:').strip())
    
    # Valida se o valor de adesivos é maior que 0
    if stickers < 0:
        raise ErrorSticker()
    
    # Loop para somar a quantidade correta baseada no tamanho da string do numero LEN (Ex: 1 = 1, 10 = 2, 100 = 3)
    for i in range(1, stickers):
        if counter + len(str(i)) > stickers:
            break
        counter += len(str(i))
        box += 1
    # Apresenta o total de caixas e quantos adesivos restaram
    print(f"Se há {stickers} adesivos disponíveis, é possivel numerar {box} caixas")
    print(f"Restaram {stickers-counter} adesivos")

except ErrorSticker as e:
    print(e)

except ValueError as e:
    # Apresenta mensagem exclusiva para esse tipo de exceção
    print('O valor informado é invalido, insira um número inteiro')
    print(e)

# Captura outras possíveis exceções
except Exception as e:
    print('Ocorreu um erro na verificação')
    print(e)
