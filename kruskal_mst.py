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


def main():
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4), (1, 2, 8)]
    selected, total = kruskal_mst(edges, 4)
    print("Kruskal MST edges:")
    for first, second, weight in selected:
        print(f"{first} - {second} (weight {weight})")
    print("Total weight:", total)


if __name__ == "__main__":
    main()
