from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator, List, Optional, Tuple


@dataclass
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

    def as_primitives(self) -> List[Tuple[int, int, int]]:
        return [edge.as_tuple() for edge in self.edges]

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

    def __delitem__(self, key):
        del self.edges[key]

    def __getitem__(self, key):
        return self.edges[key]

    def __setitem__(self, key, value):
        assert isinstance(value, Edge)
        self.edges[key] = value
