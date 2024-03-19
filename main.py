# # # # Ejercicios de LISTAS
# # # # Definir una lista de tipo str
# # # nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
# # # # Imprimir lista de nombres
# # # print(nombres)
# # # # Acceder a los elementos de una lista
# # # print(nombres[0])
# # # print(nombres[1])
# # # # Acceder a los elementos de manera inversa
# # # print(nombres[-1])
# # # print(nombres[-2])
# # #
# # # # Imprimir un rango
# # # print(nombres[0:2]) # Sin incluir el indice 2
# # # # Ir del inicio de la lista al indice  (sin incluirlo)
# # # print(nombres[:3])
# # # # Desde el indice indicado hasta el final
# # # print(nombres[1:])
# # # # Cambiar un valor de la lista
# # # nombres[3] = 'Ivone'
# # # print(nombres)
# # #
# # # # Iterar una lista
# # # for nombre in nombres:
# # #     print(nombre)
# # # else:
# # #     print('No existen mas nombres en la lista')
# # #
# # # # Preguntar el largo de una lista
# # # print(len(nombres))
# # # # Agregar un elemento a la lista
# # # nombres.append('Lorenzo')
# # # print(nombres)
# # # # Insertar un elemento en un indice en específico
# # # nombres.insert(1, 'Octavio')
# # # print(nombres)
# # # # Remover un elemento de la lista
# # # nombres.remove('Octavio')
# # # print(nombres)
# # # # Remover el último valor agregado
# # # nombres.pop()
# # # print(nombres)
# # # # Eliminar un indice
# # # del nombres[0]
# # # print(nombres)
# # # # Limpiar lista
# # # nombres.clear()
# # # print(nombres)
# # # # Borrar la lista por completo
# # # del nombres
# # # print(nombres)
# #
# # # Sintaxis de range(inicio<opcional>, fin<requerido>, incremento<opcional>)
# #
# # # Ejercicio 1. Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
# # print('Rango de 0 a 10 con numero divisibles entre 3')
# # rango1 = range(0, 11, 1) # sintaxis reducida -> range(11)
# # for num in rango1:
# #     if num % 3 == 0:
# #         print(num)
# # else:
# #     print('Fin del primer rango')
# #
# # # Ejercicio 2. Crear un rango de números de de 2 a 6, e imprimirlos
# # print('Rango con valores de inicio = 2 y fin = 6')
# # rango2 = range(2,7,1)
# # for num in rango2:
# #     print(num)
# # else:
# #     print('Fin del segundo rango')
# #
# # # Ejercicio 3. Crear un rango de 3 a 10, pero ocn incremento de 2 en 2, en lugar de 1 en 1
# # print('Rango con valores de inicio = 3, fin = 10, incremento = 2')
# # rango3 = range(3,11,2)
# # for num in rango3:
# #     print(num)
# # else:
# #     print('Fin del tercer rango')
# # --------------------------------------------------------------------------------------------------
#
# # Ejercicio de TUPLAS
# # Definir una tupla
# frutas = ('Naranja', 'Platano', 'Guayaba')
# # Si la tupla solo tiene un valor, despues de este se debe agregar una , -> frutas('narajna',)
#
# print(frutas)
# # Conocer el largo de la tupla
# print(len(frutas))
# # Acceder a un elemento
# print(frutas[0])
# # Navegación inversa
# print(frutas[-1])
# # Acceder a un rango
# print(frutas[0:1]) # Sin incluir el ultimo indice
#
# # Recorrer elementos de una tupla
# for fruta in frutas:
#     print(fruta, end=' ') # Propiedad de print para que la impresion no de saltos de linea en varios elementos
#
# # Las tuplas son imutables, osea que no pueden agregarse valores o modificar sus valores
# # Cambiar el valor de una tupla (no se puede)
# # frutas[0] = 'Pera'
# # print(frutas)
# frutaLista = list(frutas) # Convertir una tupla a una lista para poder modificar su información
# frutaLista[0] = 'Pera'
# frutas = tuple(frutaLista) # Convertir una lista a una tupla
# print('\n',frutas)
# # Eliminar la tupla
# del frutas
# print(frutas)

# Dada la siguiente tupla,
# crear una lista que solo incluya los números menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
for num in tupla:
    if num < 5:
        lista.append(num)

print(lista)