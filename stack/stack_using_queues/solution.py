class MyStack:
    """
    MyStack class implements a stack using two queues.
    """

    def __init__(self):
        """
        Initializes the stack with two empty queues.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        """
        Pushes element x to the top of the stack.

        Args:
            x (int): The element to be pushed onto the stack.
        """
        if len(self.q1) == 1 and len(self.q2) > 0:
            self.q2.append(self.q1[0])
        while self.q2:
            self.q1.append(self.q2[0])
            self.q2 = self.q2[1:]
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on the top of the stack and returns it.

        Returns:
            int: The element on the top of the stack.
        """
        if len(self.q1) == 1 and len(self.q2) > 0:
            self.q2.append(self.q1[0])
            self.q1.pop()
            while len(self.q2) > 1:
                self.q1.append(self.q2[0])
                self.q2 = self.q2[1:]
            return self.q2.pop()
        elif len(self.q1) == 0 and len(self.q2) > 0:
            while len(self.q2) > 1:
                self.q1.append(self.q2[0])
                self.q2 = self.q2[1:]
            return self.q2.pop()
        else:
            while len(self.q1) > 1:
                self.q2.append(self.q1[0])
                self.q1 = self.q1[1:]
            return self.q1.pop()

    def top(self) -> int:
        """
        Returns the element on the top of the stack.

        Returns:
            int: The element on the top of the stack.
        """
        if len(self.q1) == 0 and len(self.q2) > 0:
            while self.q2:
                self.q1.append(self.q2[0])
                self.q2 = self.q2[1:]
        while len(self.q1) > 1:
            self.q2.append(self.q1[0])
            self.q1 = self.q1[1:]
        return self.q1[0]

    def empty(self) -> bool:
        """
        Returns true if the stack is empty, false otherwise.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.q1) + len(self.q2) == 0


# Example usage
myStack = MyStack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)
print(myStack.top())   # return 5
print(myStack.pop())   # return 5
print(myStack.pop())   # return 4
print(myStack.empty())   # return False
