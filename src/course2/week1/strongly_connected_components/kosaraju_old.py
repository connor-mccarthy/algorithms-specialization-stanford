from typing import Any, Dict, List

Graph = Dict[int, List[int]]
TrackedGraph = Dict[int, Dict[str, Any]]
SCCDict = Dict[int, List[int]]


class Kosaraju:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.grev = self.make_tracker(self.reverse_graph)
        self.g = self.make_tracker(self.graph)

    @property
    def reverse_graph(self) -> Graph:
        reversed_graph: Graph = {node: [] for node in self.graph}
        for node, adjacent_nodes in self.graph.items():
            for adjacent_node in adjacent_nodes:
                reversed_graph[adjacent_node].append(node)
        return reversed_graph

    def make_tracker(self, graph: Graph) -> TrackedGraph:
        return {
            node: {
                "nodes": graph[node],
                "is_explored": False,
                "finish_time": None,
                "leader": None,
                "scc": None,
            }
            for node in graph
        }

    def first_pass(self) -> List[int]:
        self.t = len(self.grev)
        self.start_node = None
        for vertex in reversed(range(len(self.grev))):
            if not self.grev[vertex]["is_explored"]:
                self.start_node = vertex
                self.dfs(vertex)
        sorted_tuples = sorted(self.grev.items(), key=lambda x: x[1]["finish_time"])
        self.grev = {node: info for node, info in sorted_tuples}

    def dfs(self, start_node: int = 0) -> None:
        self.grev[start_node]["is_explored"] = True
        self.grev[start_node]["leader"] = self.start_node
        for adjacent_node in self.grev[start_node]["nodes"]:
            if not self.grev[adjacent_node]["is_explored"]:
                self.dfs(adjacent_node)
        self.grev[start_node]["finish_time"] = self.t
        self.t -= 1

    def second_pass(self) -> SCCDict:
        self.num_scc = 0
        for node in self.grev:
            if not self.g[node]["is_explored"]:
                self.num_scc += 1
                self.dfs_scc(node)
        return self.aggregate_scc(self.g)

    def dfs_scc(self, start_node: int):
        self.g[start_node]["is_explored"] = True
        self.g[start_node]["scc"] = self.num_scc
        for adjacent_node in self.g[start_node]["nodes"]:
            if not self.g[adjacent_node]["is_explored"]:
                self.dfs_scc(adjacent_node)

    def aggregate_scc(self, graph_tracker: TrackedGraph) -> SCCDict:
        scc_dict: SCCDict = {}
        for k, v in self.g.items():
            scc = v["scc"]
            if scc in scc_dict:
                scc_dict[scc].append(k)
            else:
                scc_dict[scc] = [k]
        return scc_dict

    def run(self) -> Dict[int, List[int]]:
        self.first_pass()
        return self.second_pass()
