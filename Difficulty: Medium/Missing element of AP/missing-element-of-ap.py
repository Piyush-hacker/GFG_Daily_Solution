#User function Template for python3

class Solution:
    def findMissing(self, arr):
        # code here
        n=len(arr)
        l=arr[1]-arr[0]
        for i in range(2,n):
            if arr[i-1]!=arr[i]-l:
                return arr[i]-l
        return arr[n-1]+l


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
import math


def main():
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    solution = Solution()

    for i in range(1, t + 1):
        arr = list(map(int, data[i].split()))
        print(solution.findMissing(arr))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends