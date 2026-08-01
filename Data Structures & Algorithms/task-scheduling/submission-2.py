class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)

        t = 0
        q = collections.deque()

        while q or heap:
            t += 1
            if heap:
                task = 1 + heapq.heappop(heap)
                if task:
                    q.append([task,t+n])

            if q and q[0][1] == t:
                    heapq.heappush(heap,q.popleft()[0])
            
        return t