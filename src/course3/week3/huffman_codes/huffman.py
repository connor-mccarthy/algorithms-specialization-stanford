from typing import Dict, List, Tuple

NumSymbol = int
AlphaSymbol = str
Frequency = int
Code = str

Frequencies = List[Frequency]
Distribution = Dict[AlphaSymbol, Frequency]
IntermediateEncoding = Dict[AlphaSymbol, Code]
Encodings = Dict[NumSymbol, Code]


def huffman(frequencies: Frequencies) -> Encodings:
    distribution = weights_to_dist_dict(frequencies)
    encoding = huffman_recursive(distribution)
    return {alpha_to_index(symbol): code for symbol, code in encoding.items()}


def huffman_recursive(distribution: Distribution) -> IntermediateEncoding:
    if is_base_case(distribution):
        return dict(zip(distribution.keys(), ["1", "0"]))

    dist_prime = distribution.copy()
    symbol1, symbol2 = lowest_prob_pair(distribution)
    prob1, prob2 = dist_prime.pop(symbol1), dist_prime.pop(symbol2)
    dist_prime[symbol1 + symbol2] = prob1 + prob2

    encoding = huffman_recursive(dist_prime)
    symbol_encoding_prefix = encoding.pop(symbol1 + symbol2)
    encoding[symbol1], encoding[symbol2] = (
        symbol_encoding_prefix + "0",
        symbol_encoding_prefix + "1",
    )
    return encoding


def is_base_case(distribution: Distribution):
    return len(distribution) == 2


def lowest_prob_pair(distribution: Distribution) -> Tuple[AlphaSymbol, AlphaSymbol]:
    sorted_dist = sorted(distribution.items(), key=lambda item: item[1])
    most_probable_symbol = sorted_dist[0][0]
    second_most_probable_symbol = sorted_dist[1][0]
    return most_probable_symbol, second_most_probable_symbol


def weights_to_dist_dict(weights: List[int]) -> Distribution:
    return {index_to_alpha(i): weight for i, weight in enumerate(weights)}


def index_to_alpha(index: int) -> str:
    return chr(ord("`") + index)


def alpha_to_index(alpha: str) -> int:
    return ord(alpha) - 96
