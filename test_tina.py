maximo = 0
sorte = 0
inicio = 1
lista = []
var = 2

#******************************** Insere número máximo ********************************
while maximo == 0:
    print('Insira um numero de 1 a 305.000')
    maximo = int(input())
    if maximo > 0:
        if maximo <= 305000:
            print()
            print('Número digitado corretamente')
        else:
            print()
            print('Número digitado fora do padrão')
            maximo = 0
    else:
        print()
        print('Número digitado fora do padrão')
        maximo = 0
#******************************** Insere número da sorte ********************************
while sorte == 0:
    print('Digite seu numero da sorte:')
    print('Numero de 1 a',maximo)
    sorte = int(input())
    if sorte > 0:
        if sorte <= maximo:
            print()
            print('Número digitado corretamente')
        else:
            print()
            print('Número digitado fora do padrão')
            sorte = 0
    else:
        print()
        print('Número digitado fora do padrão')
        sorte = 0
#******************************** Monta lista inicial ********************************
while inicio <= maximo:
    lista.append(inicio)
    inicio = inicio + 1
print( )
print('Lista inicial')
print(lista)
#******************************** Monta ultima lista ********************************
while sorte >= var:
    del (lista[var-1::var])
    var = var+1
print('Lista final')
print(lista)
#******************************** Confere se número é sortudo ********************************
print()
print('Seu numero da sorte é:')
if sorte in lista:
    print('SORTUDO')
else:
    print('SEM SORTE')