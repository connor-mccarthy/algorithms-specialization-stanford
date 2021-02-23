from typing import Any, Dict, List

Graph = Dict[int, List[int]]
TrackedGraph = Dict[int, Dict[str, Any]]


def recursive_dfs(graph_tracker: TrackedGraph, start_node: int = 0) -> TrackedGraph:
    graph_tracker[start_node]["is_explored"] = True
    for adjacent_node in graph_tracker[start_node]["nodes"]:
        if not graph_tracker[adjacent_node]["is_explored"]:
            recursive_dfs(graph_tracker, adjacent_node)
    return graph_tracker
