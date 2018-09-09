#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams


"""
图
"""

from random import randint
import time
import copy
import queue


class DenseGraph(object):
    """稠密图 - 邻接矩阵"""
    def __init__(self, n, directed):
        self.n = n  # 图中的点数
        self.m = 0  # 图中的边数
        self.directed = directed  # bool值，表示是否为有向图
        self.g = [[False for _ in range(n)] for _ in range(n)]  # 矩阵初始化都为False的二维矩阵

    def V(self):
        # 返回图中点数
        return self.n

    def E(self):
        # 返回图中边数
        return self.m

    def addEdge(self, v, w):
        # v和w中增加一条边，v和w都是[0,n-1]区间
        if v >= 0 and v < n and w >= 0 and w < n:
            if self.hasEdge(v, w):
                return None
            self.g[v][w] = True
            if not self.directed:
                self.g[w][v] = True
            self.m += 1

    def hasEdge(self, v, w):
        # v和w之间是否有边，v和w都是[0,n-1]区间
        if v >= 0 and v < n and w >= 0 and w < n:
            return self.g[v][w]

    class adjIterator(object):
        """相邻节点迭代器"""
        def __init__(self, graph, v):
            self.G = graph  # 需要遍历的图
            self.v = v  # 遍历v节点相邻的边
            self.index = 0  # 遍历的索引

        def __iter__(self):
            return self

        def next(self):
            while self.index < self.G.V():
                # 当索引小于节点数量时遍历，否则为遍历完成，停止迭代
                if self.G.g[self.v][self.index]:
                    r = self.index
                    self.index += 1
                    return r
                self.index += 1
            raise StopIteration()


class SparseGraph(object):
    """稀疏图- 邻接表"""
    def __init__(self, n, directed):
        self.n = n  # 图中的点数
        self.m = 0  # 图中的边数
        self.directed = directed  # bool值，表示是否为有向图
        self.g = [[] for _ in range(n)]  # 矩阵初始化都为空的二维矩阵

    def V(self):
        # 返回图中点数
        return self.n

    def E(self):
        # 返回图中边数
        return self.m

    def addEdge(self, v, w):
        # v和w中增加一条边，v和w都是[0,n-1]区间
        if v >= 0 and v < n and w >= 0 and w < n:
            # 考虑到平行边会让时间复杂度变为最差为O(n)
            # if self.hasEdge(v, w):
            #   return None
            self.g[v].append(w)
            if v != w and not self.directed:
                self.g[w].append(v)
            self.m += 1

    def hasEdge(self, v, w):
        # v和w之间是否有边，v和w都是[0,n-1]区间
        # 时间复杂度最差为O(n)
        if v >= 0 and v < n and w >= 0 and w < n:
            # for i in self.g[v]:
            #   if i == w:
            #       return True
            # return False
            if w in self.g[v]:
                return True
            else:
                return False

    class adjIterator(object):
        """相邻节点迭代器"""
        def __init__(self, graph, v):
            self.G = graph  # 需要遍历的图
            self.v = v  # 遍历v节点相邻的边
            self.index = 0  # 遍历的索引

        def __iter__(self):
            return self

        def next(self):
            if len(self.G.g[self.v]):
                # v有相邻节点才遍历
                if self.index < len(self.G.g[self.v]):
                    r = self.G.g[self.v][self.index]
                    self.index += 1
                    return r
                else:
                    raise StopIteration()
            else:
                raise StopIteration()


class ReadGraph(object):
    """读取文件中的图"""
    def __init__(self, graph, filename):
        with open(filename, 'r') as f:
            line = f.readline()
            v, e = self.stringstream(line)
            if v == graph.V():
                lines = f.readlines()
                for i in lines:
                    a,b = self.stringstream(i)
                    if a >= 0 and a < v and b >=0 and b < v:
                        graph.addEdge(a, b)

    def stringstream(self, text):
        result = text.strip('\n')
        result = result.split()
        a, b = result
        return int(a), int(b)


