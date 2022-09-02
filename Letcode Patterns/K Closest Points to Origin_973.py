class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:K]

#         maxHeap = []
#         for x, y in points:
#             heapq.heappush(maxHeap, (-(x ** 2 + y ** 2), [x, y]))
#             if len(maxHeap) > K:
#                 heapq.heappop(maxHeap)
#         return [p for s, p in maxHeap]
