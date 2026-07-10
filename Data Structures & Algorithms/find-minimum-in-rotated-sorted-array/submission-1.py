class Solution:
    def findMin(self, nums: List[int]) -> int:
        # # brute force
        # return min(nums)

        # init l, r pointers
        l, r = 0, len(nums) - 1
        # init current answer (first ele)
        # target = nums[0]

        # while l <= r:
        #     # if current window already sorted
        #     # update answer compared with nums[left]
        #     if nums[l] < nums[r]:
        #         target = min(target, nums[l])
        #         break

        #     # if array unsorted, do binary search
        #     mid = (l + r) // 2
        #     # update answer to middle val
        #     target = min(target, nums[mid])

        #     if nums[mid] >= nums[l]:
        #         l = mid + 1
            
        #     else:
        #         # in right sorted portion so we want to search left
        #         r = mid - 1
        # return target

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                # move pointer cause min is on left
                r = mid 
            else:
                # min is on right
                l = mid + 1
        return nums[l]

        