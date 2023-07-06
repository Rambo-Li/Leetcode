class MinStack:

    def __init__(self):
        self.q = deque([])
        self.m = []

    def push(self, val: int) -> None:
        self.q.append(val)
        if self.m and val >= self.m[-1]:
            self.m.append(self.m[-1])
        else:
            self.m.append(val)

    def pop(self) -> None:
        self.m.pop()
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1] if self.q else False

    def getMin(self) -> int:
        return self.m[-1] if self.m else False
# just record the min value in the array for every position