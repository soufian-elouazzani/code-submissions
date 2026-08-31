class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])
        visited = set()
        num_islands = 0

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            if grid[i][j] == "0":
                return 
            if (i, j) in visited:
                return

            visited.add((i,j))

            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)


        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in visited :
                    num_islands += 1
                    dfs(i, j)
        return num_islands
        
