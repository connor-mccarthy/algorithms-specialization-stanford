import heapq
import os
from typing import List, Tuple


def get_data() -> List[List[int]]:
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
        self.all_items = []  # delete me!

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
            max_e_from_min_hlow = heapq._heappop_max(self.hlow)
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
        self.all_items.append(element)  # delete me

    @property
    def median(self) -> Tuple[int]:
        odd_no_elements = len(self.hlow + self.hhigh) % 2 != 0
        if odd_no_elements:
            if len(self.hlow) > len(self.hhigh):
                return self.hlow_max
            else:
                return self.hhigh_min
        else:
            return self.hlow_max

    @property
    def median_checker(self):
        sorted_list = sorted(self.all_items)
        length = len(sorted_list)
        if length % 2 == 0:
            return sorted_list[(length // 2) - 1]
        else:
            return sorted_list[((length + 1) // 2) - 1]


if __name__ == "__main__":
    data = get_data()

    mm = MedianMaintainer()

    total = 0
    for element in data:
        mm.insert(element)
        total += mm.median

    final_answer = total % 10_000
    print(final_answer)
