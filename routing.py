import igraph as graph

class Rota:
    def __init__(self):
        self.rotas = []
        self.demanda = 0

def solveRouting(g: graph.Graph, demands):

    basic_costs = {} # edges going from node 0 to the others
    #(Rota, ganho)

1. montar tabela de ganho
    1.1 ordenar tabela tendo como base o ganho ** só usar função sort

2. fusão das rotas, limitando pela demanda
    2.1 testar se fusão é valida
    2.2 efetuar a fusão, criar uma nova rota, atualizar a rota antiga e apaga as rotas utilizadas

    "1-2-3" |
    "5-6" |

    for e in g.es:
        I J S
            p0i + p0j - pij
        print(e.source, e.target, e["peso"])
