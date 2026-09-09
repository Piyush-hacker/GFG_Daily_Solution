class Solution:
    def getNum(self, arr):
        n = 0
        for i in arr:
            n = n * 10 + i
        return n

    def findMax(self, n):
        # code here
        arr = []
        mxn = n
        while n > 0:
            arr.append(n%10)
            n //= 10

        arr = arr[::-1]
        t = sum(arr)
        mx = t

        for i in range(len(arr) - 2, -1, -1):
            arr[i] -= 1
            t += 9 - 1 - arr[i + 1]
            arr[i+1] = 9

            if t > mx:
                mx = t
                mxn = self.getNum(arr)
        return mxn           