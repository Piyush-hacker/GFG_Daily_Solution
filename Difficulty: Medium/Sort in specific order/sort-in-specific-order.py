class Solution:
    def sortIt(self, arr):
       
        n=len(arr)

        #Convert all odd numbers to negative,so that when general sort is applied            #all odd values will be before even numbers and also odd numbers will be            #sorted in decreasing order of their absolute value

        for i in range(n):
            if arr[i]%2!=0:
                arr[i]=-arr[i]
        arr.sort()
        for i in range(n):
            if arr[i]>-1:
                break
            arr[i]=-arr[i]
        return arr

