# -*- coding: latin-1 -*-

"""
Created on Wed Apr 17 15:36:48 2013

@author:
"""

from search import Search

class GraphSearch(Search):
    def search(self, problem):
        self.explored = {}
        return super(GraphSearch, self).search(problem)

    def expand_border(self, node):
        order_mem = self.explored.get(node.state)
        order_node = self.order(node)
        if order_mem is None or order_node < order_mem:
            self.insert_border(node)
            self.explored[node.state] = order_node

    def ordem(self, node):
        return node.prof
