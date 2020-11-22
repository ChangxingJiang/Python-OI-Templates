# -*-coding:UTF-8 -*-

"""并查集 (Disjoint Set Union, DSU)

用于维护、查询无向图的连通性，支持判断两个点是否在同一个连通中。
本质上使用数组结构表示的多叉树，每个节点记录它的父节点，如果父节点不存在则为它本身。

【时间复杂度】
构造实例：O(N)
查询元素所在集合：O(1)*
合并两个元素坐在集合：O(1)*
整理并查集，使所有元素均指向其最高领导者：O(N)
（其中：*为摊销）

【功能说明】
1. 包含路径压缩功能（在find的过程中直接进行路径压缩）
2. 包含依据节点数量选择领导者的功能（在union中依据子节点数量选择节点数量多的作为领导者）

【方法说明】
DSU(n) 构造并查集实例：n=并查集中元素的数量
find(i) 查询元素i所在集合的代表（这个操作也可以用来判断两个元素是否位于同一个集合中）
union(i,j) 合并元素i和元素j所在的集合，要求元素i和元素j所在集合不相交，如果相交则不合并
arrange() 整理并查集，使所有元素均指向其最高领导者
"""


class DSU:
    def __init__(self, n: int):
        self.array = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i: int):
        if self.array[i] != i:
            self.array[i] = self.find(self.array[i])
        return self.array[i]

    def union(self, i: int, j: int):
        i = self.find(i)
        j = self.find(j)
        if self.size[i] >= self.size[j]:
            self.array[j] = i
            self.size[i] += self.size[j]
        else:
            self.array[i] = j
            self.size[j] += self.size[i]

    def arrange(self):
        for i in range(len(self.array)):
            self.find(i)
