def solution():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    if n == 1:
        print(x)
        return

    X_digits = []
    temp_x = x
    for i in range(n - 1):
        r = a[i+1] // a[i]
        X_digits.append(temp_x % r)
        temp_x //= r
    X_digits.append(temp_x)

    dp0 = X_digits[-1]
    dp1 = X_digits[-1] + 1

    for i in range(n - 2, -1, -1):
        r = a[i+1] // a[i]

        v0 = X_digits[i]
        cost0_0 = v0 + dp0 if v0 < r else float('inf')
        cost0_1 = max(0, r - v0) + dp1
        new_dp0 = min(cost0_0, cost0_1)

        v1 = X_digits[i] + 1
        cost1_0 = v1 + dp0 if v1 < r else float('inf')
        cost1_1 = max(0, r - v1) + dp1
        new_dp1 = min(cost1_0, cost1_1)

        dp0, dp1 = new_dp0, new_dp1

    return dp0


if __name__ == '__main__':
    print(solution())
