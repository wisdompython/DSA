from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        ratio_list = []
        minimum_wage = float("inf")
        t = 0
        for q, w in zip(quality, wage):
            ratio_list.append((w/q, q))
        # we need to create an heap
        ratio_list.sort()
        q_heap = []
        total_q = 0
        for ratio, quality in ratio_list:
            # add to heap
            heapq.heappush(q_heap, -quality) # reverse the heap( from great to small)
            total_q += quality
        # we now need to calculate the sum

            if len(q_heap) > k :
                total_q += heapq.heappop(q_heap) # remember this heap values are negative
            
            if len(q_heap) == k:

                minimum_wage = min(minimum_wage, total_q * ratio)
        return minimum_wage

            
         
