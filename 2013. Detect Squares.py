class DetectSquares:

    def __init__(self):
        self.pcount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pcount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for x, y in self.pcount:
            if abs(x-px) == abs(y-py) and abs(x-px)>0 and (px,y) in self.pcount and (x, py) in self.pcount:
                res += self.pcount[(x,y)]*self.pcount[(px,y)]*self.pcount[(x,py)]
        return res

"""
Concept: how to detect a square? The diagonal points has a property of abs(x-x1)==abs(y-y1)
DS: a dict to store the count of points
Algo: enumerate the points, check if diagonal and two corners are present
"""