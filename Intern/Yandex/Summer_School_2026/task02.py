import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])

    seq1 = input_data[1:n+1]
    seq2 = input_data[n+1:2*n+1]
    
    parent = {}
    value = {}

    def find(i):
        if i not in parent:
            parent[i] = i
            return i
            
        root = i
        while parent[root] != root:
            root = parent[root]
            
        curr = i
        while curr != root:
            nxt = parent[curr]
            parent[curr] = root
            curr = nxt
            
        return root
        
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        
        if root_i != root_j:
            val_i = value.get(root_i)
            val_j = value.get(root_j)

            if val_i is not None and val_j is not None and val_i != val_j:
                return False

            parent[root_i] = root_j

            if val_j is None and val_i is not None:
                value[root_j] = val_i
                
        return True

    for i in range(n):
        u = seq1[i]
        v = seq2[i]
        
        u_is_digit = u.isdigit()
        v_is_digit = v.isdigit()
        
        if u_is_digit and v_is_digit:
            if u != v:
                print("NO")
                return
                
        elif u_is_digit and not v_is_digit:
            root = find(v)
            val = value.get(root)
            if val is not None and val != u:
                print("NO")
                return
            value[root] = u
            
        elif not u_is_digit and v_is_digit:
            root = find(u)
            val = value.get(root)
            if val is not None and val != v:
                print("NO")
                return
            value[root] = v
            
        else:
            if not union(u, v):
                print("NO")
                return

    print("YES")

if __name__ == '__main__':
    solve()
