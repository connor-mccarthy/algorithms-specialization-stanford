from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator, Set, Union


@dataclass(unsafe_hash=True)
class Edge:  # pragma: no cover -> this is a direct copy of the file from prims and is tested thoroughly there
    start: int
    end: int
    weight: Union[int, float]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Edge):
            raise NotImplementedError
        return (
            set((self.start, self.end)) == set((other.start, other.end))
            and self.weight == other.weight
        )

    def __lt__(self, other: Edge) -> bool:
        if not isinstance(other, Edge):
            raise NotImplementedError
        return self.weight < other.weight

    def __le__(self, other: Edge) -> bool:
        if not isinstance(other, Edge):
            raise NotImplementedError
        return self.weight <= other.weight

    @property
    def vertices(self):
        return {self.start, self.end}


class Graph:  # pragma: no cover -> this is a direct copy of the file from prims and is tested thoroughly there
    def __init__(self, *edges) -> None:
        self.edges = list(edges)

    def __iter__(self) -> Iterator:
        return iter(self.edges)

    @property
    def size(self) -> int:
        return len(self.edges)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Graph):
            raise NotImplementedError

        if self.size != other.size:
            return False

        return (all(edge in other for edge in self)) and (
            all(edge in self for edge in other)
        )

    def __delitem__(self, key: int) -> None:
        del self.edges[key]

    def __getitem__(self, key: int) -> Edge:
        return self.edges[key]

    def __setitem__(self, key: int, value: Edge) -> None:
        assert isinstance(value, Edge)
        self.edges[key] = value

    def __add__(self, edge: object) -> Graph:
        if not isinstance(edge, Edge):
            raise NotImplementedError
        edges = self.edges + [edge]
        return Graph(*edges)

    @property
    def starts(self) -> Set[int]:
        return {edge.start for edge in self}

    @property
    def ends(self) -> Set[int]:
        return {edge.end for edge in self}

    @property
    def cost(self) -> int:
        return sum(edge.weight for edge in self.edges)

    @property
    def vertices(self) -> Set[int]:
        vertices = set()
        for edge in self:
            vertices.add(edge.start)
            vertices.add(edge.end)
        return vertices

    def __str__(self):
        if self.size > 10:
            return str(self.edges[:10])[:-1] + "..." + "]"
        else:
            return str(self.edges)

    def reverse(self) -> Graph:
        return Graph(*[Edge(edge.end, edge.start, edge.weight) for edge in self.edges])
