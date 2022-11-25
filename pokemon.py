import pandas
import numpy

arbol_nombres = None
arbol_tipo = None
arbol_numero = None

class Pokemon(object):
    
    def __init__(self, nombre, numero, tipo, debilidad):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo
        self.debilidad = debilidad

    def __str__(self):
       return self.nombre + ' ' + str(self.numero) + ' ' + self.tipo + ' ' + self.debilidad

tipo = ['agua', 'fuego', 'tierra', 'electrico']
debil = ['agua', 'fuego', 'tierra', 'electrico', 'Jolteon', 'Lycanroc', 'Tyrantum']
nombre = ['Bulbasaur', 'Charmander', 'Pikachu', 'Ivysaur', 'Charmeleon', 'Charizard', 'Squirtle', 'wartortle', 'Venusaur']

for i in range (0, len(nombre)):
    pokemon = Pokemon(nombre[i], randint(1, 100), choice(tipo), choice(debil))
    arbol_nombres = insertar_nodo(arbol_nombres, [pokemon, pokemon.nombre])
    arbol_tipo = insertar_nodo(arbol_tipo, [pokemon, pokemon.tipo])
    arbol_numero = insertar_nodo(arbol_numero, [pokemon, pokemon.numero])

def inorden_numero(raiz):
    if(raiz is not None):
        inorden_numero(raiz.izq)
        print(raiz.info[1], raiz.info[0])
        inorden_numero(raiz.der)
print('Listado en orden por número:')
inorden_numero(arbol_numero)
print()

def busqueda_proximidad_poke(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[1][0:len(buscado)] == buscado):
            print(raiz.info[1])
        busqueda_proximidad_poke(raiz.izq, buscado)
        busqueda_proximidad_poke(raiz.der, buscado)

x = input('Ingrese el nombre parcial de pokemon a buscar:')
print('Todos los pokemons con ese nombre parcial:')
busqueda_proximidad_poke(arbol_nombres, x)
print()

def busqueda_proximidad_poke2(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[1][0:len(buscado)] == buscado):
            print(raiz.info[0].nombre)
        busqueda_proximidad_poke2(raiz.izq, buscado)
        busqueda_proximidad_poke2(raiz.der, buscado)

x = input('Ingrese el tipo de pokemon a buscar:')
print('Todos los pokemons de un tipo:')
busqueda_proximidad_poke2(arbol_tipo, x.lower())
print()

def inorden_numero2(raiz):
    if(raiz is not None):
        inorden_numero2(raiz.izq)
        print(raiz.info[0])
        inorden_numero2(raiz.der)

print('Listado en orden creciente numérico de pokemons:')
inorden_numero2(arbol_numero)
print()

def inorden_nombre(raiz):
    if(raiz is not None):
        inorden_nombre(raiz.izq)
        print(raiz.info[0])
        inorden_nombre(raiz.der)

print('Listado en orden creciente alfabético de pokemons:')
inorden_nombre(arbol_nombres)
print()

def por_nivel_nombre(raiz):
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        print(nodo.info[0])
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        if(nodo.der is not None):
            arribo(cola, nodo.der)
    
print('Listado en orden por nivel de pokemons:')
por_nivel_nombre(arbol_nombres)
print()

def busqueda_proximidad_poke3(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[0].debilidad[0:len(buscado)] == buscado):
            print(raiz.info[0].nombre)
        busqueda_proximidad_poke3(raiz.izq, buscado)
        busqueda_proximidad_poke3(raiz.der, buscado)

print('Debiles contra Jolteon: ')
busqueda_proximidad_poke3(arbol_nombres, 'Jolteon')
print()

print('Debiles contra Lycanroc: ')
busqueda_proximidad_poke3(arbol_nombres, 'Lycanroc')
print()

print('Debiles contra Tyrantrum: ')
busqueda_proximidad_poke3(arbol_nombres, 'Tyrantrum')
print()

cont = 0

def inorden_tipo(raiz, cont):
    if(raiz is not None):
        if raiz.info[0].tipo == 'fuego':
            cont += 1
        inorden_tipo(raiz.izq, cont)
        print(raiz.info[0].nombre, raiz.info[0].tipo)
        inorden_tipo(raiz.der, cont)
    return cont

print('Pokemons y su tipo:')
cont = inorden_tipo(arbol_nombres, cont)
print()

print('Cantidad del tipo fuego:',cont)

class nodoArbol(object):

    def __init__(self, info, nrr = None):
        self.izq = None
        self.der = None
        self.info = info
        self.nrr = nrr


