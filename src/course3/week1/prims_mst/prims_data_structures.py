from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator, Optional, Set


@dataclass(unsafe_hash=True)
class Edge:
    start: int
    end: int
    weight: Optional[int] = None

    @property
    def is_weighted(self) -> bool:
        return hasattr(self, "weight") and self.weight is not None

    def as_tuple(self):
        return (self.start, self.end, self.weight)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Edge):
            return NotImplemented
        if (
            set((self.start, self.end)) == set((other.start, other.end))
            and self.is_weighted == other.is_weighted
        ):
            if not self.is_weighted or self.weight == other.weight:
                return True
        else:
            return False


class Graph:
    def __init__(self, *edges) -> None:
        self.edges = list(edges)

    def __iter__(self) -> Iterator:
        return iter(self.edges)

    @property
    def size(self) -> int:
        return len(self.edges)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Graph):
            return NotImplemented

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
            return NotImplemented
        edges = self.edges + [edge]
        return Graph(*edges)

    @property
    def starts(self) -> Set[int]:
        return {edge.start for edge in self}

    @property
    def ends(self) -> Set[int]:
        return {edge.ends for edge in self}

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
