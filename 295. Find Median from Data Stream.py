class MedianFinder:

    def __init__(self):
        self.leftheap = []
        self.leftcount = 0
        self.rightheap = []
        self.rightcount = 0
        heapify(self.leftheap)
        heapify(self.rightheap)

    def addNum(self, num: int) -> None:
        if not self.rightheap and not self.leftheap:
            heappush(self.rightheap, num)
            self.rightcount += 1
            return
        if num >= self.rightheap[0]:
            if self.rightcount > self.leftcount:
                temp = heappushpop(self.rightheap, num)
                heappush(self.leftheap, -temp)
                self.leftcount += 1
            else:
                heappush(self.rightheap, num)
                self.rightcount += 1
        else:
            if self.leftcount > self.rightcount:
                temp = -heappushpop(self.leftheap, -num)
                heappush(self.rightheap, temp)
                self.rightcount += 1
            else:
                heappush(self.leftheap, -num)
                self.leftcount += 1
        # print(self.leftheap, self.leftcount, self.rightheap, self.rightcount)

    def findMedian(self) -> float:
        if self.leftcount == self.rightcount:
            return (-self.leftheap[0] + self.rightheap[0])/2
        elif self.leftcount > self.rightcount:
            return -self.leftheap[0]
        else:
            return self.rightheap[0]