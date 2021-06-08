"""
[Demo]
LeetCode 0699
"""


class SegmentTreeForMax:
    """求最大值线段树：区域查询和更新最大值"""

    class _Node:
        """线段树结点"""
        __slots__ = "start", "end", "val", "left", "right", "lazy"

        def __init__(self, start, end):
            self.start = start  # 左侧边界（包含）
            self.end = end  # 右侧边界（包含）
            self.left = None  # 结点左子结点
            self.right = None  # 结点右子节点
            self.val = 0  # 当前结点最小值
            self.lazy = 0  # 懒惰计算标签（即未计算的子结点最小值）

    def __init__(self, size):
        """初始化线段树实例"""
        self.root = self._Node(0, size)

    def _push_down(self, node):
        """计算当前结点的懒惰计算标签：更新子结点的值+更新子结点的懒惰计算标签+清空当前结点的懒惰计算标签"""
        if node.lazy != 0:
            node.left.val = max(node.left.val, node.lazy)
            node.left.lazy = max(node.left.lazy, node.lazy)
            node.right.val = max(node.right.val, node.lazy)
            node.right.lazy = max(node.right.lazy, node.lazy)
            node.lazy = 0

    def _update(self, node, pos1, pos2, data):
        """更新数据"""
        # 当前区间正好为当前结点的情况：即不需要继续分裂的情况
        if node.start == pos1 and node.end == pos2:
            node.val = max(node.val, data)
            node.lazy = max(node.lazy, data)

        # 当前区间为当前结点的部分的情况：即需要继续分裂的情况
        else:
            mid = (node.start + node.end) // 2

            # 创建两个子结点
            if node.left is None:
                node.left = self._Node(node.start, mid)
            if node.right is None:
                node.right = self._Node(mid + 1, node.end)

            # 计算当前结点的懒惰计算标签
            self._push_down(node)

            # 更新当前结点的值
            node.val = max(node.val, data)

            # 更新当前结点的子结点
            if pos2 <= mid:
                self._update(node.left, pos1, pos2, data)
            elif pos1 >= mid + 1:
                self._update(node.right, pos1, pos2, data)
            else:
                self._update(node.left, pos1, mid, data)
                self._update(node.right, mid + 1, pos2, data)

    def _query(self, node, start, end):
        """查询数据"""

        # 当前区间正好为当前结点的情况：即不需要继续分裂的情况
        if node.start == start and node.end == end:
            return node.val

        # 当前结点没有子结点的情况：即当前结点下所有位置的结果一致的情况
        elif node.left is None and node.right is None:
            return node.val

        # 当前区间为当前结点的部分的情况：即需要继续分裂的情况
        else:
            mid = (node.start + node.end) // 2

            # 创建两个子结点
            if node.left is None:
                node.left = self._Node(node.start, mid)
            if node.right is None:
                node.right = self._Node(mid + 1, node.end)

            # 计算当前结点的懒惰计算标签
            self._push_down(node)

            # 查询当前结果的最小值
            if end <= mid:
                return self._query(node.left, start, end)
            elif start >= mid + 1:
                return self._query(node.right, start, end)
            else:
                return max(self._query(node.left, start, mid),
                           self._query(node.right, mid + 1, end))

    def query_one(self, query):
        return self._query(self.root, query, query)

    def query_range(self, start, end):
        return self._query(self.root, start, end)

    def update_one(self, query, data):
        self._update(self.root, query, query, data)

    def update_range(self, start, end, data):
        self._update(self.root, start, end, data)
