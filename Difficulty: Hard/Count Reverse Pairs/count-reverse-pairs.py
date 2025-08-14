class Solution:
    def countRevPairs(self, arr):
        def merge_sort(nums, l, r):
            if l >= r:
                return 0
            mid = (l + r) // 2
            count = merge_sort(nums, l, mid) + merge_sort(nums, mid + 1, r)

            # Count reverse pairs across halves
            j = mid + 1
            for i in range(l, mid + 1):
                while j <= r and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            # Merge step
            temp = []
            p1, p2 = l, mid + 1
            while p1 <= mid and p2 <= r:
                if nums[p1] <= nums[p2]:
                    temp.append(nums[p1])
                    p1 += 1
                else:
                    temp.append(nums[p2])
                    p2 += 1
            temp.extend(nums[p1:mid + 1])
            temp.extend(nums[p2:r + 1])
            nums[l:r + 1] = temp

            return count

        return merge_sort(arr, 0, len(arr) - 1)

        return merge_sort(arr, 0, len(arr) - 1)