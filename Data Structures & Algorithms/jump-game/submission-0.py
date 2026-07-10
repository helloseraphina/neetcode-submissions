class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            # jump len = nums[i]
            # if this condition is true, we can reach the goal
            if i + nums[i] >= goal:
                # shift goal post to where we are jumping from
                goal = i

        if goal == 0:
            return True
        else:
            # goal > 0
            # not able to reach end of input list
            return False

