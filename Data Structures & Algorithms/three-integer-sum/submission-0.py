class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums so we can use two pointers
        nums.sort()
        triplets = []

        for i, a in enumerate(nums):
            # if it isnt first value in input array and
            # if same value as before
            # continue so we dont use duplicate value
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            # search while pointers havent crossed
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    triplets.append([a, nums[l], nums[r]])
                    # move l pointer to continue
                    l += 1 
                    # skip same val and never exceeds r pointer
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return triplets