def hamiltonian_cycle(graph):
    size = len(graph)
    if not size:
        return None
    path = [0]
    visited = [False] * size
    visited[0] = True

    def search():
        if len(path) == size:
            return graph[path[-1]][path[0]] != 0
        for vertex in range(1, size):
            if not visited[vertex] and graph[path[-1]][vertex] != 0:
                visited[vertex] = True
                path.append(vertex)
                if search():
                    return True
                path.pop()
                visited[vertex] = False
        return False

    return path + [0] if search() else None


def main():
    graph = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1], [0, 1, 0, 0, 1], [1, 1, 0, 0, 1], [0, 1, 1, 1, 0]]
    cycle = hamiltonian_cycle(graph)
    if cycle:
        print("Hamiltonian cycle found:", *cycle)
    else:
        print("No Hamiltonian cycle found.")


if __name__ == "__main__":
    main()
