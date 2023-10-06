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
    i = 0
    for x in gain:
        print(i, "route and demand:", x[0], "gain:", x[1])
        i+=1

    for i in range(len(gain)):
        curr = gain[i]
        for j in range(i + 1, len(gain)):
            target = gain[j]
            if check_fusion(curr[0], target[0]):




def check_fusion(x: Rota, y: Rota):
    print(x, "X", y)
    n2 = y.rotas
    for n1 in x.rotas:
        if n1 == n2[0] or n1 == n2[len(n2) - 1]:
            return True

    return False
