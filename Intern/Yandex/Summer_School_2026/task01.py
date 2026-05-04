import sys
import heapq

def solution():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])

    heaps = {chr(i): [] for i in range(97, 123)} # от 'a' до 'z'
    
    idx = 2
    for _ in range(n):
        if idx >= len(input_data):
            break
        word = input_data[idx]
        idx += 1
        
        start_char = word[0]
        heaps[start_char].append((0, word))

    for char in heaps:
        if heaps[char]:
            heapq.heapify(heaps[char])
            
    results = []
    for _ in range(k):
        if idx >= len(input_data):
            break
        char = input_data[idx]
        idx += 1

        if heaps[char]:
            usage_count, word = heapq.heappop(heaps[char])
            results.append(word)
            heapq.heappush(heaps[char], (usage_count + 1, word))

    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solution()
