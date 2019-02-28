import copy
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        elapse = 0
        grid_new = copy.deepcopy(grid)
        elapse = self.rot(grid, grid_new, elapse)
        return elapse
        
    def rot(self, grid, grid_new, elapse):
        col = len(grid)
        row = len(grid[0])
        rotten = []
        for i in range(len(grid_new)):
            for j in range(len(grid_new[i])):
                if grid_new[i][j] == 2:
                    rotten.append([i,j])
        for idx_pair in rotten:
            i = idx_pair[0]
            j = idx_pair[1]
            if j > 0 and grid_new[i][j-1] and grid_new[i][j-1] == 1:
                grid_new[i][j-1] = 2
            if i > 0 and grid_new[i-1][j] and grid_new[i-1][j] == 1:
                grid_new[i-1][j] = 2
            if i < col-1 and grid_new[i+1][j] and grid_new[i+1][j] == 1:
                grid_new[i+1][j] = 2
            if j < row-1 and grid_new[i][j+1] and grid_new[i][j+1] == 1:
                grid_new[i][j+1] = 2
        if grid == grid_new:
            for row in grid:
                if 1 in row:
                    elapse = -1
                    break
            return elapse
        elapse += 1
        grid = copy.deepcopy(grid_new)
        return self.rot(grid, grid_new, elapse)
