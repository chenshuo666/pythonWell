#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

# 图的节点结构
import networkx as nx
import matplotlib.pyplot as plt

class GraphMatrix:
    def __init__(self, vertice=[], matrix=[] ):
        self.matrix = matrix  # 图的矩阵结构
        self.vertice = vertice # 顶点的表示

        self.edges_dict = {}  # {(tail, head):weight}有权图
        self.edges_array = []  # (tail, head, weight)
        self.edges_array_copy = []

        self.edge_num = 0
        self.vertice_num = len(vertice)

        if len(matrix) > 0:
            if len(vertice) != len(matrix):
                raise IndexError
            self.edges = self.get_all_edges()

        # if do not provide a adjacency matrix, but provide the vertice list, build a matrix with 0
        elif len(vertice) > 0:
            self.matrix = [[0 for col in range(len(vertice))] for row in range(len(vertice))]

    def isOutRange(self, x):
        try:
            if x >= self.vertice_num or x <= 0:
                raise IndexError
        except IndexError:
            print("OUT RANGE")

    '''顶点的操作'''
    def get_all_vertice(self):#获取所有的顶点
        return self.vertice

    def get_vertice_num(self):#获取顶点的数目
        self.vertice_num = len(self.matrix)
        return self.vertice_num

    def add_vertice(self,vertice,matrix_in):#增加一个顶点
        if vertice not in self.vertice:
            self.vertice.append(vertice)
        for i in range(self.vertice_num):
            self.matrix[i].append(0)
        self.vertice_num = self.vertice_num + 1
        if matrix_in[-1] == 0 and self.vertice_num == len(matrix_in):
            self.matrix.append(matrix_in)
        else:
            return

    def delete_vertice(self, x):#删除一个顶点
        index_t = 0
        if x in self.vertice:
            for i in range(len(self.vertice)):
                if x==self.vertice[i]:
                    index_t=i
            for i in range(self.vertice_num):
                if self.matrix[i][index_t] is 1:
                    self.matrix[i][index_t] = 0
                    self.edge_num = self.edge_num - 1
                if self.matrix[index_t][i] is 1:
                    self.matrix[index_t][i] = 0
                    self.edge_num = self.edge_num - 1
            self.vertice.remove(x)
            list(map(lambda delete: delete[index_t:], self.matrix))
            self.matrix.remove(self.matrix[index_t])


    '''边的操作'''
    def get_all_edges(self):#获取所有的边
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if  self.matrix[i][j] != 0:
                    self.edges_dict[self.vertice[i], self.vertice[j]] = self.matrix[i][j]
                    self.edges_array.append([self.vertice[i], self.vertice[j], self.matrix[i][j]])

        return self.edges_array

    def get_edge_num(self):#获取边的数目
        self.edge_num = 0
        for i in range(self.vertice_num):
            for j in range(self.vertice_num):
                if self.matrix[i][j] is 1:
                    self.edge_num = self.edge_num + 1
        return self.edge_num

    def add_edge(self, vertice1, vertice2):#增加一条边
        index1 = 0
        index2 = 0
        if vertice1 in self.vertice and vertice2 in self.vertice:
            for i in range(len(self.vertice)):
                if vertice1 == self.vertice[i]:
                    index1 = i
            for t in range(len(self.vertice)):
                if vertice2 == self.vertice[t]:
                    index2 = t

            if self.matrix[index1][index2] is 0:
                self.matrix[index1][index2] = 1
                self.edge_num = self.edge_num + 1

    def remove_edge(self, vertice1, vertice2):#删除边
        index1 = 0
        index2 = 0
        if vertice1 in self.vertice and vertice2 in self.vertice:
            for i in range(len(self.vertice)):
                if vertice1 == self.vertice[i]:
                    index1 = i
            for t in range(len(self.vertice)):
                if vertice2 == self.vertice[t]:
                    index2 = t
            if self.matrix[index1][index2] is 1:
                self.matrix[index1][index2] = 0
                self.edge_num = self.edge_num - 1
            else:
                return
        else:
            return

    '''图的遍历'''

    def dfs(self,x):
        index_t = 0
        if x in self.vertice:
            for i in range(len(self.vertice)):
                if x == self.vertice[i]:
                    index_t = i
        res = []
        visited = [False]*self.vertice_num
        def DFS(i):
            res.append(self.vertice[i])
            visited[i] = True
            for j in range(self.vertice_num):
                if self.matrix[i][j] > 0 and visited[j] == False:
                    DFS(j)
        if self.vertice_num > 0:
            DFS(index_t)
        for i in range(self.vertice_num):
            if visited[i] == False:
                DFS(i)
        return res

    def bfs(self,x):
        index_t = 0
        if x in self.vertice:
            for i in range(len(self.vertice)):
                if x == self.vertice[i]:
                    index_t = i
        queue = []
        visited = [False] * self.vertice_num
        res = []

        def BFS():
            while len(queue) > 0:
                i = queue.pop(0)
                for j in range(self.vertice_num):
                    if self.matrix[i][j] > 0 and visited[j] == False:
                        res.append(self.vertice[j])
                        visited[j] = True
                        queue.append(j)

        if self.vertice_num <= 0:
            return res
        else:
            queue.append(index_t)  # index, value
            visited[0] = True
            res.append(self.vertice[index_t])
            BFS()

        for i in range(self.vertice_num):
            if visited[i] == False:
                res.append(self.vertice[i])
                visited[i] = True
                queue.append(i)
                BFS()
        return res

    # def dfs(self):#深度优先遍历
    #     def DFS(self, i, queue):
    #         queue.append(i)
    #         print(i)
    #         visited[i] = 1
    #         if len(queue) != 0:
    #             w = queue.pop()
    #             for k in range(self.vertice_num):
    #                 if self.matrix[w][k] is 1 and visited[k] is 0:
    #                     DFS(self, k, queue)
    #
    #     visited = [0] * self.vertice_num
    #     queue = []
    #     for i in range(self.vertice_num):
    #         if visited[i] is 0:
    #             DFS(self, i, queue)

    def create_undirected_matrix(self):
        graph_by_anthor = GraphMatrix(self.vertice, self.matrix)
        print(graph_by_anthor)
        return graph_by_anthor

    def draw_undirected_graph(self,graph_by_anthor): #无向无权图可视化
        G = nx.Graph()  # 建立一个空的无向图G
        for node in graph_by_anthor.vertice:
            G.add_node(str(node))
        for edge in graph_by_anthor.edges_array:
            G.add_edge(str(edge[0]), str(edge[1]))

        print("nodes:", G.nodes())  # 输出全部的节点： [1, 2, 3]
        print("edges:", G.edges())  # 输出全部的边：[(2, 3)]
        print("number of edges:", G.number_of_edges())  # 输出边的数量：1
        nx.draw(G, with_labels=True)
        plt.savefig('fig.png', bbox_inches='tight')
        plt.show()

    def draw_directed_graph(self,graph_by_anthor):
        G = nx.DiGraph()  # 建立一个空的有向图G
        for node in graph_by_anthor.vertice:
            G.add_node(str(node))
        G.add_weighted_edges_from(graph_by_anthor.edges_array)

        print("nodes:", G.nodes())  # 输出全部的节点
        print("edges:", G.edges())  # 输出全部的边
        print("number of edges:", G.number_of_edges())  # 输出边的数量
        nx.draw(G, with_labels=True)
        plt.savefig("directed_graph.png", bbox_inches='tight')
        plt.show()

if __name__ == "__main__":

    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    matrix = [[0, 1, 1, 0, 0, 1, 0, 0],  # a
              [0, 0, 1, 0, 1, 0, 0, 0],  # b
              [0, 0, 0, 1, 0, 0, 0, 0],  # c
              [0, 0, 0, 0, 1, 0, 0, 0],  # d
              [0, 0, 0, 0, 0, 1, 0, 0],  # e
              [0, 0, 1, 0, 0, 0, 1, 1],  # f
              [0, 0, 0, 0, 0, 0, 0, 1],  # g
              [0, 0, 0, 0, 0, 1, 1, 0]]  # h
    matrix_in = [0 ,0,0,0,0,0,0,1,0]
    m=GraphMatrix(nodes,matrix)
    m.add_vertice("i",matrix_in)
    # m.add_edge(6,4)
    print(m.get_all_edges())
    print(m.get_all_vertice())
    print("__________________")
    print(m.get_edge_num())
    print(m.get_vertice_num())
    print(m.dfs("c"))
    print(m.bfs("a"))
    # m.delete_vertice("i")

    p=m.create_undirected_matrix()
    m.draw_undirected_graph(p)

