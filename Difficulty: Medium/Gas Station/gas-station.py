class Solution:
    def startStation(self, gas, cost):
        #  code here
        
        n = len(gas)
        s, cnt = 0, 0
        for i in range(2*n):
            s += gas[i%n]-cost[i%n]
            if s < 0:
                s = 0
                cnt = 0
            else:
                cnt += 1
            if cnt == n:
                return i+1-n
        return -1