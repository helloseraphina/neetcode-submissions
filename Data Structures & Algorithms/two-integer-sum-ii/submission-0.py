class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]
        
            # if current sum is bigger than target
            # move r to reduce sum
            if curSum > target:
                r -= 1
            # if sum smaller than target
            # move l to increase sum
            elif curSum < target:
                l += 1
            # if cursum == target
            else:
                return [l + 1, r + 1]
        
        return []