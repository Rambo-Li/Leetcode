# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         td = {}
#         for t in tasks:
#             td[t] = td.get(t, 0) + 1
#         taskCount = [(-b,a) for a,b in td.items()]
#         heapify(taskCount)

#         pos = 0
#         idle = 0
#         taskPointer = {}
#         while taskCount:
#             count, ta = heappop(taskCount)
#             print(-count, ta)
#             if ta in taskPointer:
#                 if taskPointer[ta]+n+1 > pos:
#                     idle += taskPointer[ta] + n - pos +1
#                     taskPointer[ta] += n+1
#                     pos = taskPointer[ta] + 1
#                 else:
#                     taskPointer[ta] = pos
#                     pos += 1
#             else:
#                 if idle:
#                     idle -= 1
#                 else:
#                     taskPointer[ta] = pos
#                     pos += 1

#             if count<-1:
#                 heappush(taskCount, (count+1, ta))
#             print(taskPointer, idle, pos)
#         return pos

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = [0] * 26
        for i in tasks: cnt[ord(i) - ord('A')] += 1
        mx, mxcnt = max(cnt), 0
        for i in cnt: 
            if i == mx: mxcnt += 1
        return max((mx - 1) * (n + 1) + mxcnt, len(tasks))
    
# the best solution nailed down the idea that we only need to fit the longest. 