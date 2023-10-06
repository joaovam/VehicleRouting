import igraph as graph
import routing

def main():
    edge = []
    for i in range(0, 10):
        for j in range(i + 1, 10):
            edge.append((i, j))

    g = graph.Graph(10, edge)

    g.es['peso'] = [12, 11, 7, 10, 10, 9, 8, 6, 12,
                    8, 5, 9, 12, 14, 16, 17, 22,
                    9, 15, 17, 8, 18, 14, 22,
                    7, 9, 11, 12, 12, 17,
                    3, 17, 7, 15, 18,
                    18, 6, 15, 15,
                    16, 8, 16,
                    11, 11,
                    10]

    demands = [10, 15, 18, 17, 3, 5, 9, 4, 6]

    routing.solveRouting(g, demands)

if __name__ == '__main__':
    main()
