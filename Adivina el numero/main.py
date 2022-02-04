import random
numeroIntentos=0
numeroMin=0
numeroMax=200

print('Hola! Cual es tu nombre?:')
usuario=input()

numero = random.randint(numeroMin, numeroMax)

print('Genial, encantado ' + usuario+'!. Estoy pensando en un numero que se encuentra entre el '+str(numeroMin)+ ' y el ' +str(numeroMax))

while numeroIntentos < 7:
    print ('Intenta Adivinarlo:')
    intento = input()
    intento = int(intento)
    numeroIntentos = numeroIntentos + 1

    if intento < numero:
        print('Tu numero es demasiado bajo.')
    if intento > numero:
        print('Tu numero es demasiado alto')
    if intento == numero:
        break

if intento == numero:
    numeroIntentos=str(numeroIntentos)
    print('Buen trabajo '+ usuario + '!, tu has adivinado el numero en '+ numeroIntentos + ' intentos' )
if intento != numero:
    print('No!, el numero que estaba pensando era ' + str(numero))
