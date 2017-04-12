# -*- coding: latin-1 -*-

import heapq as hq
from graphsearch import GraphSearch


class BestFirstSearch(GraphSearch):
    def insert_border(self, node):
        hq.heappush(self.border, (self.f(node), node))
    
    def remove_border(self):
        (_, node) = hq.heappop(self.border)
        return node
    
    def f(self, node):
        raise NotImplementedError
        
    def order(self, node):
        return self.f(node)
    
class AASearch(BestFirstSearch):
    def f(self, node):
        return node.cost + self.problem.heuristics(node.state)