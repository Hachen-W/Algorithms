import heapq


def solution():
    a, b, n = map(int, input().split())

    candidates = []
    for _ in range(n):
        x, y = map(int, input().split())
        candidates.append((x, y))

    candidates.sort(key=lambda item: item[0] - item[1], reverse=True)

    pref_X = [0] * (n + 1)
    suff_Y = [0] * (n + 1)

    if a > 0:
        heap_x = []
        current_sum_x = 0
        for i in range(n):
            x = candidates[i][0]
            heapq.heappush(heap_x, x)
            current_sum_x += x

            if len(heap_x) > a:
                current_sum_x -= heapq.heappop(heap_x)

            if len(heap_x) == a:
                pref_X[i + 1] = current_sum_x

    if b > 0:
        heap_y = []
        current_sum_y = 0
        for i in range(n - 1, -1, -1):
            y = candidates[i][1]
            heapq.heappush(heap_y, y)
            current_sum_y += y
            if len(heap_y) > b:
                current_sum_y -= heapq.heappop(heap_y)
            if len(heap_y) == b:
                suff_Y[i] = current_sum_y

    max_total_skills = 0

    for i in range(a, n - b + 1):
        max_total_skills = max(max_total_skills, pref_X[i] + suff_Y[i])

    return max_total_skills


if __name__ == '__main__':
    print(solution())
