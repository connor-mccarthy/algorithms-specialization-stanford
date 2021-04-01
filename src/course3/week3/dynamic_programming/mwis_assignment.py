import os

from mwis import Nodes, mwis


def get_data() -> Nodes:
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "mwis_assignment_data.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    return [int(line.strip()) for line in lines][1:-1]


def main() -> str:
    data = get_data()
    indices = mwis(data)
    comparison_nodes = [1, 2, 3, 4, 17, 117, 517, 997]
    adj_comparison_nodes = [i - 1 for i in comparison_nodes]
    return "".join(str(int(node in indices)) for node in adj_comparison_nodes)


if __name__ == "__main__":
    print(main())
