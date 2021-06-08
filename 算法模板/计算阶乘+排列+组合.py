class Permutation:
    def __init__(self, mod=10 ** 9 + 7):
        self._mod = mod
        self._size = 0

        self._factorial = [1]  # 阶乘缓存列表 : self.fact[i] = i!
        self._factorial_inv = [1]  # 阶乘的乘法逆元缓存列表

    def factorial(self, n):
        """计算阶乘"""
        if n > self._size:
            for i in range(self._size + 1, n + 1):
                self._factorial.append((self._factorial[-1] * i) % self._mod)
                self._factorial_inv.append(pow(self._factorial[-1], self._mod - 2, self._mod))
            self._size = n
        return self._factorial[n]

    def arrange(self, n, m):
        """排列数公式(n>=m)"""
        return self.factorial(n) // self.factorial(n - m)

    def comb(self, n, m):
        """组合数公式(n>=m)"""
        return self.arrange(n, m) // self.factorial(m)


if __name__ == "__main__":
    permutation = Permutation()
    print(permutation.factorial(5))  # 120
    print(permutation.arrange(4, 2))  # 12
    print(permutation.comb(6, 2))  # 15
