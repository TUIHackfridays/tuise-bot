# -*- coding: latin-1 -*-

from node import Node

#____________________________________________________________________________

class Search(object):
    def search(self, problem):
        self.total_nodes = 0
        self.max_nodes = 0
        self.problem = problem
        self.border = []
        initial_node = Node(self.problem.initial_state())
        self.insert_border(initial_node)
        while self.border:
            node = self.remove_border()
            if self.problem.objective(node.state):
                return node.route()
            else:
                self.expand(node)

    def expand(self, node):
        for operator in self.problem.operators():
            prev_state = operator.apply_move(node.state)
            if prev_state:
                self.total_nodes += 1
                if(len(self.border) > self.max_nodes):
                    self.max_nodes = len(self.border)
                prev_node = Node(prev_state, operator, node)
                self.expand_border(prev_node)

    def remove_border(self):
        return self.border.pop(0)

    def expand_border(self, node):
        self.inserir_fronteira(node)

    def insert_border(self, node):
        raise NotImplementedError
