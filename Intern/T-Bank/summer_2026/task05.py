def solution():
    n = int(input().strip())
    s = input().strip()

    dp = [[0] * n for _ in range(n)]

    def get_match_cost(x, y):
        x_is_toi = x in ('T', 'O', 'I')
        y_is_toi = y in ('T', 'O', 'I')

        if x_is_toi and y_is_toi:
            return 0 if x == y else 1
        elif x_is_toi or y_is_toi:
            return 1
        else:
            return 2

    for L in range(1, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1

            if L == 1:
                dp[i][j] = 0 if s[i] in ('T', 'O', 'I') else 1

            elif L == 2:
                dp[i][j] = min(
                    dp[i+1][j] + 1,
                    dp[i][j-1] + 1,
                    get_match_cost(s[i], s[j])
                )

            else:
                dp[i][j] = min(
                    dp[i+1][j] + 1,
                    dp[i][j-1] + 1,
                    dp[i+1][j-1] + get_match_cost(s[i], s[j])
                )

    return dp[0][n - 1]


if __name__ == '__main__':
    print(solution())
