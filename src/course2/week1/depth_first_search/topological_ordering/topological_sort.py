from typing import Any, Dict, List

Graph = Dict[int, List[int]]
TrackedGraph = Dict[int, Dict[str, Any]]


class TopologicalSort:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.graph_tracker: TrackedGraph = {
            node: {"nodes": graph[node], "is_explored": False, "topo_id": None}
            for node in graph
        }
        self.current_label = len(self.graph)

    def sort(self) -> None:
        for vertex in self.graph_tracker:
            if not self.graph_tracker[vertex]["is_explored"]:
                self.dfs(vertex)

    def dfs(self, start_node: int = 0) -> None:
        self.graph_tracker[start_node]["is_explored"] = True
        for adjacent_node in self.graph_tracker[start_node]["nodes"]:
            if not self.graph_tracker[adjacent_node]["is_explored"]:
                self.dfs(adjacent_node)
        self.graph_tracker[start_node]["topo_id"] = self.current_label
        self.current_label -= 1
