#User function Template for python3

class Solution:
    
    #Function to find the largest number after k swaps.
    def findMaximumNum(self,s,k):
        def solve(start,k):
            if k==0 or start>=n:
                return  
            max_val='0' 
            for i in range(start+1,n):
                max_val=max(max_val,arr[i]) 
            for i in range(start+1,n):
                if arr[i]>arr[start] and arr[i]==max_val:
                    #now swap
                    arr[i],arr[start]=arr[start],arr[i] 
                    solve(start+1,k-1) 
                    #check if greater num found
                    if res[0]<"".join(arr):
                        res[0]="".join(arr)
                    #now again swap to see if some another elem is greater
                    arr[i],arr[start]=arr[start],arr[i]  
            solve(start+1,k)
        arr=[i for i in s]
        n=len(s)
        res = [s] 
        solve(0,k)
        return res[0]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob = Solution()
        print(ob.findMaximumNum(s, k))

        print("~")

# } Driver Code Ends