# -*-coding:GBK -*-

"""
图
"""

from copy import deepcopy
from typing import Dict
from typing import Tuple

from .base import BaseEdge
from .base import BaseGraph
from .base import BaseVertex


class Graph(BaseGraph):
    """图"""

    class Vertex(BaseVertex):
        """轻量级的节点的类"""

        def __init__(self, x):
            self._element = x

        def element(self):
            """返回节点的值"""
            return self._element

        def __hash__(self):
            return hash(id(self))

    class Edge(BaseEdge):
        """轻量级的边的类"""

        def __init__(self, u: "Graph.Vertex", v: "Graph.Vertex", x):
            self._origin = u
            self._destination = v
            self._element = x

        def endpoint(self) -> Tuple["Graph.Vertex", "Graph.Vertex"]:
            """返回两端点的元组

            对于有向图，返回元组(u,v)，顶点u是边的起点，顶点v是终点；
            对于无向图，返回元组(u,v)，其方向是任意的。
            """
            return self._origin, self._destination

        def opposite(self, v: "Graph.Vertex") -> "Graph.Vertex":
            """返回边的另一个顶点"""
            return self._destination if v is self._origin else self._origin

        def element(self):
            """返回节点的值"""
            return self._element

        def __hash__(self):
            return hash((self._origin, self._destination))

    def __init__(self, directed=False):
        """构造一个空的图

        :param directed: 是否为有向图(True=有向图,False=无向图)
        """
        self._directed = directed
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    @property
    def is_directed(self) -> bool:
        """返回图是否为有向图"""
        return self._incoming is not self._outgoing

    def vertex_count(self) -> int:
        """返回图的顶点的数目"""
        return len(self._outgoing)

    def vertices(self):
        """迭代返回图中所有节点"""
        return self._outgoing.keys()

    def edge_count(self) -> int:
        """返回图的边的数目"""
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed else total // 2

    def edges(self):
        """迭代返回图的所有边"""
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u: "Graph.Vertex", v: "Graph.Vertex"):
        """如果存在则返回从顶点u到顶点v的边，否则返回None"""
        return self._outgoing[u].get(v)

    def degree(self, v: "Graph.Vertex", out: bool = True) -> int:
        """返回节点的度/入度/出度

        对于无向图，返回入射到顶点v的边的数目；
        对于有向图，返回入射到顶点v的输出边(out=True)或输入(out=False)的边的数目
        """
        adj = self._outgoing if out else self._incoming
        return len(adj[v])

    def incident_edges(self, v: "Graph.Vertex", out: bool = True):
        """迭代返回所有入射到顶点v的边

        对于无向图，返回入射到顶点v的边；
        对于有向图，返回入射到顶点v的输出边(out=True)或输入(out=False)边的数目
        """
        adj = self._outgoing if out else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None) -> "Graph.Vertex":
        """创建和返回一个新的存储元素x的节点(Vertex)"""
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed:
            self._incoming[v] = {}
        return v

    def insert_edge(self, u: "Graph.Vertex", v: "Graph.Vertex", x=None) -> "Graph.Edge":
        """创建和返回一个新的从节点u到节点v的存储元素x的边(Edge)"""
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
        return e

    def remove_vertex(self, v: "Graph.Vertex"):
        """移除顶点v和图中它的所有入射边"""
        del self._outgoing[v]
        if self.is_directed:
            del self._incoming[v]

    def remove_edge(self, e: "Graph.Edge"):
        """移除图中的边e"""
        u, v = e.endpoint()
        del self._outgoing[u][v]
        del self._incoming[v][u]


def DFS(g: "Graph", u: "Graph.Vertex", discovered: Dict):
    """深度优先搜索"""
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS(g, v, discovered)


def construct_path(u: "Graph.Vertex", v: "Graph.Vertex", discovered: Dict):
    """构建从u到v的有向路径"""
    path = []
    if v in discovered:
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()
    return path


def DFS_complete(g: "Graph"):
    """返回图的全部DFS森林"""
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None
            DFS(g, u, forest)
    return forest


def BFS(g: "Graph", s: "Graph.Vertex", discovered: Dict):
    """广度优先搜索"""
    level = [s]
    while len(level) > 0:
        next_level = []
        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    next_level.append(v)
        level = next_level


def floyd_warshall(g: "Graph"):
    """Floyd_Warshall算法计算传递闭包"""
    closure = deepcopy(g)
    verts = list(closure.vertices())
    n = len(verts)
    for k in range(n):
        for i in range(n):
            if i != k and closure.get_edge(verts[i], verts[k]) is not None:
                for j in range(n):
                    if i != j != k and closure.get_edge(verts[k], verts[j]) is not None:
                        if closure.get_edge(verts[i], verts[j]) is None:
                            closure.insert_edge(verts[i], verts[j])


def topological_sort(g: "Graph"):
    """有向图的拓扑排序"""
    topo = []
    ready = []
    incount = {}
    for u in g.vertices():
        incount[u] = g.degree(u, out=False)
        if incount[u] == 0:
            ready.append(u)
    while len(ready) > 0:
        u = ready.pop()
        topo.append(u)
        for e in g.incident_edges(u):
            v = e.opposite(u)
            incount[v] -= 1
            if incount[v] == 0:
                ready.append(v)
    return topo
