# -*-coding:UTF-8 -*-

"""树状数组 / 二叉索引树 (Binary Indexed Tree)

树状数组用于高效计算数列的前缀和、区间和。
它支持在O(logN)的时间内计算任意前缀和、区间和；同时支持在O(logN)的时间内修改单点值。

【时间复杂度】
构造实例：O(N)
计算元素的前缀和：O(logN)
计算两个元素的区间和：O(logN)
修改单个值：O(logN)

【操作说明】
单点修改 O(logN) : 输入下标x和增量d，将a[x]增加d
单点查询 O(logN) : 输入下标x，求出a[x]的值
区间查询 O(logN) : 输入下标x和y，求出a[x]和a[y]的和

【方法说明】
BIT(n) 构造一个长度为n的树状数组
update(i, x) 将数组中的第i个数更新为x
add(i, x) 将数组中第i个数增加x
range_add(l, r, x) 将数组中第l个数到第r个数分别加x
query(i) 查询数组中第i个数的前缀和
range_query(l, r) 查询数组中第l个到第r个数的区间和
_lowbit(x) 计算二进制中从最低位向高位中出现的第1个非0位对应的二进制数值

【变式说明】
BIT = 标准树状数组，支持：单点修改、单点查询、区间查询
RangeUpdateBIT = 第1种变式树状数组（差分数组），支持：单点修改、区间修改、单点查询
RangeQueryUpdateBIT = 第2种变式树状数组（差分数组），支持：单点修改、区间修改、单点查询、区间查询
BIT2D = 二维树状数组

参考文献：https://www.cnblogs.com/xenny/p/9739600.html

样例：
LeetCode0307 = 标准树状数组
LeetCode0308 = 二维树状数组
"""


class BIT:
    def __init__(self, n: int):
        self.n = n
        self._tree = [0] * (n + 1)

    @staticmethod
    def _lowbit(x):
        return x & (-x)

    def update(self, i: int, x: int):
        self.add(i, x - (self.query(i) - self.query(i - 1)))

    def add(self, i: int, x: int):
        while i <= self.n:
            self._tree[i] += x
            i += BIT._lowbit(i)

    def query(self, i: int) -> int:
        ans = 0
        while i > 0:
            ans += self._tree[i]
            i -= BIT._lowbit(i)
        return ans

    def range_query(self, l: int, r: int) -> int:
        return self.query(r) - self.query(l - 1)


class RangeUpdateBIT:
    def __init__(self, n: int):
        self.n = n
        self._tree = [0] * (n + 1)

    @staticmethod
    def _lowbit(x):
        return x & (-x)

    def update(self, i: int, x: int):
        self.add(i, x - (self.query(i) - self.query(i - 1)))

    def add(self, i: int, x: int):
        while i <= self.n:
            self._tree[i] += x
            i += RangeUpdateBIT._lowbit(i)

    def range_add(self, l: int, r: int, x: int):
        self.add(l, x)
        self.add(r + 1, -x)

    def query(self, i: int) -> int:
        ans = 0
        while i > 0:
            ans += self._tree[i]
            i -= RangeUpdateBIT._lowbit(i)
        return ans


class RangeQueryUpdateBIT:
    def __init__(self, n: int):
        self.n = n
        self._sum1 = [0] * (n + 1)  # 存储D[1]
        self._sum2 = [0] * (n + 1)  # 存储1*D[1]+2*D[2]

    @staticmethod
    def _lowbit(x):
        return x & (-x)

    def update(self, i: int, x: int):
        self.add(i, x - (self.query(i) - self.query(i - 1)))

    def add(self, i: int, x: int):
        t = i
        while i <= self.n:
            self._sum1[i] += x
            self._sum2[i] += x * (t - 1)
            i += RangeQueryUpdateBIT._lowbit(i)

    def range_add(self, l: int, r: int, x: int):
        self.add(l, x)
        self.add(r + 1, -x)

    def query(self, i: int) -> int:
        ans = 0
        t = i
        while i > 0:
            ans += t * self._sum1[i] - self._sum2[i]
            i -= RangeQueryUpdateBIT._lowbit(i)
        return ans

    def range_query(self, l: int, r: int):
        return self.query(r) - self.query(l - 1)


class BIT2D:
    def __init__(self, n1: int, n2: int):
        self.n1 = n1
        self.n2 = n2
        self._tree = [[0] * (n2 + 1) for _ in range(n1 + 1)]

    @staticmethod
    def _lowbit(x):
        return x & (-x)

    def update(self, i: int, j: int, x: int):
        now = self.query(i, j) - self.query(i - 1, j) - self.query(i, j - 1) + self.query(i - 1, j - 1)
        self.add(i, j, x - now)

    def add(self, i: int, j: int, x: int):
        i_lst, j_lst = [], []
        while i <= self.n1:
            i_lst.append(i)
            i += BIT2D._lowbit(i)
        while j <= self.n2:
            j_lst.append(j)
            j += BIT2D._lowbit(j)
        for ii in i_lst:
            for jj in j_lst:
                self._tree[ii][jj] += x

    def query(self, i: int, j: int) -> int:
        i_lst, j_lst = [], []
        while i > 0:
            i_lst.append(i)
            i -= BIT2D._lowbit(i)
        while j > 0:
            j_lst.append(j)
            j -= BIT2D._lowbit(j)
        ans = 0
        for ii in i_lst:
            for jj in j_lst:
                ans += self._tree[ii][jj]
        return ans

    def range_query(self, i1: int, j1: int, i2: int, j2: int) -> int:
        return self.query(i2, j2) - self.query(i2, j1 - 1) - self.query(i1 - 1, j2) + self.query(i1 - 1, j1 - 1)
