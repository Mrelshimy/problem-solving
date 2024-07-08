class MinStack:
    """
    MinStack class supports push, pop, top, and getMin operations
    with O(1) time complexity for each.

    Attributes:
        stack (list): List to store stack elements.
        min_list (list): List to store minimum values encountered in the stack.
    """

    def __init__(self):
        """ Initializes an empty MinStack. """
        self.stack = []
        self.min_list = []

    def push(self, val: int) -> None:
        """ Pushes the element val onto the stack.
        Args:
            val (int): The element to be pushed onto the stack.
        """
        if not self.min_list or val <= self.min_list[-1]:
            self.min_list.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        """ Removes the element on the top of the stack. """
        if self.stack:
            if self.stack[-1] == self.min_list[-1]:
                self.min_list.pop()
            self.stack.pop()

    def top(self) -> int:
        """
        Retrieves the top element of the stack without removing it.

        Returns:
            int: The top element of the stack, or None if the stack is empty.
        """
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        """
        Retrieves the minimum element in the stack.

        Returns:
            int: The minimum element in the stack
            or None if the stack is empty.
        """
        if self.min_list:
            return self.min_list[-1]
        else:
            return None


# Testing Solution

obj = MinStack()
obj.push(0)
obj.push(-1)
obj.push(-2)
obj.push(5)
obj.push(3)
obj.push(-4)
print(obj.stack)
param_1 = obj.getMin()
print(param_1)
obj.pop()
print(obj.stack)
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3, param_4)
