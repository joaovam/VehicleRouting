import igraph as graph


# class Route:
#     __init__():


def solveRouting(g: graph.Graph, demands):

    basic_costs = {} # edges going from node 0 to the others

    for e in g.es:

        print(e.source, e.target)
