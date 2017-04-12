"""
Moving the Puzzle
"""

from itertools import product
from random import shuffle
from math import sqrt

__all__ = ['moves', 'move', 'num_out_of_place_pieces', 'manhattan_dist']
moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def puzzle_size(puz):
    """Size of a puzzle
    @return: dimx, dimy"""
    return (len(puz[0]), len(puz))


def puzzle_pos(puz):
    """Puzzle positions
    @return: list of valid positions (x,y) for a puzzle"""
    dimx, dimy = puzzle_size(puz)
    return product(range(dimx), range(dimy))


def valid_pos(puz, (x, y)):
    """Check if (x,y) is a valid position on the puzzle"""
    dimx, dimy = puzzle_size(puz)
    return x >= 0 and x < dimx and y >= 0 and y < dimy


def piece_pos(puz, piece):
    """Get piece position in the puzzle
    @return: (x,y)"""
    predicate = lambda (x, y): puz[y][x] == piece
    return filter(predicate, puzzle_pos(puz))[0]


def move(puz, (dx, dy)):
    """Move empty puzzle position with a (dx, dy) increment
    @param puz: puzzle
    @param dx: x increment
    @param dy: y increment
    @return: new puzzle"""
    x, y = piece_pos(puz, 0)
    nx, ny = x + dx, y + dy
    if valid_pos(puz, (nx, ny)):
        new_puzzle = [ list(linha) for linha in puz ]
        new_puzzle[y][x] = puz[ny][nx]
        new_puzzle[ny][nx] = 0
        return tuple([ tuple(linha) for linha in new_puzzle ])


def num_out_of_place_pieces(puz1, puz2):
    """Number of out of place pieces between puzzles
    @param puz1: puzzle 1
    @param puz2: puzzle 2
    @return: number of out of place pieces"""
    predicate = lambda (x, y): puz1[y][x] != puz2[y][x]
    return len(filter(predicate, puzzle_pos(puz1)))


def distman_pos(puz1, puz2, (x, y)):
    """Manhattan distance between a piece position on a puzzle"""
    xobj, yobj = piece_pos(puz2, puz1[y][x])
    return abs(xobj - x) + abs(yobj - y)


def manhattan_dist(puz1, puz2):
    """Manhattan distance between puzzles
    @param puz1: puzzle 1
    @param puz2: puzzle 2
    @return: Manhattan distance between puzzles"""
    method = lambda pos: distman_pos(puz1, puz2, pos)
    return sum(map(method, puzzle_pos(puz1)))


def is_perfect_square(n):
    """Check for a natural number n if it is a perfect square."""
    if n < 0 or int(n) != n:
        return False
    i = isqrt(n)
    while i**2 <= n:
        if i**2 == n:
            return True
        i += 1
    return False


def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
    
    
def make_puzzle(num_pieces=9):
    """Generate a random puzzle (may have no solution).
    
    @param num_pieces: number of pieces in the puzzle including blank, default: 9
    @return: puzzle"""
    if not is_perfect_square(num_pieces):
        num_pieces = 9
    puzzle = range(num_pieces)
    shuffle(puzzle)
    # reshape puzzle
    board_size = int(sqrt(num_pieces))
    board_puzzle = tuple( tup for tup in zip(*[iter(puzzle)]*board_size))
    return board_puzzle
    