from typing import Dict, List, Optional

Graph = List[List[int]]


class Kosaraju:
    def __init__(self, adj_list: List[List[int]]) -> None:
        self.num_nodes = max(node for row in adj_list for node in row)
        self.get_graphs(adj_list)
        self.t = len(self.rev_graph)
        self.start_node: Optional[int] = None
        self.visited = [False] * (self.num_nodes + 1)
        self.finishing_times: List[int] = []
        self.sccs: Dict[int, int] = {}

    def get_graphs(self, adj_list: List[List[int]]) -> None:
        graph: Graph = [[] for _ in range(self.num_nodes + 1)]
        rev_graph: Graph = [[] for _ in range(self.num_nodes + 1)]
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
