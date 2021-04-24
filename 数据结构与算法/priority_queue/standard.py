from .base import BasePriorityQueue


class UnsortedPriorityQueue(BasePriorityQueue):
    """使用未排序列表实现的优先级队列

    时间复杂度列表：
    len O(1)
    is_empty O(1)
    add O(1)
    min O(n)
    remove_min O(n)
    """

    def __init__(self):
        """创建一个空的优先级队列实例"""

    def add(self, k, v):
        pass

    def min(self):
        pass

    def remove_min(self):
        pass

    def __len__(self):
        pass
