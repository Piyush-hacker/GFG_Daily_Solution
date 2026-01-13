class Solution:
    def canServe(self, arr):
        count_5 = 0
        count_10 = 0
        count_20 = 0
        # cnt = 0
        for i in arr:

            if i not in [5,10,20]:
                return False
            if i > 5 and count_5 == 0:
                return False
            if i == 5:
                count_5 += 1
            elif i == 10:
                count_10 += 1
                if count_5 == 0:
                    return False
                count_5 -= 1 
            elif i == 20:
                count_20 += 1
                if count_10 == 0 and count_5 < 3:
                    # print(count_5,count_10,count_20)
                    return False
                if count_10 > 0 and count_5 > 0:
                    count_10 -= 1
                    count_5 -= 1
                elif count_10 == 0 and count_5 > 2:
                    count_5 -= 3
            # print((count_5, count_10, count_20), "i - ",cnt)
            # cnt += 1
                    
        return True