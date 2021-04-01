import os

from mwis import Nodes, mwis


def get_data() -> Nodes:
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "mwis_assignment_data.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    return [int(line) for line in lines][1:]


def main():
    data = get_data()
    indep_set = mwis(data)
    comparison_nodes = [1, 2, 3, 4, 17, 117, 517, 997]
    return "".join(int(node in indep_set) for node in comparison_nodes)
