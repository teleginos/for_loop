from typing import List


def search_for_prime_numbers(*args) -> None:
    for number in args:
        flag = True
        if number == 1:
            primes.append(number)
            continue
        for num in range(2, number):
            if number % num == 0:
                not_primes.append(number)
                flag = False
                break
        if flag:
            primes.append(number)


numbers = [number for number in range(1, 16)]

primes: List = []
not_primes: List = []
if __name__ == '__main__':
    search_for_prime_numbers(*numbers)
    print(f"Primes: {primes}")
    print(f"Not Primes: {not_primes}")
