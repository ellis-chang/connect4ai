from __future__ import absolute_import, division, print_function
import copy, random
from tkinter import E
from game import Game

COL_COUNT = 7
MAX_PLAYER, MIN_PLAYER = 0, 1

# tree node to construct the game tree
class Node:
    def __init__(self, state, player_type):
        self.state = (copy.deepcopy(state[0], state[1]))
        self.children = []
        self.player_type = player_type

    def is_terminal(self):
        if not self.children:
            return True
        else:
            return False

# the AI agent to determine and place next move
class AI:
    def __init__(self, root_state, search_depth=3):
        self.root = Node(root_state, MAX_PLAYER)
        self.search_depth = search_depth
        self.simulator = Game(*root_state)

    def build_tree(self, node=None, depth=0):
        if node is None or node.is_terminal():
            node = self.root
        pass

    def get_children(self, node):
        if node.children is not None:
            return node.children

    def minimax_alpha_beta(self, node):
        infinity = float('inf')
        best_val = infinity
        beta = infinity
        children = self.get_children(node)
        best_state = None
        for state in children:
            val = self.min_alpha_beta(state, best_val, beta)
            if val > best_val:
                best_val = val
                best_state = state
        return best_state

    def max_alpha_beta(self, alpha, beta):
        pass

    def min_alpha_beta(self, alpha, beta):
        pass
        