import sys

def solution():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
        
    patterns = input_data[2:]

    groups = [{} for _ in range(1 << m)]
    for p in patterns:
        mask = 0
        for i in range(m):
            if p[i] != '?':
                mask |= (1 << i)
        groups[mask][p] = groups[mask].get(p, 0) + 1

    proj_count = [[{} for _ in range(1 << m)] for _ in range(1 << m)]
    
    for mask in range(1 << m):
        if not groups[mask]:
            continue
        for s, count in groups[mask].items():
            sub_mask = mask
            while True:
                proj_chars = []
                for i in range(m):
                    if sub_mask & (1 << i):
                        proj_chars.append(s[i])
                    else:
                        proj_chars.append('?')
                proj_s = "".join(proj_chars)

                if proj_s in proj_count[mask][sub_mask]:
                    proj_count[mask][sub_mask][proj_s] += count
                else:
                    proj_count[mask][sub_mask][proj_s] = count
                    
                if not sub_mask:
                    break
                sub_mask = (sub_mask - 1) & mask
                
    ans = 0

    for mask in range(1 << m):
        for count in groups[mask].values():
            if count >= 2:
                ans += count * (count - 1) // 2

    for mask1 in range(1 << m):
        if not groups[mask1]:
            continue
        for mask2 in range(mask1 + 1, 1 << m):
            if not groups[mask2]:
                continue

            common_mask = mask1 & mask2
            
            dict1 = proj_count[mask1][common_mask]
            dict2 = proj_count[mask2][common_mask]

            if len(dict1) > len(dict2):
                dict1, dict2 = dict2, dict1
                
            for proj_s, count in dict1.items():
                if proj_s in dict2:
                    ans += count * dict2[proj_s]
                    
    print(ans)

if __name__ == '__main__':
    solution()
