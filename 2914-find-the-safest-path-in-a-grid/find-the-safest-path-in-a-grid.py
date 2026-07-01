class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        from collections import deque
from heapq import *

class Solution:
    def maximumSafenessFactor(self, g):
        n=len(g)
        d=[[-1]*n for _ in range(n)]
        q=deque()
        for i in range(n):
            for j in range(n):
                if g[i][j]:
                    d[i][j]=0
                    q.append((i,j))
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            x,y=q.popleft()
            for dx,dy in dirs:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<n and d[nx][ny]==-1:
                    d[nx][ny]=d[x][y]+1
                    q.append((nx,ny))
        h=[(-d[0][0],0,0)]
        vis={(0,0)}
        while h:
            s,x,y=heappop(h)
            s=-s
            if (x,y)==(n-1,n-1):
                return s
            for dx,dy in dirs:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<n and (nx,ny) not in vis:
                    vis.add((nx,ny))
                    heappush(h,(-min(s,d[nx][ny]),nx,ny))