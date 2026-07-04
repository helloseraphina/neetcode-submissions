class MinStack:

    def __init__(self):
        self.stack = [] 
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        # get min of val and top of minstack if stack nonempty
        # if it is empty, just min of val and val
        val = min(val, self.minStack[-1] if self.minStack else val)

        #append min val of input val and min of top of minstack
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # get min value from min stack
        # which is always at top of min stack
        return self.minStack[-1]
        
