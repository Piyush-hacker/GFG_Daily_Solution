class Solution:
    def maxArea(self, mat):
        # code here
        # algorithm: scan row by row and compute the max histogram

        # calculate the histogram given height
        def max_area(heights):
            # compute the histogram for each height.
            # find the closeser smaller height left and right for each height[i]
            # area = height[i] * (right[i]-left[i]-1)
            n = len(heights)
            right = [n]*n
            stack = []
            for i in range(n):
                while stack and heights[stack[-1]] > heights[i]:
                    right[stack.pop()] = i
                stack.append(i)
                
            left = [-1]*n
            stack.clear()
            for i in range(n-1, -1, -1):
                while stack and heights[stack[-1]] > heights[i]:
                    left[stack.pop()] = i
                stack.append(i)
            
            r = 0
            for i in range(n):
                r = max(r, height[i]*(right[i]-left[i]-1))
            #print(f"{heights = }, {r = }")
            return r
            
        height = [0]*len(mat[0])
        ans = 0
        for r in mat:
            for i in range(len(r)):
                if r[i] == 0:
                    height[i] = 0
                else:
                    height[i] += 1
            ans = max(ans, max_area(height))
        return ans