class Component(object):
    """深度优先遍历和联通分量"""
    def __init__(self, graph):
        self.G = graph  # 图
        self.ccount = 0  # 联通分量
        self.visited = [False for _ in range(self.G.V())]  # 记录每个节点是否被遍历
        self.id = [-1 for _ in range(self.G.V())]  # 相连节点的id相同，初始都为-1
        i = 0
        while i < self.G.V():
            if not self.visited[i]:
                self.dfs(i)
                self.ccount += 1
            i += 1

    def dfs(self, v):
        # 深度优先遍历
        self.visited[v] = True
        self.id[v] = self.ccount
        adj = self.G.adjIterator(self.G, v)  # 找到v节点所有相邻的点，进行迭代遍历
        for i in adj:
            # 如果遍历到还未遍历的节点，继续向下进行递归的深度遍历
            if not self.visited[i]:
                self.dfs(i)

    def count(self):
        # 返回联通分量
        return self.ccount

    def isConnected(self, v, w):
        # 判断节点是否相连
        if v >=0 and v < self.G.V() and w >= 0 and w < self.G.V():
            return self.id[v] == self.id[w]


class Path(object):
    """寻找路径"""
    def __init__(self, graph, s):
        self.G = graph  # 图
        self.s = s  # 从s节点开始寻找到其他节点的路径
        self.visited = [False for _ in range(self.G.V())]  # 记录每个节点是否被遍历
        self.fromed = [-1 for _ in range(self.G.V())] # 记录此节点来自哪个节点的连接

        # 寻找路径
        self.dfs(s)

    def dfs(self, v):
        # 深度优先遍历
        self.visited[v] = True
        adj = self.G.adjIterator(self.G, v)  # 找到v节点所有相邻的点，进行迭代遍历
        for i in adj:
            # 如果遍历到还未遍历的节点，继续向下进行递归的深度遍历
            if not self.visited[i]:
                self.fromed[i] = v  # 对还未遍历的节点，先将此节点的from修改为v，表示i节点来自v节点相连
                self.dfs(i)

    def hasPath(self, w):
        # w与v是否有路径
        if w >= 0 and w < self.G.V():
            return self.visited[w]

    def path(self, w):
        # 从v到w的路径
        s = []
        p = w
        while p != -1:
            s.append(p)
            p = self.fromed[p]
        s.reverse()
        return s

    def showPath(self, w):
        # 展示路径
        s = self.path(w)
        for i in s:
            print(i)


class ShortestPath(object):
    """广度优先遍历和最短路径"""
    def __init__(self, graph, s):
        self.G = graph  # 图
        self.s = s  # 从s节点开始寻找到其他节点的路径
        self.visited = [False for _ in range(self.G.V())]  # 记录每个节点是否被插入队列
        self.fromed = [-1 for _ in range(self.G.V())] # 记录此节点来自哪个节点的连接
        self.ord = [-1 for _ in range(self.G.V())]  # 记录s节点到每一个节点的距离
        # 无向图最短路径算法
        q = queue.Queue()
        q.put(s)
        self.visited[s] = True
        self.ord[s] = 0
        while not q.empty():
            v = q.get()
            adj = self.G.adjIterator(self.G, v)  # 找到v节点所有相邻的点，进行迭代遍历
            for i in adj:
                # 如果遍历到还未加入过队列的节点，将其加入队列
                if not self.visited[i]:
                    q.put(i)
                    self.visited[i] = True
                    self.fromed[i] = v
                    self.ord[i] = self.ord[v] + 1

    def hasPath(self, w):
        # w与v是否有路径
        if w >= 0 and w < self.G.V():
            return self.visited[w]

    def path(self, w):
        # 从v到w的路径
        s = []
        p = w
        while p != -1:
            s.append(p)
            p = self.fromed[p]
        s.reverse()
        return s

    def showPath(self, w):
        # 展示路径
        s = self.path(w)
        for i in s:
            print(i)

    def length(self, w):
        # s到w的距离
        if w >= 0 and w < self.G.V():
            return self.ord[w]

if __name__=="__main__":
    n = 13
    g1 = DenseGraph(n, False)
    for _ in range(100):
      a = randint(0,n-1)
      b = randint(0,n-1)
      g1.addEdge(a, b)
    v = 0
    adj = DenseGraph.adjIterator(g1, v)
    for w in adj:
      print(w)
    #filename = 'graph.txt'
    #readgraph1 = ReadGraph(g1, filename)
    # component1 = Component(g1)
    # print component1.count()
