def prim_mst(graph):
    vertex_count = len(graph)
    if not vertex_count:
        return [], 0
    keys = [float("inf")] * vertex_count
    parents = [-1] * vertex_count
    in_tree = [False] * vertex_count
    keys[0] = 0
    for _ in range(vertex_count):
        vertex = min((i for i in range(vertex_count) if not in_tree[i]), key=lambda i: keys[i], default=None)
        if vertex is None or keys[vertex] == float("inf"):
            break
        in_tree[vertex] = True
        for neighbor, weight in enumerate(graph[vertex]):
            if weight and not in_tree[neighbor] and weight < keys[neighbor]:
                keys[neighbor] = weight
                parents[neighbor] = vertex
    edges = [(parents[i], i, graph[i][parents[i]]) for i in range(1, vertex_count) if parents[i] != -1]
    return edges, sum(edge[2] for edge in edges)


def main():
    graph = [[0, 2, 0, 6, 0], [2, 0, 3, 8, 5], [0, 3, 0, 0, 7], [6, 8, 0, 0, 9], [0, 5, 7, 9, 0]]
    edges, total = prim_mst(graph)
    print("Prim MST edges:")
    for first, second, weight in edges:
        print(f"{first} - {second} (weight {weight})")
    print("Total weight:", total)


if __name__ == "__main__":
    main()
