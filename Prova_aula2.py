# [PYDS-A02] Você está responsável por gerenciar os resultados de uma competição esportiva. Para isso, você tem uma lista de tuplas onde cada tupla representa 
# uma equipe e suas respectivas pontuações em diferentes rodadas. O formato de cada tupla é:

# ('nome_da_equipe', [lista_de_pontuacoes]).

# Tarefas a serem realizadas:

# Calcular a média das pontuações: Para cada equipe, calcule a média de suas pontuações e armazene esses valores em uma nova lista chamada medias.
# Cada média deve corresponder à equipe respectiva.

# Ordenar as médias: Organize a lista medias em ordem decrescente, de modo que a equipe com a maior média apareça primeiro.

# Criar uma lista de classificação: Crie uma nova lista chamada classificacao, que contenha tuplas. Cada tupla deverá ter o nome da equipe e sua média 
# de pontuações, seguindo a ordem decrescente da média.

# Exibir a classificação final: Mostre na tela a classificação final das equipes, exibindo o nome da equipe e sua média, da equipe com a maior média 
# para a menor.


lista_eqp1 = [40 , 33 , 60]
lista_eqp2 = [60 , 80 , 75]
lista_eqp3 = [90 , 50 , 87]
lista_eqp4 = [100 , 97 , 59]
lista_eqp5 = [78 , 80 , 79]

media1 = sum(lista_eqp1) / len(lista_eqp1)
media2 = sum(lista_eqp2) / len(lista_eqp2)
media3 = sum(lista_eqp3) / len(lista_eqp3)
media4 = sum(lista_eqp4) / len(lista_eqp4)
media5 = sum(lista_eqp5) / len(lista_eqp5)


eqp1 = ('Equipe 1' , lista_eqp1)
eqp2 = ('Equipe 2' , lista_eqp2)
eqp3 = ('Equipe 3' , lista_eqp3)
eqp4 = ('Equipe 4' , lista_eqp4)
eqp5 = ('Equipe 5' , lista_eqp5)
lista_de_equipes = [eqp1 , eqp2 , eqp3 , eqp4 , eqp5]

print('====='*10)
print('\n\n')
for i in lista_de_equipes:
    print(i)

print('\n\n')

medias = []
medias.append(media1)
medias.append(media2)
medias.append(media3)
medias.append(media4)
medias.append(media5)

equipes = ['Equipe 1' , 'Equipe 2' , 'Equipe 3' , 'Equipe 4' , 'Equipe 5']

classificacao = sorted(zip(medias , equipes) , reverse=True)

print('====='*10)
print('\n\n')

print('Classificação Final:')
print('\n')
for media , equipe in classificacao:
    print(f'{equipe} - {media:.2f}')

print('\n\n')
print('====='*10)




