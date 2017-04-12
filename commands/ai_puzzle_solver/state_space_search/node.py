class Node:
    def __init__(self, state, operator = None, predecessor = None):
        self.state = state
        self.operator = operator
        self.predecessor = predecessor
        if predecessor is None:
            self.prof=0
            self.cost=0
        else:
            self.prof = predecessor.prof + 1
            self.cost = predecessor.cost + operator.cost(state, 
                                                          predecessor.state)
        
    def route(self):
        route = []
        node_route = self
        while node_route:
            route.insert(0,node_route)
            node_route = node_route.predecessor
        return route
        