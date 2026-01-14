class Solution:

    def catchThieves(self, arr, k):

        police = []

        thief = []

 

        # Store indices of policemen and thieves

        for i in range(len(arr)):

            if arr[i] == 'P':

                police.append(i)

            else:

                thief.append(i)

 

        i = j = 0

        count = 0

 

        # Two-pointer approach

        while i < len(police) and j < len(thief):

            if abs(police[i] - thief[j]) <= k:

                count += 1

                i += 1

                j += 1

            elif thief[j] < police[i]:

                j += 1

            else:

                i += 1

 

        return count

