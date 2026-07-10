class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Our current "goal" is initially the last index,
        # since that's where we ultimately want to reach.
        goal = len(nums) - 1

        # Traverse the array backwards, starting from the
        # second-to-last index and moving to index 0.
        for i in range(len(nums) - 2, -1, -1):

            # nums[i] is the maximum jump length from index i.
            #
            # If the furthest we can jump from i reaches or passes
            # the current goal, then index i itself becomes a new goal.
            #
            # Example:
            # goal = 5
            # i = 3
            # nums[3] = 2
            #
            # 3 + 2 = 5 >= goal
            #
            # Since we can jump from index 3 to the goal,
            # we now only need to know if we can reach index 3.
            if i + nums[i] >= goal:

                # Move ("shift") the goal backwards.
                # Instead of trying to reach the original end,
                # our new target is simply reaching index i.
                goal = i

        # If the goal has been moved all the way back to index 0,
        # then we can reach the last index starting from the beginning.
        return goal == 0