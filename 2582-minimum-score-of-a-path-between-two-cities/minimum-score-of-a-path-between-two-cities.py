from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        vis = [False] * (n + 1)
        ans = float("inf")

        def dfs(u):
            nonlocal ans
            vis[u] = True

            for v, d in graph[u]:
                ans = min(ans, d)
                if not vis[v]:
                    dfs(v)

        dfs(1)
        return ans
        