def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    iter = 5
    while iter * iter <= number:
        if number % iter == 0 or number % (iter + 2) == 0:
            return False
        iter += 6
    return True


def is_palindrome(number: int) -> bool:
    s = str(number)
    return s == s[::-1]


def calculate_S(number: int, primes: list[int]) -> int:
    min_prime = 0
    max_prime = 0

    for p in primes:
        if p * p > number:
            break
        if number % p == 0:
            min_prime = p
            break

    other = number // p
    if is_prime(other):
        max_prime = other
    else:
        max_prime = p
        for q in primes:
            if q * q > other:
                break
            if other % q == 0:
                cand = other // q
                if is_prime(cand):
                    max_prime = cand

    if min_prime == 0:
        return 0

    return min_prime + max_prime


def main():
    N = 400_000
    primes = []
    for number in range(2, N + 1):
        if is_prime(number):
            primes.append(number)

    count = 0
    number = 4_000_001

    print("N\tS")
    while count < 5:
        s = calculate_S(number, primes)
        if s > 50_000 and is_palindrome(s):
            print(number, s, sep="\t")
            count += 1
        number += 1


if __name__ == "__main__":
    main()
