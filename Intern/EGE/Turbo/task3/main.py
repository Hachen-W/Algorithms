def main():
    f = open('74869_35729177473081588_doc.txt')

    k = int(f.readline())
    n = int(f.readline())

    works = []
    for _ in range(n):
        start, end = map(int, f.readline().split())
        works.append((start, end))

    works.sort()

    curators = [0] * (k + 1)
    count = 0
    last_start = -1
    last_curator = 10**9

    for start, end in works:
        for i in range(1, k + 1):
            if curators[i] <= start:
                curators[i] = end + 1
                count += 1

                if start > last_start:
                    last_start = start
                    last_curator = i
                elif start == last_start:
                    last_curator = min(last_curator, i)

                break

    print(count, last_curator)


if __name__ == "__main__":
    main()