class nodoArbolHuffman(object):
    
    def __init__(self, info, valor):
        self.izq = None
        self.der = None
        self.info = info
        self.valor = valor

class nodoArbolGreek(object):
    
    def __init__(self, info, madre, descipcion=None):
        self.izq = None
        self.der = None
        self.info = info
        self.madre = madre
        self.descripcion = descipcion

class nodoArbolMarvel(object):

    def __init__(self, nombre, heroe):
        self.izq = None
        self.der = None
        self.nombre = nombre
        self.heroe = heroe


def insertar_nodo(raiz, dato, nrr=None):
    if(raiz is None):
        raiz = nodoArbol(dato, nrr)
    else:
        if(raiz.info > dato):
            raiz.izq = insertar_nodo(raiz.izq, dato, nrr)
        else:
            raiz.der = insertar_nodo(raiz.der, dato, nrr)
    return raiz

def insertar_nodo_morse(raiz, dato):
    if(raiz is None):
        raiz = nodoArbol(dato)
    else:
        if(raiz.info[0] > dato[0]):
            raiz.izq = insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = insertar_nodo(raiz.der, dato)
    return raiz


def inorden(raiz):
    if(raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


from Archivos import leer

def inorden_lightsaber(raiz, archivo):
    if(raiz is not None):
        inorden_lightsaber(raiz.izq, archivo)
        jedi = leer(archivo, raiz.nrr)
        if(jedi[4].find('green') > -1):
            print(raiz.info, jedi[4])
        inorden_lightsaber(raiz.der, archivo)


def inorden_altura(raiz, archivo):
    if(raiz is not None):
        inorden_altura(raiz.izq, archivo)
        personaje = leer(archivo, raiz.nrr)
        if(personaje.altura > 1.00):
            print(raiz.info, personaje.altura)
        inorden_altura(raiz.der, archivo)


def inorden_peso(raiz, archivo):
    if(raiz is not None):
        inorden_peso(raiz.izq, archivo)
        personaje = leer(archivo, raiz.nrr)
        if(personaje.peso < 75):
            print(raiz.info, personaje.peso)
        inorden_peso(raiz.der, archivo)


def postorden(raiz):
    if(raiz is not None):
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)

def preorden(raiz):
    if(raiz is not None):
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def por_nivel(raiz):
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        print(nodo.info)
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        if(nodo.der is not None):
            arribo(cola, nodo.der)


def busqueda(raiz, buscado):
    if(raiz is not None):
        if(raiz.info == buscado):
            return raiz
        else:
            if(raiz.info > buscado):         
                return busqueda(raiz.izq, buscado)
            else:
                return busqueda(raiz.der, buscado)

def busqueda_nario(raiz, buscado, pos):
    if(raiz is not None):
        if(raiz.info == buscado):
            pos.append(raiz)
            return
        busqueda_nario(raiz.izq, buscado, pos)
        busqueda_nario(raiz.der, buscado, pos)

def busqueda_proximidad(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[0:len(buscado)] == buscado):
            print(raiz.info)
        busqueda_proximidad(raiz.izq, buscado)
        busqueda_proximidad(raiz.der, buscado)

def arbol_vacio(raiz):
    return raiz is None

