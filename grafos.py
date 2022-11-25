class grafo_siete_maravillas():
    def __init__(self):
        self.vertices = [['Cristo Redentor', 'Brasil', 'Arquitectonica'], ['Coliseo', 'Italia', 'Arquitectonica'], ['Taj Mahal', 'India', 'Arquitectonica'], ['Machu Picchu', 'Peru', 'Arquitectonica'], ['Petra', 'Jordania', 'Arquitectonica'], ['Chichen Itza', 'Mexico', 'Arquitectonica'], ['La Gran Muralla China', 'China', 'Arquitectonica']]
        self.aristas = [('Cristo Redentor', 'Coliseo', 1), ('Cristo Redentor', 'Taj Mahal', 1), ('Cristo Redentor', 'Machu Picchu', 1), ('Cristo Redentor', 'Petra', 1), ('Cristo Redentor', 'Chichen Itza', 1), ('Cristo Redentor', 'La Gran Muralla China', 1), ('Coliseo', 'Taj Mahal', 1), ('Coliseo', 'Machu Picchu', 1), ('Coliseo', 'Petra', 1), ('Coliseo', 'Chichen Itza', 1), ('Coliseo', 'La Gran Muralla China', 1), ('Taj Mahal', 'Machu Picchu', 1), ('Taj Mahal', 'Petra', 1), ('Taj Mahal', 'Chichen Itza', 1), ('Taj Mahal', 'La Gran Muralla China', 1), ('Machu Picchu', 'Petra', 1), ('Machu Picchu', 'Chichen Itza', 1), ('Machu Picchu', 'La Gran Muralla China', 1), ('Petra', 'Chichen Itza', 1), ('Petra', 'La Gran Muralla China', 1), ('Chichen Itza', 'La Gran Muralla China', 1)]
        self.grafo = {}
        for vertice in self.vertices:
            self.grafo[vertice[0]] = []
        for arista in self.aristas:
            self.grafo[arista[0]].append(arista[1])
            self.grafo[arista[1]].append(arista[0])
    def get_arbol_de_expansion_minima(self):
        arbol = []
        arbol.append(self.aristas[0])
        for arista in self.aristas:
            if arista[0] not in arbol and arista[1] not in arbol:
                arbol.append(arista)
        return arbol
    def get_si_tienen_maravilla(self, pais):
        for vertice in self.vertices:
            if vertice[1] == pais:
                return 'Si, en ' + str(pais) + ' se encuentra el ' + str(vertice[0]) + ', que es una maravilla ' + str(vertice[2])
        return 'No, no tienen ninguna maravilla'
    def get_si_tienen_mas_de_una_maravilla(self, pais):
        contador = 0
        for vertice in self.vertices:
            if vertice[1] == pais:
                contador += 1
        if contador > 1:
            return 'Si, en ' + str(pais) + ' se encuentran ' + str(contador) + ' maravillas'
        return 'No, en ' + str(pais) + ' solo se encuentra una maravilla'
    def get_si_pais_con_maravillas_del_mismo_tipo(self, pais, tipo):
        count_arqui = 0
        count_natu = 0
        for vertice in self.vertices:
            if vertice[1] == pais and vertice[2] == tipo:
                if tipo == 'Arquitectonica':
                    count_arqui += 1
                else:
                    count_natu += 1
        return 'En ' + str(pais) + ' hay ' + str(count_arqui) + ' maravillas arquitectonicas y ' + str(count_natu) + ' maravillas naturales'

    def get_vertices(self):
        return self.vertices
    def get_aristas(self):
        return self.aristas
    def get_grafo(self):
        return self.grafo
    def get_grado(self, vertice):
        return len(self.grafo[vertice])
    def get_adyacentes(self, vertice):
        return self.grafo[vertice]


if __name__ == '__main__':
    grafo = grafo_siete_maravillas()
    print('Vertices: {}'.format(grafo.get_vertices()))
    print('Aristas: {}'.format(grafo.get_aristas()))
    print('Grafo: {}'.format(grafo.get_grafo()))
    print(grafo.get_si_pais_con_maravillas_del_mismo_tipo('Mexico', 'Arquitectonica'))
    print(grafo.get_si_tienen_maravilla('Mexico'))
    print(grafo.get_si_tienen_mas_de_una_maravilla('Mexico'))
    print(grafo.get_arbol_de_expansion_minima())

