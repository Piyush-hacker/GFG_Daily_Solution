class Solution:
    def missingNumber(self, arr):
        a=set(arr)
        count=1
        while True:
            if count not in a:
                return count
            count+=1