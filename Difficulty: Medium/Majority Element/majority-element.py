#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #code here
        n = len(arr)
        freq = {}
        
        for i in arr:
            freq[i] = freq.get(i,0) + 1
            
        for i in freq:
            if freq[i] > n // 2:
                return i
                
        return -1