class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        from collections import deque

class Solution:
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])
        q = deque([(0, 0, health - grid[0][0])])
        vis = [[-1] * n for _ in range(m)]
        vis[0][0] = health - grid[0][0]

        while q:
            x, y, h = q.popleft()

            if h <= 0:
                continue
            if x == m - 1 and y == n - 1:
                return True

            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nh = h - grid[nx][ny]
                    if nh > vis[nx][ny]:
                        vis[nx][ny] = nh
                        q.append((nx, ny, nh))

        return False