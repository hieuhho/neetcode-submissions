class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []

        # do a recursion
        # check for number of open and close
        # if open and close == n, add stack to ans, return
        # if open < n, add open to stack, continue to recurse with open count + 1
        # if close < open, add close to stack, continue to recurse with close count + 1

        def recurse(open_count, close_count):
            if open_count == close_count == n:
                ans.append("".join(stack))
                return

            if open_count < n:
                stack.append('(')
                recurse(open_count + 1, close_count)
                stack.pop()
            
            if close_count < open_count:
                stack.append(')')
                recurse(open_count, close_count + 1)
                stack.pop()
        
        recurse(0, 0)
        return ans