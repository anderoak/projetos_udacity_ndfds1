# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for linha in data_list[:20]:
    print(linha)

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for linha in data_list[:20]:
    print(linha[6])


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
    Função para criar uma lista o o conteúdo de uma coluna específica.
    Argumentos:
        param1: Lista de dados.
        param2: Índice referente a coluna que será a origem da lista.
    Retorna:
        Uma lista com o conteúdo de uma coluna.
    """
    column_list = []
    for i in range(len(data_list)):
        column_list.append(data[i][index])
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0
unknow = 0
for gender in column_to_list(data_list, -2):
    if gender == "Male":
        male += 1
    elif gender == "Female":
        female += 1
    else:
        unknow += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female, "\nGênero desconhecido: ", unknow)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
    Função para contar os tipos de gênero.
    Argumentos:
        param: Lista de dados.
    Retorna:
        Uma lista com o total de cada gênero, masculino e feminino.
    """
    male = 0
    female = 0
    for gender in column_to_list(data_list, -2):
        if gender == "Male":
            male += 1
        elif gender == "Female":
            female += 1
    return [male, female]

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """
    Função para verificar maior ocorrência entre os gêneros.
    Argumentos:
        param: Lista de dados.
    Retorna:
        Uma string com nome do gênero com maior ocorrência ou a string "Igual" em caso de igualdade.
    """
    answer = ""
    gender_totals = count_gender(data_list)
    if gender_totals[0] > gender_totals[1]:
        answer = "Masculino"
    elif gender_totals[0] < gender_totals[1]:
        answer="Feminino"
    else:
        answer="Igual"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
def count_user_type(data_list):
    """
    Função para contar os tipos de usuário.
    Argumentos:
        param: Lista de dados.
    Retorna:
        Uma lista com o tota de usuários de cada tipo, subscriber e customer.
    """
    subscriber = 0
    customer = 0
    for user_type in column_to_list(data_list, -3):
        if user_type == "Subscriber":
            subscriber += 1
        elif user_type == "Customer":
            customer += 1
    return [subscriber, customer]

print("\nTAREFA 7: Verifique o gráfico!")
user_type_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos de Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "O total por gênero não inclui a quantidade de usuários tipo Customer ("+ str(unknow) + ").\nPorque apenas os registros de usuários do tipo Subscriber tem o campo gênero preenchido."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().

trip_duration_list = column_to_list(data_list, 2)

# Converte valores para inteiro.
for i in range(len(trip_duration_list)):
        trip_duration_list[i] = int(trip_duration_list[i])

# "Recriando a roda" - Já que não posso usar as práticas funções que alguém criou antes.
def min_max_med_medi(list):
    """
        A partir da entrada de uma lista, função para calcula os valores estatísticos
        descritivos Mínimo, Máximo, Média e Mediana.
        Argumentos:
            param: Lista de valores  de inteiros.
        Retorna:
            Uma lista com os valores [Mínimo, Máximo, Média, Mediana].
    """
    min = 2**100
    max = 0
    mean_sum = 0

    for i in range(len(list)):
        value = int(list[i])
        if value < min:
            min = value
        if value > max:
            max = value
        mean_sum += value

    mean = mean_sum/len(list)
    sorted_list = sorted(list)

    if (len(sorted_list) % 2) == 0:
        mid_up = sorted_list[int(len(sorted_list)/2)]
        mid_dn = sorted_list[int((len(sorted_list)/2)-1)]
        medi = (mid_up + mid_dn)/2
    else:
        medi = sorted_list[int((len(sorted_list)/2))]
    return [min, max, mean, medi]

min_trip, max_trip, mean_trip, median_trip = min_max_med_medi(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", round(mean_trip), "Mediana: ", round(median_trip))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_types = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
Função de exemplo com anotações.
Argumentos:
    param1: O primeiro parâmetro.
    param2: O segundo parâmetro.
Retorna:
    Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

from collections import Counter
def count_items(column_list):
    types_list = dict(Counter(column_list))
    item_types = [key for key in types_list.keys()]
    count_items = [types_list[key] for key in types_list.keys()]
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------

input("Aperte Enter para continuar...")
# RESPOSTA BONUS
# Qual a idade Mínima, Máxima, Média e Mediana dos usuários?
from datetime import datetime

def get_age_list(min_year=0, max_year=datetime.now().year):
    """
    Cria uma lista de idades e uma lista de anos provavelmente informados errado, se houver.
    Argumentos:
        param1: Ano mínimo válido (se não informado considera o ano 0).
        param2: Ano máximo válido (se não infomado cosidera o ano atual).
    Retorna:
        Uma lista de valores x.
    """
    birth_year_list = column_to_list(data_list, -1)
    age_list = []
    probably_wrong_birth_year = []
    currentYear = datetime.now().year
    for i in range(len(birth_year_list)):
        if (birth_year_list[i] != ''):
            if (int(float(birth_year_list[i]))) < min_year or (int(float(birth_year_list[i]))) > max_year:
                probably_wrong_birth_year.append(data_list[i])
            age_list.append(int(currentYear - float(birth_year_list[i])))
    return age_list, probably_wrong_birth_year

# O parâmetro atual testa idades maiores de 90 e menores de 16 anos
min_year = (datetime.now().year - 90)
max_year = (datetime.now().year - 16)
age_list, probably_wrong_birth_year = get_age_list(min_year, max_year)

min_age, max_age, mean_age, median_age = min_max_med_medi(age_list)

print("\nRESPOSTA BÔNUS: Imprimindo a idade mínima, máxima, média e mediana dos usuários")
print("Min: ", min_age, "Max: ", max_age, "Média: ", round(mean_age), "Mediana: ", round(median_age))

if probably_wrong_birth_year != []:
    print('ATTENTION: Probably wrong birth year informed on database.')
    input("Aperte Enter para listar...")
    for linha in probably_wrong_birth_year:
        print(linha)

print('Fim da apresentação.\nObrigado pelo seu tempo e atenção!')
