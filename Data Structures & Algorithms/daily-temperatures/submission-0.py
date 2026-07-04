class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # default values 0
        result = [0] * len(temperatures)
        stack = [] # pair: [temp, index] index to calculate difference in days

        for i, t in enumerate(temperatures):
            # while stack not empty and temp is greater than top of stack
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                # comp num days it took to find a greater temperature
                # based on current index i 
                result[stackInd] = (i - stackInd)
            stack.append([t, i])
        return result
                        
