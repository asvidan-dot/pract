class MathAlgorithms:
    # 1. Sieve of Eratosthenes (Easy)
    @staticmethod
    def sieve_of_eratosthenes(n: int) -> list:
        if n < 2: return []
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for p in range(2, int(n**0.5) + 1):
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
        return [p for p, is_prime in enumerate(primes) if is_prime]

    # 2. Greatest Common Divisor (Easy)
    @staticmethod
    def gcd_recursive(a: int, b: int) -> int:
        return a if b == 0 else MathAlgorithms.gcd_recursive(b, a % b)

    @staticmethod
    def gcd_iterative(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    # 3. Power Function (Medium)
    @staticmethod
    def fast_power(x: float, n: int) -> float:
        if n == 0: return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        
        res = 1.0
        while n > 0:
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2
        return res

    # 4. Square Root (Medium)
    @staticmethod
    def square_root(x: int) -> int:
        if x < 2: return x
        left, right = 1, x // 2
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

    # 5. Factorial Trailing Zeroes (Easy)
    @staticmethod
    def trailing_zeroes(n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count

if __name__ == "__main__":
    algo = MathAlgorithms()

    print("--- ДЕМОНСТРАЦІЯ РОБОТИ АЛГОРИТМІВ ---")
    
    # Task 1
    n_sieve = 30
    print(f"1. Sieve of Eratosthenes (n={n_sieve}): {algo.sieve_of_eratosthenes(n_sieve)}")
    
    # Task 2
    a, b = 48, 18
    print(f"2. GCD of {a} and {b}: Recursive={algo.gcd_recursive(a, b)}, Iterative={algo.gcd_iterative(a, b)}")
    
    # Task 3
    base, exp = 2, -3
    print(f"3. Power {base}^{exp} = {algo.fast_power(base, exp)}")
    
    # Task 4
    val = 10
    print(f"4. Square root of {val} (floor): {algo.square_root(val)}")
    
    # Task 5
    n_fact = 100
    print(f"5. Trailing zeroes in {n_fact}!: {algo.trailing_zeroes(n_fact)}")
    print("--------------------------------------")