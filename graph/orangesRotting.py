from typing import List
from collections import deque
class Solution:
    def orangesRotting(self,m,n,grid)->int:
        queue=deque()

        fresh_count=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh_count+=1

        if fresh_count==0:
            return 0

        minutes=0
        directions=[
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]
        while queue and fresh_count>0:
            minutes+=1
            for _ in range(len(queue)):
                r,c=queue.popleft()

                for go_r,go_c in directions:
                    new_r,new_c=r+go_r,c+go_c
                    if  0<=new_c<m and 0<=new_r<n and grid[new_r][new_c]==1:
                        grid[new_r][new_c]=2
                        fresh_count-=1
                        queue.append((new_r,new_c))
        return minutes if fresh_count==0 else -1

def main()->None:
    m,n=map(int,input().split())
    grid=[list(map(int,input().split())) for _ in range(m)]
    print(Solution().orangesRotting(m,n,grid))

if __name__ == "__main__":
    main()