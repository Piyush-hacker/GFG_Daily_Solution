class Solution:
    def orangesRot(self, mat):
        r, c = len(mat), len(mat[0])
        q, fresh = [], 0

        for i in range(r):
            for j in range(c):
                if mat[i][j] == 2: q.append((i, j))
                elif mat[i][j] == 1: fresh += 1

        time = 0
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while q and fresh:
            new_q = []
            for x, y in q:
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < r and 0 <= ny < c and mat[nx][ny] == 1:
                        mat[nx][ny] = 2
                        fresh -= 1
                        new_q.append((nx, ny))
            q = new_q
            time += 1

        return time if fresh == 0 else -1