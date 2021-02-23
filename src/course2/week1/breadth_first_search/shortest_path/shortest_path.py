from typing import Any, Dict, List

Graph = Dict[int, List[int]]
TrackedGraph = Dict[int, Dict[str, Any]]


def shortest_path(graph: Graph, target_node: int) -> int:
    all_nodes = list(graph.keys())
    graph_tracker: TrackedGraph = {
        node: {"nodes": graph[node], "is_explored": False, "distance": 0}
        for node in all_nodes
    }

    start_node = all_nodes[0]
    queue = [start_node]
    graph_tracker[start_node]["is_explored"] = True
    while queue:

        current_node = queue.pop(0)
        adjacent_nodes = graph_tracker[current_node]["nodes"]

        if current_node == target_node:
            return graph_tracker[current_node]["distance"]

        for adjacent_node in adjacent_nodes:
            if not graph_tracker[adjacent_node]["is_explored"]:
                graph_tracker[adjacent_node]["is_explored"] = True
                graph_tracker[adjacent_node]["distance"] = (
                    graph_tracker[current_node]["distance"] + 1
                )
                queue.append(adjacent_node)
