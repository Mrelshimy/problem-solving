## Problem Description

Design a stack that supports the following operations in constant time complexity:

- `push(val)`: Pushes the element `val` onto the stack.
- `pop()`: Removes the element on the top of the stack.
- `top()`: Retrieves the top element of the stack.
- `getMin()`: Retrieves the minimum element in the stack.

You must implement the `MinStack` class with O(1) time complexity for each operation.

### Example

```python
# Example usage:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()   # return -3
minStack.pop()
minStack.top()      # return 0
minStack.getMin()   # return -2
```

### Constraints

- Values pushed (val) into the stack are within the range -2^31 to 2^31 - 1.
- Operations pop(), top(), and getMin() are always called on non-empty stacks.
- There will be at most 30,000 calls to push(), pop(), top(), and getMin() combined.
