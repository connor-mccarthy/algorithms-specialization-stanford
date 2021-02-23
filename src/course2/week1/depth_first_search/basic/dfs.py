from typing import Any, Dict, List

Graph = Dict[int, List[int]]
TrackedGraph = Dict[int, Dict[str, Any]]


def dfs(graph: Graph) -> TrackedGraph:
    all_nodes = list(graph.keys())
    graph_tracker: TrackedGraph = {
        node: {"nodes": graph[node], "is_explored": False} for node in all_nodes
    }

    start_node = all_nodes[0]
    queue = [start_node]
    graph_tracker[start_node]["is_explored"] = True
    while queue:

        current_node = queue.pop()
        adjacent_nodes = graph_tracker[current_node]["nodes"]

        for adjacent_node in adjacent_nodes:
            if not graph_tracker[adjacent_node]["is_explored"]:
                graph_tracker[adjacent_node]["is_explored"] = True
                queue.append(adjacent_node)

    return graph_tracker
