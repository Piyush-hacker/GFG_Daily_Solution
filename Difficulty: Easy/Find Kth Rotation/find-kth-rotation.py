class Solution:
    def findKRotation(self, arr):
        k,min_val = min(enumerate(arr),key = lambda x:x[1]) #find the index of minimum element which will gradually gives you the number of rotation.
        if k == 0:
            return 0
        return k    