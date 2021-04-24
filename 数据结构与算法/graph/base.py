# -*-coding:GBK -*-

"""
抽象基类

BaseVertex 轻量级的边的抽象基类
BaseGraph 图的抽象基类
"""

from abc import ABCMeta
from abc import abstractmethod


class BaseVertex(metaclass=ABCMeta):
    """轻量级的节点的抽象基类"""
    __slots__ = ("_element",)

    @abstractmethod
    def element(self):
        """返回节点的值"""


class BaseEdge(metaclass=ABCMeta):
    """轻量级的边的抽象基类"""
    __slots__ = ("_origin", "_destination", "_element")

    @abstractmethod
    def endpoint(self):
        """返回两端点的元组

        对于有向图，返回元组(u,v)，顶点u是边的起点，顶点v是终点；
        对于无向图，返回元组(u,v)，其方向是任意的。
        """

    @abstractmethod
    def opposite(self, v):
        """返回边的另一个顶点"""

    @abstractmethod
    def element(self):
        """返回节点的值"""


class BaseGraph(metaclass=ABCMeta):
    """图的抽象基类"""

    @abstractmethod
    def vertex_count(self):
        """返回图的顶点的数目"""

    @abstractmethod
    def vertices(self):
        """迭代返回图中所有节点"""

    @abstractmethod
    def edge_count(self):
        """返回图的边的数目"""

    @abstractmethod
    def edges(self):
        """迭代返回图的所有边"""

    @abstractmethod
    def get_edge(self, u, v):
        """如果存在则返回从顶点u到顶点v的边，否则返回None"""

    @abstractmethod
    def degree(self, v, out=True):
        """返回节点的度/入度/出度

        对于无向图，返回入射到顶点v的边的数目；
        对于有向图，返回入射到顶点v的输出边(out=True)或输入(out=False)的边的数目
        """

    @abstractmethod
    def incident_edges(self, v, out=True):
        """迭代返回所有入射到顶点v的边

        对于无向图，返回入射到顶点v的边；
        对于有向图，返回入射到顶点v的输出边(out=True)或输入(out=False)边的数目
        """

    @abstractmethod
    def insert_vertex(self, x=None):
        """创建和返回一个新的存储元素x的节点(Vertex)"""

    @abstractmethod
    def insert_edge(self, u, v, x=None):
        """创建和返回一个新的从节点u到节点v的存储元素x的边(Edge)"""

    @abstractmethod
    def remove_vertex(self, v):
        """移除顶点v和图中它的所有入射边"""

    @abstractmethod
    def remove_edge(self, e):
        """移除图中的边e"""
