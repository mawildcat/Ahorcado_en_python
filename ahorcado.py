
'''
Juego del ahorcado hecho por mi del canal de youtube de Manuel González, reto 7, nivel 15
'''
import random
import os

from sympy import false

presentacion = '**************************\n*** JUEGO DEL AHORCADO ***\n**************************\n'
ahorcado = ['          !===| \n              |\n              |\n              |\n        ======|\n ',
'          !===| \n          O   |\n              |\n              |\n        ======|\n ',
'          !===| \n         _O   |\n              |\n              |\n        ======|\n ',
'          !===| \n         _O_  |\n              |\n              |\n        ======|\n ',
'          !===| \n         _O_  |\n          |   |\n              |\n        ======|\n ',
'          !===| \n         _O_  |\n          |   |\n         /    |\n        ======|\n ',
'          !===| \n         _O_  |\n          |   |\n         / \  |\n        ======|\n ']

lista_palabras = ['PERRO','GATO','ARMARIO','SILLA','HOGUERA','PAJARO','ALMENDRA','MELOCOTON','ESCALERA','BORDILLO','PAJARO','JAULA','BASURA','SOL',
'ALFOMBRA','CHIMENEA','BOLIGRAFO','LLUVIA','TAZA','MASAJE','TECLADO','TELEFONO','TOALLA','SOMBRERO','JIRAFA','LEON','ARDILLA','COCHE','LUNA','ARBOL',
'HOJA','ORDENADOR','CUCHARA','TENEDOR','PLATO','VASO','ZAPATILLA','BOTA','GOTA','UÑA','PATA','ALA','ASA','HIERRO']
abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'  # Letras que se pueden introducir
palabra = random.choice(lista_palabras) # Palabra que genera el programa
letras = []     # Lista de letras introducidas por el usuario, para que no se repitan
guiones = list('_'*len(palabra))    # Lista de guiones de tamaño de la palabra
fallos = 0
os.system('cls')

print(presentacion)
print(ahorcado[0])
print('         ',''.join(guiones))
print('')
#print('         ',palabra)
#print('         ','_'*len(palabra))
#print(type(guiones))

while True:

    letra = input('Introduce una letra: ').upper()

    if letra in letras:
        print('Ya se introdujo la {}'.format(letra))
    elif letra not in abecedario:
        print('Debe ser una letra')
    else:
        letras.append(letra)

        if letra in palabra:                # Si está en la palabra, imprime el mismo dibujo y aparecen las letras acertadas
            os.system('cls')
            print(presentacion)
            print(ahorcado[fallos])
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    guiones[i] = letra                
            #print('         ',palabra)
            print('         ',''.join(guiones))
            print('')
            if ''.join(guiones) == palabra:
                print('HAS GANADO!!!')
                print()
                break
        else:
            os.system('cls')
            fallos += 1
            print(presentacion)
            print(ahorcado[fallos])
            #print('         ',palabra)
            print('         ',''.join(guiones))
            print('')
            if fallos >= 6:
                print('PERDISTE, la palabra era: {}'.format(palabra))
                print()
                break

