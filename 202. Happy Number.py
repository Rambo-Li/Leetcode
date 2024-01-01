class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            next_n = 0
            while n >0:
                n, r = divmod(n, 10)
                next_n += r**2
            if next_n == 1:
                return True
            elif next_n in visited:
                return False
            visited.add(next_n)
            n = next_n

"""
Concept: Squared digits will form a cycle
DS: hashmap to detect reoccurrence
Algo: update the hashmap when generating a new number"""