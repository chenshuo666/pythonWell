#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

# 图的节点结构
class GraphMatrix:
    def __init__(self, map=[]):
        self.map = map  # 图的矩阵结构
        self.node_num = len(map)
        self.edge_num = 0

    #  self.node_num = get_node_num()#节点数
    #  self.edge_num = get_edge_num()#边数
    def isOutRange(self, x):
        try:
            if x >= self.node_num or x <= 0:
                raise IndexError
        except IndexError:
            print("节点下标出界")

    def get_node_num(self):
        self.node_num = len(self.map)
        return self.node_num

    def get_edge_num(self):
        self.get_node_num()
        self.edge_num = 0
        for i in range(self.node_num):
            for j in range(self.node_num):
                if self.map[i][j] is 1:
                    self.edge_num = self.edge_num + 1
        return self.edge_num

    def InsertNode(self,matrix_in):
        for i in range(self.node_num):
            self.map[i].append(0)
        self.node_num = self.node_num + 1
        if matrix_in[-1] == -1 and self.node_num == len(matrix_in):
            self.map.append(matrix_in)
        else:
            return

    # 假删除，只是归零而已
    def DeleteNode(self, x):
        for i in range(self.node_num):
            if self.map[i][x] is 1:
                self.map[i][x] = 0
                self.edge_num = self.edge_num - 1
            if self.map[x][i] is 1:
                self.map[x][i] = 0
                self.edge_num = self.edge_num - 1

    def AddEdge(self, x, y):
        if self.map[x][y] is 0:
            self.map[x][y] = 1
            self.edge_num = self.edge_num + 1

    def RemoveEdge(self, x, y):
        if self.map[x][y] is 0:
            self.map[x][y] = 1
            self.edge_num = self.edge_num + 1

    def bfs(self):
        def BFS(self, i):
            print(i)
            visited[i] = 1
            for k in range(self.node_num):
                if self.map[i][k] == 1 and visited[k] == 0:
                    BFS(self, k)

        visited = [0] * self.node_num
        for i in range(self.node_num):
            if visited[i] is 0:
                BFS(self, i)

    def dfs(self):
        def DFS(self, i, queue):
            queue.append(i)
            print(i)
            visited[i] = 1
            if len(queue) != 0:
                w = queue.pop()
                for k in range(self.node_num):
                    if self.map[w][k] is 1 and visited[k] is 0:
                        DFS(self, k, queue)

        visited = [0] * self.node_num
        queue = []
        for i in range(self.node_num):
            if visited[i] is 0:
                DFS(self, i, queue)

if __name__ == '__main__':
    maps = [
        [-1, 1, 0, 0],
        [0, -1, 0, 0],
        [0, 0, -1, 1],
        [1, 0, 0, -1]]
    matrix = [1, 0, 0, 0, -1]
    G = GraphMatrix(maps)
    G.InsertNode(matrix)
    G.AddEdge(1, 4)
    print("广度优先遍历")
    G.bfs()
    print("深度优先遍历")
    G.dfs()