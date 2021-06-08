class PrimeFactorDecompositioner:
    """质因数分解计算器"""

    def __init__(self, size):
        """size=支持分解的最大数"""
        self.size = size
        self.primes = self.get_primes(int(pow(self.size, 0.5)) + 1)  # 计算需要的质因数列表

    def get_prime_factors(self, x):
        """计算x的质因数列表（如果同一个质因数有多个，则返回多个）"""
        res = []
        for prime in self.primes:
            if prime > x:
                break
            while x % prime == 0:
                res.append(prime)
                x //= prime
        if x > 1:
            res.append(x)
        return res

    @staticmethod
    def get_primes(n: int) -> list:
        if n < 2:
            return []

        num_list = [True] * n
        num_list[0], num_list[1] = False, False

        for i in range(2, int(pow(n, 0.5)) + 1):
            if num_list[i]:  # 如果i为质数(不是任何质数的倍数)
                num_list[i * i::i] = [False] * ((n - i * i - 1) // i + 1)  # 因为要包含i*i所以需要+1；因为n不在列表里，所以需要-1

        return [i for i in range(n) if num_list[i]]
