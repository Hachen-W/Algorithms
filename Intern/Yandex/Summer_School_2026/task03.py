import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        print("-2")
        return
        
    n = int(input_data[0])

    points = []
    idx = 1
    for _ in range(n):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
            
        points.append((abs(x), abs(y)))
        idx += 2

    points.sort(key=lambda p: (p[0], p[1]))
    
    filtered = []
    for p in points:
        while filtered and filtered[-1][1] <= p[1]:
            filtered.pop()
        filtered.append(p)
        
    n_filtered = len(filtered)
    dp = [0] * (n_filtered + 1)

    class CHT:
        def __init__(self):
            self.lines = []
            self.ptr = 0
            
        def check_pop(self, lA, lB, lC):
            mA, cA = lA
            mB, cB = lB
            mC, cC = lC
            return (cC - cB) * (mA - mB) <= (cB - cA) * (mB - mC)
            
        def add(self, m, c):
            line = (m, c)
            while len(self.lines) >= 2:
                if self.check_pop(self.lines[-2], self.lines[-1], line):
                    self.lines.pop()
                else:
                    break
            self.lines.append(line)
            
        def query(self, x):
            if self.ptr >= len(self.lines):
                self.ptr = max(0, len(self.lines) - 1)
            while self.ptr < len(self.lines) - 1:
                mB, cB = self.lines[self.ptr]
                mC, cC = self.lines[self.ptr+1]
                if (cC - cB) <= x * (mB - mC):
                    self.ptr += 1
                else:
                    break
            m, c = self.lines[self.ptr]
            return m * x + c

    cht = CHT()

    for i in range(1, n_filtered + 1):
        m = 4 * filtered[i-1][1]
        c = dp[i-1]
        cht.add(m, c)

        x_val = filtered[i-1][0]
        dp[i] = cht.query(x_val)
        
    print(dp[n_filtered])

if __name__ == '__main__':
    solve()
