import sys
from bisect import bisect_right


def solution():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    h = [int(x) for x in input_data[1:n+1]]

    A = [0] * (n + 1)
    B = [0] * (n + 1)
    
    vals_set = set()
    for j in range(n):
        val_h = h[j]
        aj = val_h - (j + 1)
        bj = val_h + (j + 1)
        A[j + 1] = aj
        B[j + 1] = bj
        vals_set.add(aj)
        vals_set.add(bj)

    vals = sorted(list(vals_set))
    K = len(vals)

    val_to_idx = {val: i for i, val in enumerate(vals, 1)}

    idx_A = [0] * (n + 1)
    idx_B = [0] * (n + 1)
    for j in range(1, n + 1):
        idx_A[j] = val_to_idx[A[j]]
        idx_B[j] = val_to_idx[B[j]]

    BIT_A_count = [0] * (K + 1)
    BIT_A_sum = [0] * (K + 1)
    BIT_B_count = [0] * (K + 1)
    BIT_B_sum = [0] * (K + 1)

    total_A_count = 0
    total_A_sum = 0
    total_B_count = n
    total_B_sum = 0

    for j in range(1, n + 1):
        idx = idx_B[j]
        BIT_B_count[idx] += 1
        BIT_B_sum[idx] += B[j]
        total_B_sum += B[j]

    for i in range(1, K + 1):
        nxt = i + (i & (-i))
        if nxt <= K:
            BIT_B_count[nxt] += BIT_B_count[i]
            BIT_B_sum[nxt] += BIT_B_sum[i]

    ans = 10**18
    target = n // 2 + 1
    bs_right = bisect_right

    max_h = max(h) if h else 0
    max_possible_x = max_h + n

    for i in range(1, n + 1):
        val_B = B[i]
        idx_b = idx_B[i]
        while idx_b <= K:
            BIT_B_count[idx_b] -= 1
            BIT_B_sum[idx_b] -= val_B
            idx_b += idx_b & (-idx_b)
        total_B_count -= 1
        total_B_sum -= val_B

        val_A = A[i]
        idx_a = idx_A[i]
        while idx_a <= K:
            BIT_A_count[idx_a] += 1
            BIT_A_sum[idx_a] += val_A
            idx_a += idx_a & (-idx_a)
        total_A_count += 1
        total_A_sum += val_A

        low = 0
        high = max_possible_x
        x_opt = high
        
        while low <= high:
            mid = (low + high) // 2
            u = mid - i
            w = mid + i
            
            c_A = 0
            idx_u = bs_right(vals, u)
            while idx_u > 0:
                c_A += BIT_A_count[idx_u]
                idx_u -= idx_u & (-idx_u)
                
            c_B = 0
            idx_w = bs_right(vals, w)
            while idx_w > 0:
                c_B += BIT_B_count[idx_w]
                idx_w -= idx_w & (-idx_w)
                
            if c_A + c_B >= target:
                x_opt = mid
                high = mid - 1
            else:
                low = mid + 1

        L_i = i if i >= n - i + 1 else n - i + 1
        X = x_opt if x_opt > L_i else L_i

        u = X - i
        w = X + i

        cA_le = 0
        sA_le = 0
        idx_u = bs_right(vals, u)
        while idx_u > 0:
            cA_le += BIT_A_count[idx_u]
            sA_le += BIT_A_sum[idx_u]
            idx_u -= idx_u & (-idx_u)
            
        cA_gt = total_A_count - cA_le
        sA_gt = total_A_sum - sA_le
        cost_A = (u * cA_le - sA_le) + (sA_gt - u * cA_gt)

        cB_le = 0
        sB_le = 0
        idx_w = bs_right(vals, w)
        while idx_w > 0:
            cB_le += BIT_B_count[idx_w]
            sB_le += BIT_B_sum[idx_w]
            idx_w -= idx_w & (-idx_w)
            
        cB_gt = total_B_count - cB_le
        sB_gt = total_B_sum - sB_le
        cost_B = (w * cB_le - sB_le) + (sB_gt - w * cB_gt)

        total_cost = cost_A + cost_B
        if total_cost < ans:
            ans = total_cost

    print(ans)


if __name__ == '__main__':
    solution()
