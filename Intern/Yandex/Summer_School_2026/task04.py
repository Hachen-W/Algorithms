import sys
from collections import defaultdict
from operator import itemgetter


def solution():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    patterns = input_data[2:]

    groups = defaultdict(lambda: defaultdict(int))
    for p in patterns:
        mask = 0
        for i, c in enumerate(p):
            if c != '?':
                mask |= (1 << i)
        groups[mask][p] += 1

    active_masks = list(groups.keys())
    n_masks = len(active_masks)
    
    ans = 0

    for pat_counts in groups.values():
        for count in pat_counts.values():
            if count >= 2:
                ans += count * (count - 1) // 2

    memo = {mask: {} for mask in active_masks}
    
    def get_proj(mask, sub_mask):
        mask_memo = memo[mask]
        if sub_mask in mask_memo:
            return mask_memo[sub_mask]

        indices = [i for i in range(m) if (sub_mask & (1 << i))]
        mask_groups = groups[mask]
        res = defaultdict(int)

        if not indices:
            res[()] = sum(mask_groups.values())
        elif len(indices) == 1:
            idx = indices[0]
            for p, count in mask_groups.items():
                res[p[idx]] += count
        else:
            getter = itemgetter(*indices)
            for p, count in mask_groups.items():
                res[getter(p)] += count
                
        mask_memo[sub_mask] = res
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

            d2_get = dict2.get
            for proj_tuple, count in dict1.items():
                c2 = d2_get(proj_tuple)
                if c2:
                    ans += count * c2

    print(ans)

if __name__ == '__main__':
    solution()
