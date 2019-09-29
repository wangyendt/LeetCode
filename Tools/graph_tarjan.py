# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/24 20:43
# software: PyCharm


from collections import defaultdict
from itertools import chain


class Graph(object):
    def __init__(self, edges, vertices=()):
        edges = list(list(x) for x in edges)
        self.edges = edges
        self.vertices = set(chain(*edges)).union(vertices)
        self.tails = defaultdict(list)
        for head, tail in self.edges:
            self.tails[head].append(tail)

    @classmethod
    def from_dict(cls, edge_dict):
        return cls((k, v) for k, vs in edge_dict.items() for v in vs)


class _StrongCC(object):
    def strong_connect(self, head):
        lowlink, count, stack = self.lowlink, self.count, self.stack
        lowlink[head] = count[head] = self.counter = self.counter + 1
        stack.append(head)

        for tail in self.graph.tails[head]:
            if tail not in count:
                self.strong_connect(tail)
                lowlink[head] = min(lowlink[head], lowlink[tail])
            elif count[tail] < count[head]:
                if tail in self.stack:
                    lowlink[head] = min(lowlink[head], count[tail])

        if lowlink[head] == count[head]:
            component = []
            while stack and count[stack[-1]] >= count[head]:
                component.append(stack.pop())
            self.connected_components.append(component)

    def __call__(self, graph):
        self.graph = graph
        self.counter = 0
        self.count = dict()
        self.lowlink = dict()
        self.stack = []
        self.connected_components = []

        for v in self.graph.vertices:
            if v not in self.count:
                self.strong_connect(v)

        return self.connected_components


strongly_connected_components = _StrongCC()

if __name__ == '__main__':
    # https://stackoverflow.com/questions/6575058/tarjans-strongly-connected-components-algorithm-in-python-not-working
    edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'),
             ('E', 'A'), ('A', 'E'), ('C', 'A'), ('C', 'E'),
             ('D', 'F'), ('F', 'B'), ('E', 'F')]
    print(strongly_connected_components(Graph(edges)))
    edge_dict = {'a': ['b', 'c', 'd'],
                 'b': ['c', 'a'],
                 'c': ['d', 'e'],
                 'd': ['e'],
                 'e': ['c']}
    print(strongly_connected_components(Graph.from_dict(edge_dict)))
