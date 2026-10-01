def floyd_warshall(distances):
    result = [row[:] for row in distances]
    for middle in range(len(result)):
        for start in range(len(result)):
            for end in range(len(result)):
                result[start][end] = min(result[start][end], result[start][middle] + result[middle][end])
    return result


def main():
    infinity = 10**9
    distances = [[0, 3, infinity, 5], [2, 0, infinity, 4], [infinity, 1, 0, 6], [infinity, infinity, 2, 0]]
    print("Floyd-Warshall matrix:")
    for row in floyd_warshall(distances):
        print(*row)


if __name__ == "__main__":
    main()
