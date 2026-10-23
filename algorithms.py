import heapq


def optimal_merge_patterns(files):
    heap = list(files)
    heapq.heapify(heap)
    total_cost = 0
    while len(heap) > 1:
        cost = heapq.heappop(heap) + heapq.heappop(heap)
        total_cost += cost
        heapq.heappush(heap, cost)
    return total_cost


def huffman_codes(frequencies):
    heap = []
    order = 0
    for character, frequency in sorted(frequencies.items()):
        heapq.heappush(heap, (frequency, order, (character, None, None)))
        order += 1
    while len(heap) > 1:
        left_frequency, _, left = heapq.heappop(heap)
        right_frequency, _, right = heapq.heappop(heap)
        node = (None, left, right)
        heapq.heappush(heap, (left_frequency + right_frequency, order, node))
        order += 1
    codes = {}

    def visit(node, code):
        character, left, right = node
        if left is None and right is None:
            codes[character] = code
            return
        visit(left, code + "0")
        visit(right, code + "1")

    if heap:
        visit(heap[0][2], "")
    return codes


class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, first, second):
        first_root = self.find(first)
        second_root = self.find(second)
        if first_root == second_root:
            return False
        if self.rank[first_root] < self.rank[second_root]:
            first_root, second_root = second_root, first_root
        self.parent[second_root] = first_root
        if self.rank[first_root] == self.rank[second_root]:
            self.rank[first_root] += 1
        return True


def kruskal_mst(edges, vertex_count):
    selected = []
    total = 0
    sets = DisjointSet(vertex_count)
    for first, second, weight in sorted(edges, key=lambda edge: edge[2]):
        if sets.union(first, second):
            selected.append((first, second, weight))
            total += weight
    return selected, total


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


def dijkstra(adjacency, source):
    distances = [float("inf")] * len(adjacency)
    distances[source] = 0
    queue = [(0, source)]
    while queue:
        distance, vertex = heapq.heappop(queue)
        if distance != distances[vertex]:
            continue
        for neighbor, weight in adjacency[vertex]:
            candidate = distance + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                heapq.heappush(queue, (candidate, neighbor))
    return distances


def floyd_warshall(distances):
    result = [row[:] for row in distances]
    for middle in range(len(result)):
        for start in range(len(result)):
            for end in range(len(result)):
                result[start][end] = min(result[start][end], result[start][middle] + result[middle][end])
    return result


def tsp_dp(graph):
    size = len(graph)
    if size == 0:
        return float("inf")
    full_mask = (1 << size) - 1
    unreachable = float("inf")
    dp = [[unreachable] * size for _ in range(1 << size)]
    dp[1][0] = 0
    for mask in range(1, 1 << size):
        for current in range(size):
            if not mask & (1 << current) or dp[mask][current] == unreachable:
                continue
            for neighbor in range(size):
                if mask & (1 << neighbor) or graph[current][neighbor] == 0:
                    continue
                next_mask = mask | (1 << neighbor)
                dp[next_mask][neighbor] = min(dp[next_mask][neighbor], dp[mask][current] + graph[current][neighbor])
    return min((dp[full_mask][vertex] + graph[vertex][0] for vertex in range(1, size) if graph[vertex][0]), default=unreachable)


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
    print("Python Programs for Various Algorithms")
    print("1. Optimal Merge Patterns\n2. Huffman Coding\n3. Minimum Spanning Tree (Kruskal)")
    print("4. Minimum Spanning Tree (Prim)\n5. Single Source Shortest Path (Dijkstra)")
    print("6. Floyd-Warshall Algorithm\n7. Travelling Salesman Problem (TSP)")
    print("8. Hamiltonian Cycle Problem\n9. Exit")
    while True:
        try:
            choice = int(input("Enter your choice: "))
        except (ValueError, EOFError):
            break
        if choice == 9:
            break
        if choice == 1:
            print("Optimal merge cost:", optimal_merge_patterns([5, 10, 20, 30]))
        elif choice == 2:
            print("Huffman Codes:")
            for character, code in sorted(huffman_codes(dict(zip("abcdef", [5, 9, 12, 13, 16, 45]))).items()):
                print(f"{character} -> {code}")
        elif choice == 3:
            edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4), (1, 2, 8)]
            selected, total = kruskal_mst(edges, 4)
            print("Kruskal MST edges:")
            for first, second, weight in selected:
                print(f"{first} - {second} (weight {weight})")
            print("Total weight:", total)
        elif choice == 4:
            graph = [[0, 2, 0, 6, 0], [2, 0, 3, 8, 5], [0, 3, 0, 0, 7], [6, 8, 0, 0, 9], [0, 5, 7, 9, 0]]
            selected, total = prim_mst(graph)
            print("Prim MST edges:")
            for first, second, weight in selected:
                print(f"{first} - {second} (weight {weight})")
            print("Total weight:", total)
        elif choice == 5:
            adjacency = [[(1, 4), (2, 1)], [(0, 4), (2, 2), (3, 5)], [(0, 1), (1, 2), (3, 8), (4, 10)], [(1, 5), (2, 8), (4, 2)], [(2, 10), (3, 2)]]
            print("Shortest distances from source 0:")
            for vertex, distance in enumerate(dijkstra(adjacency, 0)):
                print(f"{vertex} -> {distance}")
        elif choice == 6:
            inf = 10**9
            matrix = [[0, 3, inf, 5], [2, 0, inf, 4], [inf, 1, 0, 6], [inf, inf, 2, 0]]
            print("Floyd-Warshall matrix:")
            for row in floyd_warshall(matrix):
                print(*row)
        elif choice == 7:
            graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
            print("Minimum TSP cost:", tsp_dp(graph))
        elif choice == 8:
            graph = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1], [0, 1, 0, 0, 1], [1, 1, 0, 0, 1], [0, 1, 1, 1, 0]]
            cycle = hamiltonian_cycle(graph)
            print("Hamiltonian cycle found: " + " ".join(map(str, cycle)) if cycle else "No Hamiltonian cycle found.")
        else:
            print("Invalid choice.")
        print()


if __name__ == "__main__":
    main()
