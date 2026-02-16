def find_primes(n: int) -> str:
    """
       Find all prime numbers up to a given integer using the Sieve of Eratosthenes.

       Args:
           n (int): The upper limit (inclusive) for finding prime numbers.

       Returns:
           str: A space-separated string of prime numbers if any exist,
                otherwise the string 'No primes'.
       """
    if n <= 2:
        return 'No primes'
    candidates = set(range(2, n + 1))
    for number in range(2, int(n**0.5) + 1):
        if number in candidates:
            candidates -= set(range(number**2, n + 1, number))
    primes = map(str, sorted(candidates))
    return ' '.join(primes)


if __name__ == '__main__':
    n = int(input('Enter number: '))
    print(find_primes(n))
