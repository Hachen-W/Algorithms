def solution():
    n, m = map(int, input().split())
    MOD = 10**9 + 7
    first_pair_ways = (m * (m - 1)) % MOD

    if n == 1:
        return first_pair_ways

    next_pair_multiplier = (m**2 - 3 * m + 3) % MOD
    total_ways = (first_pair_ways * pow(next_pair_multiplier, n - 1, MOD)) % MOD

    return total_ways


if __name__ == '__main__':
    print(solution())