def remplazar(raiz):
    """Determina el nodo que remplazará al que se elimina."""
    aux = None
    if(raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux

def eliminar_nodo(raiz, clave):
    x = None
    if(raiz is not None):
        if(clave < raiz.info):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif(clave > raiz.info):
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if(raiz.izq is None):
                raiz = raiz.der
            elif(raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.info = aux.info
    return raiz, x

def insertar_nario(padre, hijo):
    if(padre.izq is None):
        #print('insertar hijo de', padre.info)
        padre.izq = hijo
    else:
        aux = padre.izq
        while(aux.der is not None):
            aux = aux.der
        #print('insertar hno de', aux.info)
        aux.der = hijo

def por_nivel_nario(raiz):
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        print(nodo.info)
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        hno = nodo.der
        while(hno is not None):
            print(hno.info)
            if(hno.izq is not None):
                arribo(cola, hno.izq)
            hno = hno.der
            
# arbol = None

# arbol = insertar_nodo(arbol, 5)
# arbol = insertar_nodo(arbol, 3)
# arbol = insertar_nodo(arbol, 4)
# arbol = insertar_nodo(arbol, 7)
# arbol = insertar_nodo(arbol, 9)
# arbol = insertar_nodo(arbol, 0)
# arbol = insertar_nodo(arbol, 1)
# arbol = insertar_nodo(arbol, 6)

# arbol = insertar_nodo(arbol, 7)
# arbol = insertar_nodo(arbol, 7)

# 3 5
# cantp, canti = 0, 0

def contar(raiz, cp, ci):
    if(raiz is not None):
        if(raiz.info % 2 == 0):
            cp += 1
        else:
            ci += 1
        cp, ci = contar(raiz.izq, cp, ci)
        cp, ci = contar(raiz.der, cp, ci)
    return cp, ci

# cantp, canti = contar(arbol, cantp, canti)
# print(cantp, canti)


def contar_repetidos(raiz, buscado, cant):
    if(raiz is not None):
        if(raiz.info == buscado):
            cant += 1
            cant = contar_repetidos(raiz.der, buscado, cant)
        else:
            cant = contar_repetidos(raiz.izq, buscado, cant)
    return cant

# cant = 0
# bus = 7
# pos = busqueda(arbol, bus)
# if(pos is not None):
#     print('asdas', contar_repetidos(pos, bus, cant))
# else:
#     print(0)



#arbol, dato = eliminar_nodo(arbol, 5)
# por_nivel(arbol)

# pos = busqueda(arbol, 20)
# if(pos is not None):
#     print(pos.info)
# else:
#     print(pos)

# from random import randint

# for i in range(0, 1000):
#     arbol = insertar_nodo(arbol, randint(0, 50000))

# print('barrido inorden')
# inorden(arbol)
# a = input()
# print('barrido preorden')
# preorden(arbol)
# a = input()
# print('barrido postorden')
# postorden(arbol)
# a = input()
# print('barrido por nivel')
# por_nivel(arbol)
# # a = input()

# buscado = int(input('ingrese valor buscado '))
# pos = busqueda(arbol, buscado)

# if(pos is not None):
#     print('esta')
# else:
#     print('no esta')

class nodoArbol(object):

    def __init__(self, info, nrr = None):
        self.izq = None
        self.der = None
        self.info = info
        self.nrr = nrr
        self.altura = 0

class nodoArbolHuffman(object):
    
    def __init__(self, info, valor):
        self.izq = None
        self.der = None
        self.info = info
        self.valor = valor

def altura(raiz):
    """Devuelve la altura de un nodo."""
    if(raiz is None):
        return -1
    else:
        return raiz.altura


def actualizaraltura(raiz):
    """Actualiza la altura de un nodo."""
    if(raiz is not None):
        alt_izq = altura(raiz.izq)
        alt_der = altura(raiz.der)
        raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) + 1


def insertar_nodo(raiz, dato, nrr=None):
    "Agrega un elemnto al arbol"
    if(raiz is None):
        raiz = nodoArbol(dato, nrr)
    else:
        if(raiz.info[1] > dato[1]):
            raiz.izq = insertar_nodo(raiz.izq, dato, nrr)
        else:
            raiz.der = insertar_nodo(raiz.der, dato, nrr)
    raiz = balancear(raiz)
    actualizaraltura(raiz)
    return raiz

def inorden(raiz):
    "Realiza un recorrido del arbol, mostrando la informacion"
    if(raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


def inorden_lightsaber(raiz, archivo):
    if(raiz is not None):
        inorden_lightsaber(raiz.izq, archivo)
        jedi = leer(archivo, raiz.nrr)
        if(jedi[4].find('green') > -1):
            print(raiz.info, jedi[4])
        inorden_lightsaber(raiz.der, archivo)

def inorden_name(raiz, archivo, jedis):
    if(raiz is not None):
        inorden_name(raiz.izq, archivo, jedis)
        jedi = leer(archivo, raiz.nrr)
        jedis.append(jedi)
        inorden_name(raiz.der, archivo, jedis)

def postorden(raiz):
    "Recorrido de orden posterior, mostrando la informacion"
    if(raiz is not None):
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)

def preorden(raiz):
    "Recorrido de orden previo, mostrando la informacion"
    if(raiz is not None):
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)

def padre(raiz, buscado):
    if(raiz is not None):
        if((raiz.der is not None and raiz.der.info == buscado) or (raiz.izq is not None and raiz.izq.info == buscado)):
            print('El padre de buscado es', raiz.info)
        else:
            padre(raiz.izq, buscado)
            padre(raiz.der, buscado)

def por_nivel(raiz):
    "Muestra la informacion del arbol, por nivel"
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        print(nodo.info)
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        if(nodo.der is not None):
            arribo(cola, nodo.der)


def busqueda(raiz, buscado):
    "Devuelve un puntero que apunta al nodo que tieneel elemnento buscado"
    if(raiz is not None):
        if(raiz.info == buscado):
            return raiz
        else:
            if(raiz.info > buscado):         
                return busqueda(raiz.izq, buscado)
            else:
                return busqueda(raiz.der, buscado)

