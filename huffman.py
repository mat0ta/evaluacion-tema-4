class nodo_arbol():
    def __init__(self, valor, freq, padre=None, derecha=None, izquierda=None, codigo=None):
        self.valor = valor
        self.freq = freq
        self.padre = padre
        self.derecha = derecha
        self.izquierda = izquierda
        self.codigo = codigo

def sort(lista, n):
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j].freq > lista[j+1].freq :
                lista[j], lista[j+1] = lista[j+1], lista[j]

def make_huffman(lista):
    lista
    while len(lista) >1:
        sort(lista, len(lista))
        padre = nodo_arbol(None, None)
        padre.izquierda = lista[0]
        padre.derecha = lista[1]
        padre.freq = padre.derecha.freq + padre.izquierda.freq
        lista[0].padre = padre
        lista[1].padre = padre
        lista.append(padre)
        lista.pop(0)
        lista.pop(0)
    return lista[0]

def make_code(nodo, code):
    if nodo.valor != None:
        nodo.codigo = code
        return
    make_code(nodo.izquierda, code + '0')
    make_code(nodo.derecha, code + '1')

def make_table(nodo, table):
    if nodo.valor != None:
        table[nodo.valor] = nodo.codigo
        return
    make_table(nodo.izquierda, table)
    make_table(nodo.derecha, table)

def encode(texto, table):
    texto_codificado = ''
    for letra in texto:
        texto_codificado += table[letra]
    return texto_codificado

def decode(texto_codificado, nodo):
    texto_decodificado = ''
    nodo_actual = nodo
    for bit in texto_codificado:
        if bit == '0':
            nodo_actual = nodo_actual.izquierda
        else:
            nodo_actual = nodo_actual.derecha
        if nodo_actual.valor != None:
            texto_decodificado += nodo_actual.valor
            nodo_actual = nodo
    return texto_decodificado

def print_tree(nodo, nivel):
    if nodo.valor != None:
        print(' ' * nivel + nodo.valor)
        return
    print_tree(nodo.izquierda, nivel + 1)
    print_tree(nodo.derecha, nivel + 1)

def print_tree(raiz):    
    if raiz is not None:
        print_tree(raiz.izquierda)  
        print(raiz.freq)
        print_tree(raiz.derecha)
    else:
        pass

def main():
    texto = 'AMTTMATMAMTATM13010313013AMMTTFF'
    lista = [nodo_arbol('A', 0.2), nodo_arbol('F', 0.17), nodo_arbol('1', 0.13), nodo_arbol('3', 0.21), nodo_arbol('0', 0.05), nodo_arbol('M', 0.09), nodo_arbol('T', 0.15)]
    huffman = make_huffman(lista)
    make_code(huffman, '')
    table = {}
    make_table(huffman, table)
    print(table)
    print_tree(huffman)
    texto_codificado = encode(texto, table)
    print(texto_codificado)
    texto_decodificado = decode(texto_codificado, huffman)
    print(texto_decodificado)

if __name__ == '__main__':
    main()