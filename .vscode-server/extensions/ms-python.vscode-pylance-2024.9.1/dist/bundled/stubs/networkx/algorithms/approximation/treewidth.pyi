import itertools
import sys
from heapq import heapify, heappop, heappush

from ...classes.graph import Graph
from ...utils import not_implemented_for

__all__ = ["treewidth_min_degree", "treewidth_min_fill_in"]

def treewidth_min_degree(G: Graph): ...
def treewidth_min_fill_in(G: Graph): ...

class MinDegreeHeuristic:
    def __init__(self, graph): ...
    def best_node(self, graph): ...

def min_fill_in_heuristic(graph): ...
def treewidth_decomp(G: Graph, heuristic=...): ...
