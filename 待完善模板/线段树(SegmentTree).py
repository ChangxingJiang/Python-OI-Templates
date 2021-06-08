# --*-- coding:GBK -- * --


"""线段树 (Segment Tree) (Segment Tree)

核心思想（Lazy思想）：对整个结点进行的操作，先在结点上做标记，而并非真正执行，直到根据查询操作的需要分成两部分

【操作说明】

【参数说明】
self.N = 线段树的数组长度
self.H = 线段树的高度
self.update_fn = 更新线段树的函数
self.query_fn = 查询线段树的函数
self.tree = [0] * (2 * N)  # 线段树数组
self.lazy = [0] * N  # 线段树lazy属性

【方法说明】
SegmentTree(N, update_fn, query_fn) 构造一棵长度为N的线段树
_apply(x, val)
_pull(x) 计算叶节点x及其祖先节点的值（计算lazy属性）
query(l, r) 查询从l到r的值

【类说明】
SegmentTree = 基于两个数组实现的线段树

"""


class SegmentTree(object):
    def __init__(self, N, update_fn, query_fn):
        self.N = N
        self.update_fn = update_fn
        self.query_fn = query_fn

        # 计算线段树的高度
        self.H = 1
        while (1 << self.H) < N:
            self.H += 1

        # 初始化线段树数组和lazy属性数组（lazy属性对应所有内部节点）
        self.tree = [0] * (2 * N)
        self.lazy = [0] * N

    def _apply(self, x, val):
        """计算x的值，并将x的子节点的计算填写到lazy属性中"""
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.N:
            self.lazy[x] = self.update_fn(self.lazy[x], val)  # 每个节点的lazy属性都是给子节点用的

    def _pull(self, x):
        """计算叶节点x及其祖先节点的值"""
        while x > 1:
            x >>= 1
            self.tree[x] = self.query_fn(self.tree[x * 2], self.tree[x * 2 + 1])
            self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

    def _push(self, x):
        """从根节点向下计算x的祖先节点的lazy属性中的值"""
        for h in range(self.H, 0, -1):
            y = x >> h
            if self.lazy[y]:
                self._apply(y * 2, self.lazy[y])
                self._apply(y * 2 + 1, self.lazy[y])
                self.lazy[y] = 0

    def update(self, l, r, h):
        # 计算L和R对应的叶节点坐标
        l += self.N
        r += self.N

        # 从叶节点开始向上更新值
        L0, R0 = l, r
        while l <= r:
            print("更新区域:", l, r, "->", l & 1, r & 1)
            if l & 1 == 1:
                self._apply(l, h)
                l += 1
            if r & 1 == 0:
                self._apply(r, h)
                r -= 1
            print("当前更新:", self.tree, self.lazy)
            l >>= 1
            r >>= 1

        # 计算叶节点x及其祖先节点的值
        self._pull(L0)
        self._pull(R0)

        print("更新完成", self.tree, self.lazy)

    def query(self, l, r):
        """查询从L到R（开闭区间）的值"""

        # 计算L和R对应的叶节点坐标
        l += self.N
        r += self.N

        # 计算从根节点向下计算x的祖先节点的lazy属性中的值（将lazy属性中的值计算到节点中）
        self._push(l)
        self._push(r)

        # 查询指定范围的和
        ans = 0
        while l <= r:
            print(l, r, "->", l & 1, r & 1)
            if l & 1 == 1:
                ans = self.query_fn(ans, self.tree[l])
                l += 1
            if r & 1 == 0:
                ans = self.query_fn(ans, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return ans


if __name__ == "__main__":
    def sum_(a, b):
        return a + b


    st = SegmentTree(8, sum_, sum_)
    print(st.update(3, 5, 1))
    # print(st.query(2, 5))
    # print(st.query(3, 5))
