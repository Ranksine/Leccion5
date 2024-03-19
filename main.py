# Ejercicios de LISTAS
# Definir una lista de tipo str
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
# Imprimir lista de nombres
print(nombres)
# Acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])
# Acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])

# Imprimir un rango
print(nombres[0:2]) # Sin incluir el indice 2
# Ir del inicio de la lista al indice  (sin incluirlo)
print(nombres[:3])
# Desde el indice indicado hasta el final
print(nombres[1:])
# Cambiar un valor de la lista
nombres[3] = 'Ivone'
print(nombres)

# Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista')

# Preguntar el largo de una lista
print(len(nombres))
# Agregar un elemento a la lista
nombres.append('Lorenzo')
print(nombres)
# Insertar un elemento en un indice en específico
nombres.insert(1, 'Octavio')
print(nombres)
# Remover un elemento de la lista
nombres.remove('Octavio')
print(nombres)
# Remover el último valor agregado
nombres.pop()
print(nombres)
# Eliminar un indice
del nombres[0]
print(nombres)
# Limpiar lista
nombres.clear()
print(nombres)
# Borrar la lista por completo
del nombres
print(nombres)

# Sintaxis de range(inicio<opcional>, fin<requerido>, incremento<opcional>)

# Ejercicio 1. Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
print('Rango de 0 a 10 con numero divisibles entre 3')
rango1 = range(0, 11, 1) # sintaxis reducida -> range(11)
for num in rango1:
    if num % 3 == 0:
        print(num)
else:
    print('Fin del primer rango')

# Ejercicio 2. Crear un rango de números de de 2 a 6, e imprimirlos
print('Rango con valores de inicio = 2 y fin = 6')
rango2 = range(2,7,1)
for num in rango2:
    print(num)
else:
    print('Fin del segundo rango')

# Ejercicio 3. Crear un rango de 3 a 10, pero ocn incremento de 2 en 2, en lugar de 1 en 1
print('Rango con valores de inicio = 3, fin = 10, incremento = 2')
rango3 = range(3,11,2)
for num in rango3:
    print(num)
else:
    print('Fin del tercer rango')
# --------------------------------------------------------------------------------------------------

# Ejercicio de TUPLAS
# Definir una tupla
frutas = ('Naranja', 'Platano', 'Guayaba')
# Si la tupla solo tiene un valor, despues de este se debe agregar una , -> frutas('narajna',)

print(frutas)
# Conocer el largo de la tupla
print(len(frutas))
# Acceder a un elemento
print(frutas[0])
# Navegación inversa
print(frutas[-1])
# Acceder a un rango
print(frutas[0:1]) # Sin incluir el ultimo indice

# Recorrer elementos de una tupla
for fruta in frutas:
    print(fruta, end=' ') # Propiedad de print para que la impresion no de saltos de linea en varios elementos

# Las tuplas son imutables, osea que no pueden agregarse valores o modificar sus valores
# Cambiar el valor de una tupla (no se puede)
# frutas[0] = 'Pera'
# print(frutas)
frutaLista = list(frutas) # Convertir una tupla a una lista para poder modificar su información
frutaLista[0] = 'Pera'
frutas = tuple(frutaLista) # Convertir una lista a una tupla
print('\n',frutas)
# Eliminar la tupla
del frutas
print(frutas)

# Dada la siguiente tupla,
# crear una lista que solo incluya los números menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
for num in tupla:
    if num < 5:
        lista.append(num)

print(lista)

# Ejercicios de colecciones SET
# Set
planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
# Conocer largo
print(len(planetas))
# Revisar si un elemento está presente
print('Marte' in planetas)
# Agregar un elemento
planetas.add('Tierra')
print(planetas)
# EN SET no se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)
# Eliminar elementos posiblemente arrojando un error(No se pueden eliminar elementos que no existen)
planetas.remove('Tierra')
print(planetas)
# Eliminar ejemento sin arrojar error (en caso de que el elemento no se encuentre)
planetas.discard('Jupiters')
print(planetas)
# Limpiar set
planetas.clear()
print(planetas)
# Eliminar el set
del planetas
print(planetas)

# Ejecicios de colecciones Diccionarios
# dict (key, value)
diccionario = {
    'IDE':'Integrated Development Enviroment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}
print(diccionario)
# Largo
print(len(diccionario))
# Acceder a un elemento (key)
print(diccionario['IDE'])
# Otra forma de recuperar un elemento
print(diccionario.get('OOP'))
# Modificar elementos
diccionario['IDE'] = 'integrated development enviroment'
print(diccionario)
# Recorrer los elementos
for termino in diccionario:
    print(termino)

for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

    for valor in diccionario.values():
        print(valor)

# Comprobar existencia de algun elemento
print('IDE' in diccionario)
# Agregar un elemento al diccionario
diccionario['PK'] = 'Primary Key'
print(diccionario)
# Remover elemento
diccionario.pop('DBMS')
print(diccionario)
# Limpiar diccionario
diccionario.clear()
print(diccionario)
# Eliminar el diccionario
del diccionario
print(diccionario)