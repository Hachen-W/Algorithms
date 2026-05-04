import sys

def solution():
    # Быстрое чтение всего ввода разом
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    patterns = input_data[2:]

    groups = {}
    for p in patterns:
        mask = 0
        for i in range(m):
            if p[i] != '?':
                mask |= (1 << i)
        
        if mask not in groups:
            groups[mask] = {}
        groups[mask][p] = groups[mask].get(p, 0) + 1

    active_masks = list(groups.keys())
    n_masks = len(active_masks)
    
    ans = 0

    for pat_counts in groups.values():
        for count in pat_counts.values():
            if count >= 2:
                ans += count * (count - 1) // 2

    memo = {mask: {} for mask in active_masks}
    
    def get_proj(mask, sub_mask):
        if sub_mask in memo[mask]:
            return memo[mask][sub_mask]

        indices = [i for i in range(m) if (sub_mask & (1 << i))]
                
        res = {}
        for p, count in groups[mask].items():
            proj = tuple(p[i] for i in indices)
            res[proj] = res.get(proj, 0) + count
            
        memo[mask][sub_mask] = res
        return res

    for i in range(n_masks):
        mask1 = active_masks[i]
        for j in range(i + 1, n_masks):
            mask2 = active_masks[j]

            common_mask = mask1 & mask2

            dict1 = get_proj(mask1, common_mask)
            dict2 = get_proj(mask2, common_mask)

            if len(dict1) > len(dict2):
                dict1, dict2 = dict2, dict1
                
            for proj_tuple, count in dict1.items():
                if proj_tuple in dict2:
                    ans += count * dict2[proj_tuple]

    print(ans)

if __name__ == '__main__':
    solution()
