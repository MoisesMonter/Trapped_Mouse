
def Labirinto():


    labirinto_visivel =[[0,0,1,1,1,0,1,1,0,1],
                        [1,0,1,0,0,0,1,1,0,1],
                        [0,0,0,0,1,1,0,0,0,1],
                        [1,0,1,0,0,0,0,1,1,1],
                        [1,0,1,0,1,0,1,1,0,1],
                        [1,1,1,0,0,0,0,0,0,1],
                        ]
    labirinto=[]
    for linha in labirinto_visivel:
        aux=[]
        for coluna in linha:
            aux.append(str(coluna))
        labirinto.append(aux)
    return labirinto
