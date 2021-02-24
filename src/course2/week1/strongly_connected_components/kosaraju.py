from typing import Any, Dict, List, Optional

Graph = Dict[int, List[int]]
TrackedGraph = Dict[int, Dict[str, Any]]


class Kosaraju:
    def __init__(self, graph: Graph) -> None:
        self.graph = self.reverse_graph(graph)
        self.t = 0
        self.start_node: Optional[int] = None
        self.explored_nodes: List[int] = []
        self.finishing_times: List[int] = []
        self.sccs: Dict[int, int] = {}

    def reverse_graph(self, graph: Graph) -> Graph:
        reversed_graph: Graph = {node: [] for node in graph}
        for node, adjacent_nodes in graph.items():
            for adjacent_node in adjacent_nodes:
                reversed_graph[adjacent_node].append(node)
        return reversed_graph

    def first_pass(self) -> List[int]:
        self.current_label = len(self.graph)
        for vertex in self.graph:
            if vertex not in self.explored_nodes:
                self.start_node = vertex
                self.dfs(vertex)
        self.finishing_times.reverse()

    def dfs(self, start_node: int = 0) -> None:
        self.explored_nodes.append(start_node)
        for adjacent_node in self.graph[start_node]:
            if adjacent_node not in self.explored_nodes:
                self.dfs(adjacent_node)
        self.finishing_times.append(start_node)
        self.current_label -= 1

    def second_pass(self) -> None:
        self.num_scc = 0
        for node in self.finishing_times:
            if node not in self.explored_nodes:
                self.num_scc += 1
                self.dfs_scc(node)

    def dfs_scc(self, start_node: int):
        self.explored_nodes.append(start_node)
        self.sccs[start_node] = self.num_scc
        for adjacent_node in self.graph[start_node]:
            if adjacent_node not in self.explored_nodes:
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
        self.t = 0
        self.start_node = None
        self.explored_nodes = []
        self.graph = self.reverse_graph(self.graph)
        self.second_pass()
        return self.aggregate_scc()


graph = {
    1: [7],
    2: [5],
    3: [9],
    4: [1],
    5: [8],
    6: [3, 8],
    7: [4, 9],
    8: [2],
    9: [6],
}
kosaraju = Kosaraju(graph)
actual = kosaraju.run()
print(actual)
