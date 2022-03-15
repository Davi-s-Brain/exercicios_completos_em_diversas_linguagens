# Escolhe um sanduíche automáticamente

from random import choice, randint

listaPaes = ['3 Queijos', 'Parmesão e orégano', '9 grãos', 'Italiano Branco']
listaQueijos = ['Cheddar', 'Suíço', 'Queijo Mussarela Ralada']
listaVegetais = ['Azeitonas', 'Picles', 'Pepinos', 'Pimentão', 'Alface',
                 'Cebola Roxa', 'Tomate', 'Rúcula', 'Cenoura Ralada', 'Vinagrete']
listaMolhos = ['Cebola Agridoce', 'Chipotle', 'Barbecue', 'Parmesão',
               'Maionese Temperada', 'Mostarda e Mel', 'Supreme']


def escolhe_pao():
    pao = choice(listaPaes)
    return print(pao)


def escolhe_queijo():
    queijo = choice(listaQueijos)
    return print(queijo)


def escolhe_vegetais():
    i = randint(2, 4)
    vegetais = []
    for n in range(i):
        escolhido = choice(listaVegetais)
        index_lista = listaVegetais.index(escolhido)
        vegetais.append(escolhido)
        listaVegetais.pop(index_lista)

    return print(vegetais)


def escolhe_molhos():
    i = randint(2, 3)
    molho = []
    for n in range(i):
        escolhido = choice(listaMolhos)
        index_lista = listaMolhos.index(escolhido)
        molho.append(escolhido)
        listaMolhos.pop(index_lista)

    return print(molho)


def monta_sanduba():
    escolhe_pao()
    escolhe_queijo()
    print('Recheio à vontade')
    escolhe_vegetais()
    escolhe_molhos()


monta_sanduba()
