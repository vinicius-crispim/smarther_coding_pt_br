'''
    Um cliente da SMARTHIS possui o seguinte processo de RPA: Todo dia um grupo de
    notas fiscais, cada uma com um valor, chegam para serem processadas. O
    processamento destas notas segue as seguintes regras:
    Notas com valor abaixo de R$ 5.000 reais devem ter seu valor incluído no banco de
    dados do cliente diretamente.
    Notas acima de R$ 5.000 reais devem ter seu valor enviado por email para o centro de
    custo do cliente, onde serão incluídas manualmente por eles.
    Notas com valor R$ 0 não devem ser processadas e no final da automação, deve ser
    enviado um email ao centro de custo informando a quantidade de notas com este valor.
    A quantidade total de notas processadas (independente de valor) deve ser enviada por
    e-mail para o centro de custo.
    O pseudocódigo deste processo pode ser visto abaixo:
    • Obter as notas a serem processadas no dia e criar um array de objetos que
    representem essas notas fiscais.
    • Enviar um e-mail para o centro de custo com a quantidade de itens desse array
    (quantidade total de notas)
    • Para cada nota:
    o Se o valor da nota é igual a zero:
    ▪ Incrementa a contagem de notas zeradas
    o Se o valor da nota é menor que R$ 5.000:
    ▪ Inclui os dados da nota fiscal no banco de dados
    o Senão:
    ▪ Envia a nota fiscal por e-mail para o centro de custo
    • Enviar um e-mail com a quantidade de notas fiscais com o valor igual a zero.
    Recentemente, o cliente solicitou uma alteração no RPA. Eles querem que todos os
    emails sejam mandados em sequência, sem que nenhuma inclusão no banco de dados
    seja feita entre o envio de qualquer e-mail. Estas inclusões devem ser feitas antes ou
    depois do envio de todos os emails.
    Em outras palavras, entre os email de quantidade de notas, quantidade de notas zeradas
    e notas acima de R$ 5.000, não podem existir inclusões no banco de dados.
    Modifique o código para incluir esta regra nova.
'''

''' 
    A lógica atual mistura o envio de e-mails e as inclusões no banco de dados em blocos iguais, então 
    para modificar isso eu decidi separar em dois blocos diferentes, primeiro fazendo as inclusões no banco
    e depois fazendo os envios de e-mails
'''

def process_nf():
    
    # Recebo o total de filas (notas) para serem processadas e guardo em uma variável
    # Para exemplificar, decidi fixar o valor
    notes = [
            {'nota':'Nota 1', 'valor':4200},
            {'nota':'Nota 2', 'valor':6000},
            {'nota':'Nota 3', 'valor':4000},
            {'nota':'Nota 4', 'valor':9000},
            {'nota':'Nota 5', 'valor':0}
        ]

    # Pego a quantidade de notas
    total = len(notes)

    # Variável para contar as notas com valor 0 - serão usadas para enviar e-mail
    zeroCounter = 0

    # Lista para salvar as notas maiores que 0 e menores que R$5000,00 - serão inclusas no banco posteriormente
    dbNotes = []

    # Lista para salvar as notas maiores que R$5000,00 - serão usadas para enviar e-mail
    emailNotes = []

    # Percorre as notas
    for nota in notes:
        # Caso valor seja zero, adicionar na variável que conta as notas com valor 0
        if nota["valor"] == 0:
            zeroCounter += 1
        # Caso valor seja maior que zero e menor que R$5.000, adiciona na lista de notas para o banco
        elif nota["valor"] < 5000:
            dbNotes.append(nota)
        # Caso valor seja maior que R$5.000, adiciona na lista de notas envio de e-mail
        else:
            emailNotes.append(nota)

    # Eu optei por inserir as notas no banco primeiramente, portanto insere as notas no banco
    for nota in dbNotes:
        insert_note(nota)

    # Após as inclusões, o RPA irá fazer os envios de e-mail
    send_email_total(total)
    send_email_notes(emailNotes)
    send_email_zero(zeroCounter)

# Envia o e-mail com o total de notas
def send_email_total(total):
    print(f"Código de envio de e-mail com o total de notas para os destinatários - total: {total}")    
    
# Envia o e-mail com o total de notas zeradas
def send_email_zero(zeroCounter):
    print(f"Código de envio de e-mail com o total de notas zeradas - Notas zeradas: {zeroCounter}")    

# Envia um e-mail para notas acima de R$5.000
def send_email_notes(notes):
    # Loop para enviar um e-mail para cada nota com valor acima de R$5.000
    for note in notes:
        print(f"Código de envio de e-mail para a nota acima de R$5.000 - {note['nota']} - {note['valor']}")    

# Insere notas no banco
def insert_note(note):
    print(f"Código para incluir nota no banco de dados - {note['nota']} - {note['valor']}")


process_nf()

