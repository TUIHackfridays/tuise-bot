import math
import puzzle as puz
from state_space_search.bestfirstsearch import AASearch as SearchMecanism

#_________________________________
# Defining MoveEmptyPos operator

class MoveEmptyPos:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def apply_move(self, state):
        return puz.move(state, (self.dx, self.dy))

    def cost(self, state1, state2):
        return 1

#______________________________________________
# Defining the puzzle problem of sliding pieces
class ProblemPuzzle:
    def __init__(self, puz_ini,puz_fin):
        self.puz_ini = puz_ini
        self.puz_fin = puz_fin

        # directions
        left = MoveEmptyPos(-1, 0)
        right = MoveEmptyPos(1, 0)
        up = MoveEmptyPos(0, -1)
        down = MoveEmptyPos(0, 1)

        self._operators = [left, right, up, down]


    def initial_state(self):
        return self.puz_ini

    def operators(self):
        return self._operators

    def objective(self, state):
        return state == self.puz_fin

    def heuristics(self, state):
        return puz.manhattan_dist(state, self.puz_fin)


#______________________________________________
# Validate a puzzle
def validate_puzzle(puz):
    values = []
    max_val = (len(puz[0]) * len(puz)) - 1 # number of pieces with blank removed
    for line in puz:
        for elem in  line:
            if elem in values or elem > max_val:
                return False
            else:
                values.append(elem)
                values = sorted(values)
    return True

#______________________________________________
# Show puzzle
def show_puzzle(puz):
    for line in puz:
        print(line)
    print("")
    

def generate_puzzle(size = 9, flatten=False):
    gen_puzzle = puz.make_puzzle(size)
    if flatten:
        gen_puzzle = [element for tupl in gen_puzzle for element in tupl]
    return gen_puzzle


def list_to_puzzle(flattened_puzzle):
    num_pieces = len(flattened_puzzle)
    board_size = int(math.sqrt(num_pieces))
    return tuple( tup for tup in zip(*[iter(flattened_puzzle)]*board_size))


def get_solution(puz_ini, show_solution=False, flatten=False):
    puz_fin = ((1,2,3),
                (4,5,6),
                (7,8,0))
                
    valid = validate_puzzle(puz_ini)
    if valid:
        problem = ProblemPuzzle(puz_ini, puz_fin)
        solution = SearchMecanism().search(problem)
    
        steps = 0
        final_solution = []
    
        if solution:
            steps = len(solution) - 1
            for node in solution:
                if show_solution:
                    show_puzzle(node.state)
                if flatten:
                    final_solution.append([element for tupl in node.state for element in tupl])
                else:
                    final_solution.append([list(x) for x in node.state])
            return final_solution, "Found solution with " + str(steps) + " steps."
        else:
            return None, "No solution found"
    else:
        return None, "Invalid puzzle."


if __name__ == "__main__":
    #_____________________________________________
    # Running
    
    puz_ini = ((1,2,3),
                (4,5,6),
                (7,0,8))
    
#    puz_ini = ((2,3,6),
#                (1,0,5),
#                (4,7,8))
    
#    puz_ini = ((1,2,3),
#                (8,4,5),
#                (6,7,0))
    
#    puz_ini = ((8,4,5),
#                (6,1,2),
#                (3,7,0))
    
#    puz_ini = ((1,2,3),
#               (8,4,5),
#               (6,7,0))
    
#    puz_ini = ((8,4,5),
#               (6,1,2),
#               (3,7,0)) # conf. B
    
    puz_ini = generate_puzzle()
    
    solution, message = get_solution(puz_ini, show_solution=True, flatten=True)
    if solution is not None:
        print(solution)
    print(message)