class Solution:
    def isValid(self, s: str) -> bool:
        # stack its like an array/list but you can only remove from the top/end of the array 
        # LIFO last in first out 

        myDict = { 
            ')':'(', 
            '}':'{',
            ']':'['
        }

        
        stack = []
        for char in s:
            if char in myDict:
                if stack and stack[-1] == myDict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if stack:
            return False
        else:
            return True
