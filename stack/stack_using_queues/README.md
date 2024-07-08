## Implement Stack using Queues

- Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `pop`, `top`, and `empty`).
- You must use only standard operations of a queue: push to back, peek/pop from front, size, and is empty operations.

### Example

```python
# Example usage:
myStack = MyStack()
myStack.push(1)
myStack.push(2)
myStack.top()     # Output: 2
myStack.pop()     # Output: 2
myStack.empty()   # Output: False
```

### Constraints

- 1 <= x <= 9 (values pushed onto the stack)
- At most 100 calls will be made to push, pop, top, and empty.
- All calls to pop and top are valid.

