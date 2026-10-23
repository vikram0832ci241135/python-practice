import heapq


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


def main():
    adjacency = [[(1, 4), (2, 1)], [(0, 4), (2, 2), (3, 5)], [(0, 1), (1, 2), (3, 8), (4, 10)], [(1, 5), (2, 8), (4, 2)], [(2, 10), (3, 2)]]
    print("Shortest distances from source 0:")
    for vertex, distance in enumerate(dijkstra(adjacency, 0)):
        print(f"{vertex} -> {distance}")


if __name__ == "__main__":
    main()
