from collections import deque


def subgraph_isomorphism(graph1, graph2, start1, start2):
    visited1 = set()
    visited2 = set()
    queue1 = deque([(start1, start2)])
    visited1.add(start1)
    visited2.add(start2)

    while queue1:
        vertex1, vertex2 = queue1.popleft()

        for neighbor1 in graph1[vertex1]:
            is_isomorphic = False
            for neighbor2 in graph2[vertex2]:
                if neighbor1 not in visited1 and neighbor2 not in visited2:
                    queue1.append((neighbor1, neighbor2))
                    visited1.add(neighbor1)
                    visited2.add(neighbor2)
                    is_isomorphic = True
                    break
                elif neighbor1 in visited1 and neighbor2 in visited2:
                    is_isomorphic = True
                    break

            if not is_isomorphic:
                return False

    return True


if __name__ == '__main__':
    # Defina os dois subgrafos para verificar o isomorfismo
    graph1 = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['C']
    }

    graph2 = {
        'X': ['Y', 'Z'],
        'Y': ['X', 'W'],
        'Z': ['X', 'V'],
        'W': ['Y'],
        'V': ['Z']
    }

    # Defina os vértices de partida para cada subgrafo
    start1 = 'A'
    start2 = 'X'

    # Verifique o isomorfismo dos subgrafos
    is_isomorphic = subgraph_isomorphism(graph1, graph2, start1, start2)

    # Exiba o resultado
    if is_isomorphic:
        print("Os subgrafos são isomórficos.")
    else:
        print("Os subgrafos não são isomórficos.")



