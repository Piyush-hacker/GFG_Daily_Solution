class Solution:
    def rearrange(self, arr, x):
        # code here
        arr.sort(key=lambda item:abs(item-x))
        
        