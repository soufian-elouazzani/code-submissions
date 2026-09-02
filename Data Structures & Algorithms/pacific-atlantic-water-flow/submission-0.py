class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(i, j, visited):
            visited.add((i, j))
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                # Check boundaries and if water can flow FROM neighbor TO current
                if (0 <= ni < rows and 0 <= nj < cols and 
                    (ni, nj) not in visited and 
                    heights[ni][nj] >= heights[i][j]):  # ← KEY: neighbor must be >= current
                    dfs(ni, nj, visited)


        # Start from Pacific edges (top row, left column)
        for i in range(rows):
            dfs(i, 0, pacific)  # Left edge (Pacific)
            dfs(i, cols-1, atlantic)  # Right edge (Atlantic)
        
        for j in range(cols):
            dfs(0, j, pacific)  # Top edge (Pacific)
            dfs(rows-1, j, atlantic)  # Bottom edge (Atlantic)
        
        # Cells that can reach both oceans
        result = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacific and (i, j) in atlantic:
                    result.append([i, j])
        
        return result
