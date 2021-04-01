import os
import sys

from huffman import Frequencies, huffman

sys.setrecursionlimit(1500)


def get_data() -> Frequencies:
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "huffman_assignment_data.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    return [int(line) for line in lines][1:]


def main() -> None:
    frequencies = get_data()
    encodings = huffman(frequencies)
    shortest_encoding = min(encodings.items(), key=lambda mapping: len(mapping[1]))[1]
    longest_encoding = max(encodings.items(), key=lambda mapping: len(mapping[1]))[1]
    print("Min length encoding:", len(shortest_encoding))
    print("Max length encoding:", len(longest_encoding))


if __name__ == "__main__":
    main()
