class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.hp = nums[:k]
        heapify(self.hp)
        for n in nums[k:]:
            if n > self.hp[0]:
                heappushpop(self.hp, n)

    def add(self, val: int) -> int:
        if  len(self.hp)>= self.k and val > self.hp[0]:
            heappushpop(self.hp, val)
        elif len(self.hp) < self.k:
            heappush(self.hp, val)
        return self.hp[0]