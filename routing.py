import igraph as graph


class Rota:
    def __init__(self):
        self.rotas = []
        self.demanda = 0

    def __str__(self):
        return f"{self.rotas}, {self.demanda}"


def solveRouting(g: graph.Graph, demands):
    basic_costs = {}  # edges going from node 0 to the others
    gain = []
    # (Rota, ganho)

    # 1. montar tabela de ganho
    #     1.1 ordenar tabela tendo como base o ganho ** só usar função sort
    #
    # 2. fusão das rotas, limitando pela demanda
    #     2.1 testar se fusão é valida
    #     2.2 efetuar a fusão, criar uma nova rota, atualizar a rota antiga e apaga as rotas utilizadas
    #
    #     "1-2-3" |
    #     "5-6" |
    #
    for e in g.es:
        if e.source == 0:
            basic_costs[e.target] = e["peso"]
        else:
            route = Rota()
            route.rotas.append(e.source)
            route.rotas.append(e.target)
            route.demanda = demands[e.source - 1] + demands[e.target - 1]

            profit = basic_costs[e.source] + basic_costs[e.target] - e["peso"]

            gain.append((route, profit))

    gain.sort(key=lambda x: x[1], reverse=True)

    for x in gain:
        print("route and demand:", x[0], "gain:", x[1])
