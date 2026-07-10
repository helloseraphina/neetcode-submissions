class Solution:
    def climbStairs(self, n: int) -> int:
        # num ways depend only on prev two steps
        # two variables that rep 
        # one = way to reach current step
        # two = ways to reach previous step
        # start both as 1 (base case)
        one, two = 1, 1

        for i in range(n - 1):
            # store one in temp value before update
            temp = one
            one = one + two # adding two prev values
            # shift two to prev value of one
            two = temp
        
        return one
        