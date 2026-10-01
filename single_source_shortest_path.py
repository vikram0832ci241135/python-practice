import heapq
import sys

INF = float("inf")


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


def dijkstra(vertex_count, adjacency, source):
    distances = [INF] * (vertex_count + 1)
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


def bellman_ford(vertex_count, edges, source):
    distances = [INF] * (vertex_count + 1)
    distances[source] = 0
    for _ in range(vertex_count - 1):
        changed = False
        for edge in edges:
            if distances[edge.source] != INF and distances[edge.target] > distances[edge.source] + edge.weight:
                distances[edge.target] = distances[edge.source] + edge.weight
                changed = True
        if not changed:
            break
    has_negative_cycle = any(
        distances[edge.source] != INF
        and distances[edge.target] > distances[edge.source] + edge.weight
        for edge in edges
    )
    return distances, has_negative_cycle


def main():
    data = sys.stdin.buffer.read().split()
    if len(data) < 2:
        return
    values = iter(map(int, data))
    vertex_count = next(values)
    edge_count = next(values)
    adjacency = [[] for _ in range(vertex_count + 1)]
    edges = []
    has_negative_weight = False
    for _ in range(edge_count):
        source, target, weight = next(values), next(values), next(values)
        adjacency[source].append((target, weight))
        edges.append(Edge(source, target, weight))
        has_negative_weight |= weight < 0
    source = next(values)

    if has_negative_weight:
        distances, has_negative_cycle = bellman_ford(vertex_count, edges, source)
        if has_negative_cycle:
            print("Negative cycle detected")
            return
    else:
        distances = dijkstra(vertex_count, adjacency, source)

    for vertex in range(1, vertex_count + 1):
        print("INF" if distances[vertex] == INF else int(distances[vertex]))


if __name__ == "__main__":
    main()
