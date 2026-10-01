import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
       
        count = Counter(tasks)
        
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        
        wait_queue = deque()
        
        time = 0
        
        while max_heap or wait_queue:
            time += 1
            
            if max_heap:
                
                cnt = 1 + heapq.heappop(max_heap)
     
                if cnt != 0:
                    wait_queue.append([cnt, time + n])
     
            if wait_queue and wait_queue[0][1] == time:
                heapq.heappush(max_heap, wait_queue.popleft()[0])
                
        return time