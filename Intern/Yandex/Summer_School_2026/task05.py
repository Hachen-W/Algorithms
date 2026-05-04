import sys
from bisect import bisect_right

def solution():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    h = [0] * (n + 1)
    for i in range(1, n + 1):
        h[i] = int(input_data[i])

    A = [0] * (n + 1)
    B = [0] * (n + 1)
    
    vals_set = set()
    for j in range(1, n + 1):
        A[j] = h[j] - j
        B[j] = h[j] + j
        vals_set.add(A[j])
        vals_set.add(B[j])

    vals = sorted(list(vals_set))
    K = len(vals)

    BIT_A_count = [0] * (K + 1)
    BIT_A_sum = [0] * (K + 1)
    BIT_B_count = [0] * (K + 1)
    BIT_B_sum = [0] * (K + 1)

    total_A_count = total_A_sum = 0
    total_B_count = total_B_sum = 0

    for j in range(1, n + 1):
        idx = bisect_right(vals, B[j])
        i_bit = idx
        while i_bit <= K:
            BIT_B_count[i_bit] += 1
            BIT_B_sum[i_bit] += B[j]
            i_bit += i_bit & (-i_bit)
        total_B_count += 1
        total_B_sum += B[j]

    ans = float('inf')
    target = n // 2 + 1

    for i in range(1, n + 1):
        idx_b = bisect_right(vals, B[i])
        i_bit = idx_b
        while i_bit <= K:
            BIT_B_count[i_bit] -= 1
            BIT_B_sum[i_bit] -= B[i]
            i_bit += i_bit & (-i_bit)
        total_B_count -= 1
        total_B_sum -= B[i]

        idx_a = bisect_right(vals, A[i])
        i_bit = idx_a
        while i_bit <= K:
            BIT_A_count[i_bit] += 1
            BIT_A_sum[i_bit] += A[i]
            i_bit += i_bit & (-i_bit)
        total_A_count += 1
        total_A_sum += A[i]

        low = 1
        high = 2000000000
        x_opt = high
        
        while low <= high:
            mid = (low + high) // 2
            u = mid - i
            w = mid + i
            
            idx_u = bisect_right(vals, u)
            c_A = 0
            i_bit = idx_u
            while i_bit > 0:
                c_A += BIT_A_count[i_bit]
                i_bit -= i_bit & (-i_bit)
                
            idx_w = bisect_right(vals, w)
            c_B = 0
            i_bit = idx_w
            while i_bit > 0:
                c_B += BIT_B_count[i_bit]
                i_bit -= i_bit & (-i_bit)
                
            if c_A + c_B >= target:
                x_opt = mid
                high = mid - 1
            else:
                low = mid + 1

        L_i = i if i >= n - i + 1 else n - i + 1
        X = x_opt if x_opt > L_i else L_i

        u = X - i
        w = X + i

        idx_u = bisect_right(vals, u)
        cA_le = sA_le = 0
        i_bit = idx_u
        while i_bit > 0:
            cA_le += BIT_A_count[i_bit]
            sA_le += BIT_A_sum[i_bit]
            i_bit -= i_bit & (-i_bit)
            
        cA_gt = total_A_count - cA_le
        sA_gt = total_A_sum - sA_le
        cost_A = (u * cA_le - sA_le) + (sA_gt - u * cA_gt)

        idx_w = bisect_right(vals, w)
        cB_le = sB_le = 0
        i_bit = idx_w
        while i_bit > 0:
            cB_le += BIT_B_count[i_bit]
            sB_le += BIT_B_sum[i_bit]
            i_bit -= i_bit & (-i_bit)
            
        cB_gt = total_B_count - cB_le
        sB_gt = total_B_sum - sB_le
        cost_B = (w * cB_le - sB_le) + (sB_gt - w * cB_gt)

        total_cost = cost_A + cost_B
        if total_cost < ans:
            ans = total_cost

    print(ans)

if __name__ == '__main__':
    solution()
