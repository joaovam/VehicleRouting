import igraph as graph


class Rota:
    def __init__(self):
        self.rotas = []
        self.demanda = 0
        self.custo = 0

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
        # print(i, "route and demand:", x[0], "gain:", x[1])
        i += 1

    routes = list()
    for r in gain:
        #print(r)
        routes.append(r[0])
    i = 0
    while i < len(routes):
        curr = routes[i]
        j = 0
        while j < len(routes):
            print(i, j, len(routes))
            target = routes[j]
            if check_fusion(curr, target):
                remove_demand = common_member(curr.rotas, target.rotas)

                total_demand = (curr.demanda + target.demanda) - demands[remove_demand - 1]
                print("check: ", curr, target, "demand: ", total_demand)

                if total_demand < 40:
                    fusion_route = Rota()
                    fusion_route.rotas = makes_fusion(curr.rotas, target.rotas)

                    fusion_route.demanda = total_demand
                    routes.remove(target)
                    routes.remove(curr)
                    print(routes[i])
                    curr = fusion_route
                    routes.append(curr)

                    print(fusion_route)
            j += 1
        i += 1
    return routes


def verify_routes(routes: list[Rota], n):
    c = routes.copy()
    c = sorted(c, key=lambda x: len(x.rotas), reverse=True)

    supplied = [False] * (n + 1)
    solution = []
    should_append = False
    for r in c:
        for x in r.rotas:
            if not supplied[x]:
                supplied[x] = True
                should_append = True

        if should_append:
            solution.append(r)
        should_append = False
    return solution


def check_fusion(x: Rota, y: Rota):
    n2 = y.rotas

    skip = True

    for n1 in x.rotas:
        if n1 not in n2:
            skip = False

    if not skip:
        for n1 in x.rotas:
            if n1 == n2[0] or n1 == n2[len(n2) - 1]:
                return True
    # print(x, "X", y, skip)
    return False


def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    if a_set & b_set:
        return (a_set & b_set).pop()
    else:
        return 0


def makes_fusion(a, b):
    solution = []
    if a[0] == b[0]:
        solution.extend(b)
        solution.extend(a[1:])
    elif a[0] == b[len(b) - 1]:
        solution.extend(b)
        solution.extend(a[1:])
    elif a[len(a) - 1] == b[0]:
        solution.extend(a)
        solution.extend(b[1:])
    else:
        solution.extend(a)
        b = b[:-1]
        b.reverse()
        solution.extend(b)

    return f(solution)


def f(seq):  # Order preserving
    ''' Modified version of Dave Kirby solution '''
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]
