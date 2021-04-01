from typing import List, Set

Nodes = List[int]
Indices = Set[int]


def nodes_to_array(nodes: Nodes) -> List[int]:
    nodes.insert(0, 0)
    return nodes


def mwis(nodes: Nodes) -> Indices:
    num_nodes = len(nodes)
    weights = nodes_to_array(nodes)

    for j in range(2, num_nodes + 1):
        weights[j] = max(weights[j - 1], weights[j - 2] + nodes[j])

    indep_set = set()

    i = num_nodes
    while i >= 2:
        if weights[i - 1] >= weights[i - 2] + nodes[i]:
            i -= 1
        else:
            indep_set.add(i)
            i -= 2

    # all the indices are off by one because of the bookkeeping done by the weights array; they're also reversed
    return set(sorted({i - 1 for i in indep_set}))
