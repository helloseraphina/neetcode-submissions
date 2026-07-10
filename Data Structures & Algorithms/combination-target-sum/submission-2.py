class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # sort nums to stop early when sum > target
        nums.sort()

        def dfs(i, cur, total):
            # define base cases
            if total == target:
                # maintaining only single varibale list for current for recursive use
                # so create copy otherwise we are modifying original
                res.append(cur.copy())
                return

            for j in range (i, len(nums)):
                if total + nums[j] > target:
                    # stop loop as we no need to check larger nums
                    return
                # add nums[j] to current list
                cur.append(nums[j])
                # call dfs
                # reuse allowed
                dfs(j, cur, total + nums[j])
                cur.pop() # pop last candidate to backtrack

            # # out of bounds, so cannot find further combos
            # if i >= len(nums) or total > target:
            #     return
            
            # cur.append(nums[i])
            # dfs(i, cur, total + nums[i])
            # cur.pop() # pop candidate to backtrack
            # dfs(i + 1, cur, total)
        
        # call dfs to start recursion
        # 0 beginningn index, empty array as current combo, 0 as total
        dfs(0, [], 0)
        return res
        