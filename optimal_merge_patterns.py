import heapq


def optimal_merge_patterns(files):
    queue = list(files)
    heapq.heapify(queue)
    total_cost = 0
    while len(queue) > 1:
        cost = heapq.heappop(queue) + heapq.heappop(queue)
        total_cost += cost
        heapq.heappush(queue, cost)
    return total_cost


def main():
    print("Optimal Merge Cost =", optimal_merge_patterns([5, 10, 20, 30]))


if __name__ == "__main__":
    main()
