import os
from typing import Dict, List, Optional

import numpy as np

from clustering import clustering
from graph_data_structures import Edge, Graph

Bits = List[int]


def get_data(filename: str) -> List[List[int]]:
    directory = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    lines = [tuple(line.strip().split()) for line in lines][1:]  # type: ignore
    return [[int(item) for item in line] for line in lines]


def get_small_data() -> Graph:
    lines = get_data("clustering.txt")
    return Graph(*[Edge(*edge_data) for edge_data in lines])


def get_big_data() -> List[List[int]]:
    MAX_DISTANCE = 3
    data = get_data("clustering_big.txt")
    data = list({tuple(sub) for sub in data})
    data = [list(sub) for sub in data]

    data = np.array(data, dtype=np.uint32)
    distance_matrix = get_hamming_distance(data)
    del data
    edges = np.argwhere((distance_matrix > 0) & (distance_matrix < MAX_DISTANCE))
    del distance_matrix
    edges = list({tuple(sorted(sub)) for sub in edges})
    return [list(edge) for edge in edges]


def get_hamming_distance(array: np.ndarray) -> np.ndarray:
    return (array[:, None, :] != array).sum(2)
    # return 2 * np.inner(array - 0.5, 0.5 - array).astype(np.uint32) + array.shape[1] / 2


# this is code from a previous section src/course2/week1/strongly_connected_components/kosaraju.py
class Kosaraju:
    Graph = List[List[int]]

    def __init__(self, adj_list: List[List[int]]) -> None:
        self.num_nodes = max(node for row in adj_list for node in row)
        self.get_graphs(adj_list)
        self.t = len(self.rev_graph)
        self.start_node: Optional[int] = None
        self.visited = [False] * (self.num_nodes + 1)
        self.finishing_times: List[int] = []
        self.sccs: Dict[int, int] = {}

    def get_graphs(self, adj_list: List[List[int]]) -> None:
        graph: Kosaraju.Graph = [[] for _ in range(self.num_nodes + 1)]
        rev_graph: Kosaraju.Graph = [[] for _ in range(self.num_nodes + 1)]
        for line in adj_list:
            graph[line[0]] += [line[1]]
            rev_graph[line[1]] += [line[0]]
        self.graph = graph
        self.rev_graph = rev_graph

    def first_pass(self) -> List[int]:
        for vertex in range(self.num_nodes):
            if not self.visited[vertex]:
                self.start_node = vertex
                self.dfs(vertex)
        self.finishing_times.reverse()

    def dfs(self, start_node: int = 0) -> None:
        self.visited[start_node] = True
        for adjacent_node in self.rev_graph[start_node]:
            if not self.visited[adjacent_node]:
                self.dfs(adjacent_node)
        self.finishing_times.append(start_node)
        self.t -= 1

    def second_pass(self) -> None:
        self.num_scc = 0
        for node in self.finishing_times:
            if not self.visited[node]:
                self.num_scc += 1
                self.dfs_scc(node)

    def dfs_scc(self, start_node: int):
        self.visited[start_node] = True
        self.sccs[start_node] = self.num_scc
        for adjacent_node in self.graph[start_node]:
            if not self.visited[adjacent_node]:
                self.dfs_scc(adjacent_node)

    def aggregate_scc(self) -> Dict[int, List[int]]:
        grouped_sccs: Dict[int, List[int]] = {}
        for node, group in self.sccs.items():
            if group in grouped_sccs:
                grouped_sccs[group].append(node)
            else:
                grouped_sccs[group] = [node]
        return grouped_sccs

    def run(self) -> Dict[int, List[int]]:
        self.first_pass()
        self.start_node = None
        self.visited = [False] * (self.num_nodes + 1)
        self.second_pass()
        return self.aggregate_scc()


def main() -> None:
    small_data_answer = clustering(get_small_data(), k=4)
    print("Question 1 answer:", small_data_answer)

    big_graph = get_big_data()
    kosaraju = Kosaraju(big_graph)
    components = kosaraju.run()
    largest_k = len(components)
    print("Question 2 answer:", largest_k)


if __name__ == "__main__":
    main()