def busqueda_proximidad(raiz, buscado):
    2
    if(raiz is not None):
        if(raiz.info[0:len(buscado)] == buscado):
            print(raiz.info)
        busqueda_proximidad(raiz.izq, buscado)
        busqueda_proximidad(raiz.der, buscado)

def busqueda_proximidad_archivo(raiz, buscado, archivo):
    if(raiz is not None):
        if(raiz.info[0:len(buscado)] == buscado):
            libro = leer(archivo, raiz.nrr)
            print(libro.isbn, libro.cant, libro.titulo, libro.autores)
        busqueda_proximidad_archivo(raiz.izq, buscado, archivo)
        busqueda_proximidad_archivo(raiz.der, buscado, archivo)

def busqueda_archivo(raiz, cantidad, archivo):
    if(raiz is not None):
        libro = leer(archivo, raiz.nrr)
        if(libro.cant > cantidad):
            print(libro.isbn, libro.cant, libro.titulo, libro.autores)
        busqueda_archivo(raiz.izq, cantidad, archivo)
        busqueda_archivo(raiz.der, cantidad, archivo)

def arbol_vacio(raiz):
    return raiz is None

def remplazar(raiz):
    """Determina el nodo que remplazará al que se elimina."""
    aux = None
    if(raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux


def eliminar_nodo(raiz, clave):
    "Elimina un elemento del arbol y lo devuelve si lo envuentra"
    x = None
    if(raiz is not None):
        if(clave < raiz.info):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif(clave > raiz.info):
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if(raiz.izq is None):
                raiz = raiz.der
            elif(raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.info = aux.info
    raiz = balancear(raiz)
    actualizaraltura(raiz)
    return raiz, x

def hijo_der(arbol):
    if(arbol.der is None):
        print(arbol.der)
    else:
        print('Hijo derecho:', arbol.der.info)

def hijo_izq(arbol):
    if(arbol.izq is None):
        print(arbol.izq)
    else:
        print('Hijo izquierdo:', arbol.izq.info)

def rotar_simple(raiz, control):
    """Realiza una rotación simple de nodos a la derecha o a la izquierda."""
    if control:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz
    actualizaraltura(raiz)
    actualizaraltura(aux)
    raiz = aux
    return raiz

def rotar_doble(raiz, control):
    """Realiza una rotación doble de nodos a la derecha o a la izquierda."""
    if control:
        raiz.izq = rotar_simple(raiz.izq, False)
        raiz = rotar_simple(raiz, True)
    else:
        raiz.der = rotar_simple(raiz.der, True)
        raiz = rotar_simple(raiz, False)
    return raiz


def balancear(raiz):
    """Determina que rotación hay que hacer para balancear el árbol."""
    if(raiz is not None):
        if(altura(raiz.izq)-altura(raiz.der) == 2):
            if(altura(raiz.izq.izq) >= altura(raiz.izq.der)):
                raiz = rotar_simple(raiz, True)
            else:
                raiz = rotar_doble(raiz, True)
        elif(altura(raiz.der)-altura(raiz.izq) == 2):
            if(altura(raiz.der.der) >= altura(raiz.der.izq)):
                raiz = rotar_simple(raiz, False)
            else:
                raiz = rotar_doble(raiz, False)
    return raiz

def cortar_por_nivel(raiz, bosque):
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        if(altura(nodo) == 7 ):
            bosque.append(nodo.izq)
            bosque.append(nodo.der)
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        if(nodo.der is not None):
            arribo(cola, nodo.der)

def contar_a(raiz, cantidad):
    if(raiz is not None):
        contar_a(raiz.izq, cantidad)
        contar_a(raiz.der, cantidad)
        cantidad[0] += 1
        

# 3 5
# cantp, canti = 0, 0

# def contar(raiz, cp, ci):
#     if(raiz is not None):
#         if(raiz.info % 2 == 0):
#             cp += 1
#         else:
#             ci += 1
#         cp, ci = contar(raiz.izq, cp, ci)
#         cp, ci = contar(raiz.der, cp, ci)
#     return cp, ci

# cantp, canti = contar(arbol, cantp, canti)
# print(cantp, canti)


# def contar_repetidos(raiz, buscado, cant):
#     if(raiz is not None):
#         if(raiz.info == buscado):
#             cant += 1
#             cant = contar_repetidos(raiz.der, buscado, cant)
#         else:
#             cant = contar_repetidos(raiz.izq, buscado, cant)
#     return cant