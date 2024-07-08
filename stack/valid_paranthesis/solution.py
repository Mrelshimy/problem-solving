class Solution:
    """
    A class to determine if a given string of parentheses is valid.
    """

    def isValid(self, s: str) -> bool:
        """
        Check if all brackets in the string are closed
        and in the same order of opening.

        Args:
            s (str): The input string containing just the characters
            '(', ')', '{', '}', '[' and ']'.

        Returns:
            bool: True if the input string is valid, False otherwise.
        """

        paranthesis = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        if s[0] in paranthesis.keys() or len(s) % 2 != 0:
            return False

        stack = [1]
        for x in s:
            if x in paranthesis.values():
                stack.append(x)
            else:
                if stack[-1] == paranthesis[x]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 1:
            return True
        else:
            return False


# Example usage
s = "(}"
res = Solution()
print(res.isValid(s))  # return False
