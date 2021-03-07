import heapq
import os
from typing import List


def get_data() -> List[int]:
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "median_maintenance_assignment_data.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    split_lines = [line.strip().split(" ") for line in lines]
    return [int(element) for line in split_lines for element in line]


class MedianMaintainer:
    def __init__(self) -> None:
        self.hlow: List[int] = []
        self.hhigh: List[int] = []

    @property
    def is_empty(self) -> bool:
        return len(self.hlow + self.hhigh) == 0

    @property
    def hhigh_min(self) -> int:
        return heapq.nsmallest(1, self.hhigh)[0]

    @property
    def hlow_max(self) -> int:
        return heapq.nlargest(1, self.hlow)[0]

    def rebalance(self) -> None:
        if len(self.hlow) > len(self.hhigh) + 1:
            max_e_from_min_hlow = heapq._heappop_max(self.hlow)  # type: ignore
            heapq.heappush(self.hhigh, max_e_from_min_hlow)
        elif len(self.hhigh) > len(self.hlow) + 1:
            min_e_from_hhigh = heapq.heappop(self.hhigh)
            heapq.heappush(self.hlow, min_e_from_hhigh)
            heapq._heapify_max(self.hlow)

    def insert(self, element: int) -> None:
        if self.is_empty or element < self.hlow_max:
            heapq.heappush(self.hlow, element)
            heapq._heapify_max(self.hlow)
        else:
            heapq.heappush(self.hhigh, element)
        self.rebalance()

    @property
    def median(self) -> int:
        odd_no_elements = len(self.hlow + self.hhigh) % 2 != 0
        if odd_no_elements:
            if len(self.hlow) > len(self.hhigh):
                return self.hlow_max
            else:
                return self.hhigh_min
        else:
            return self.hlow_max
