import pytest

from dijkstra import dijkstra

input1 = """
1	2,1	8,2

2	1,1	3,1

3	2,1	4,1

4	3,1	5,1

5	4,1	6,1

6	5,1	7,1

7	6,1	8,1

8	7,1	1,2
"""

expected1 = """
1 0 []

2 1 [2]

3 2 [2, 3]

4 3 [2, 3, 4]

5 4 [2, 3, 4, 5]

6 4 [8, 7, 6]

7 3 [8, 7]

8 2 [8]

"""


@pytest.mark.parametrize("input_data, expected", [(input1, expected1)])
def test_dijkstra(input_data, expected):
    graph = []
    actual = dijkstra(graph)
    expected = []
    assert actual == expected
