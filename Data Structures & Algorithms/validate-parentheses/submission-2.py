class Solution:
    def isValid(self, s: str) -> bool:
        # stack its like an array/list but you can only remove from the top/end of the array 
        # LIFO last in first out 

        myDict = { 
            '(':')', 
            '{':'}',
            '[':']'
        }

        
        stack = []
        for char in s:
            if char in ('(', '{', '['):
                stack.append(char)
            if (char in (')', '}', ']') or char in ('(', '{', '[')) and not stack:
                return False
            if char in (')', '}', ']') and stack:
                if char == myDict[stack[-1]]:
                    stack.pop()
                else:
                    return False
            
        return not stack