from abc import ABCMeta
from abc import abstractmethod


class BasePriorityQueue(metaclass=ABCMeta):
    """优先级队列的抽象基类"""

    class Item:
        """轻量级的键值对类"""
        __slots__ = ("_key", "_value")

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other: "BasePriorityQueue.Item"):
            return self._key < other._key

    @abstractmethod
    def add(self, k, v):
        """向优先级队列中插入一个拥有键k和值v的元组"""

    @abstractmethod
    def min(self):
        """返回一个元组(k,v)，代表优先级队列P中一个包含键和值的元组，该元组的键值是最小值

        如果队列为空，将发生错误
        """

    @abstractmethod
    def remove_min(self):
        """从优先级队列P中移除一个拥有最小键值的元组，并且返回这个被移除的元组

        如果队列为空，将发生错误
        """

    def is_empty(self):
        """如果优先级队列不包含任何元组，将返回True"""
        return len(self) == 0

    @abstractmethod
    def __len__(self):
        """返回优先级队列中元素的数量"""
