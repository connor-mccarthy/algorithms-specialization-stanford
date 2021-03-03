import os

from dijkstra import WeightedGraph, dijkstra


def get_data() -> WeightedGraph:
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "dijkstra_assignment_data.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    string_lines = [line.strip().split() for line in lines]
    graph = []
    for line in string_lines:
        start_node = line[0]
        for edge_string in line[1:]:
            end_node, weight = edge_string.split(",")
            graph.append((int(weight), int(start_node), int(end_node)))
    return graph


if __name__ == "__main__":
    graph = get_data()
    desired_vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    paths = dijkstra(graph, 1)
    distances = [paths[vertice] for vertice in desired_vertices]
    final_answer = ",".join(str(d) for d in distances)
    print(final_answer)
