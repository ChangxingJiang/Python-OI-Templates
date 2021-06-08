"""并查集 (Disjoint Set Union, DSU)

用于维护、查询无向图的连通性，支持判断两个点是否在同一个连通中。
本质上使用数组结构表示的多叉树，每个节点记录它的父节点，如果父节点不存在则为它本身。

【功能说明】
1. 包含路径压缩功能（在find的过程中直接进行路径压缩）
2. 包含依据节点数量选择领导者的功能（在union中依据子节点数量选择节点数量多的作为领导者）

【时间复杂度】
构造实例：O(N)
查询元素所在集合：O(1)*
合并两个元素坐在集合：O(1)*
（其中：*为摊销）

【定长并查集(DSU1)方法说明】
DSU1(n) 构造长度为n的并查集实例
find(i) 查询i所属的连通分支
union(i,j) 合并i和j的连通分支
group_num 计算当前的连通分支数量

【变长并查集(DSU2)方法说明】
DSU2() 构造并查集实例
add(x) 向并查集中添加新的元素x
find(x) 查询i所属的连通分支
union(x,y) 合并i和j的连通分支
get_size(x) 获取元素x所在连通分支的元素数量
"""


class DSU:
    def __init__(self, n: int):
        self._n = n
        self._array = [i for i in range(n)]
        self._size = [1] * n
        self._group_num = n

    def find(self, i: int) -> int:
        """查询i所在的连通分支:O(1)"""
        if self._array[i] != i:
            self._array[i] = self.find(self._array[i])
        return self._array[i]

    def union(self, i: int, j: int) -> bool:
        """合并i和j所属的连通分支:O(1)"""
        i, j = self.find(i), self.find(j)
        if i != j:
            self._group_num -= 1
            if self._size[i] >= self._size[j]:
                self._array[j] = i
                self._size[i] += self._size[j]
            else:
                self._array[i] = j
                self._size[j] += self._size[i]
            return True
        else:
            return False

    def is_connected(self, i: int, j: int) -> bool:
        return self.find(i) == self.find(j)

    @property
    def group_num(self) -> int:
        """计算连通分支数量:O(1)"""
        return self._group_num

    @property
    def max_group_size(self) -> int:
        """计算最大连通分支包含的数量:O(N)"""
        import collections
        return max(collections.Counter(self._array).values())
