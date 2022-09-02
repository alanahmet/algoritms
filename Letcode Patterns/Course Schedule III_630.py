class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        time = 0
        maxHeap = []

        for d, ld in sorted(courses, key=lambda x: x[1]):
            heapq.heappush(maxHeap, -d)
            time += d

            if time > ld:
                time += heapq.heappop(maxHeap)
        return len(maxHeap)
