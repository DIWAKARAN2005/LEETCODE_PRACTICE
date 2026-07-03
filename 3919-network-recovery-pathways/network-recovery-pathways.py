from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:

        n = len(online)
        g = [[] for _ in range(n)]
        indeg = [0] * n
        mx = 0

        for u, v, w in edges:
            g[u].append((v, w))
            indeg[v] += 1
            mx = max(mx, w)

        q = deque(i for i in range(n) if indeg[i] == 0)
        topo = []

        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        def check(x):
            dist = [float("inf")] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == float("inf"):
                    continue
                if u not in (0, n - 1) and not online[u]:
                    continue

                for v, w in g[u]:
                    if w >= x and (v == n - 1 or online[v]):
                        dist[v] = min(dist[v], dist[u] + w)

            return dist[-1] <= k

        l, r, ans = 0, mx, -1

        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans