def solution():
    n = int(input().strip())

    prices = list(map(int, input().split()))

    if n <= 1:
        return 0

    left_profits = [0] * n
    min_price_so_far = prices[0]

    for i in range(1, n):
        min_price_so_far = min(min_price_so_far, prices[i])
        left_profits[i] = max(left_profits[i - 1], prices[i] - min_price_so_far)

    right_profits = [0] * n
    max_price_so_far = prices[-1]

    for i in range(n - 2, -1, -1):
        max_price_so_far = max(max_price_so_far, prices[i])
        right_profits[i] = max(right_profits[i + 1], max_price_so_far - prices[i])

    max_total_profit = 0
    for i in range(n):
        current_profit = left_profits[i] + right_profits[i]
        max_total_profit = max(max_total_profit, current_profit)

    return max_total_profit


if __name__ == '__main__':
    print(solution())
