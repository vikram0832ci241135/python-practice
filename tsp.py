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


def main():
    graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    print("Minimum TSP cost =", tsp_dp(graph))


if __name__ == "__main__":
    main()
