class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 # start of the string
        r = len(s) - 1 # end of the string

        # 1.) Check if alphanumeric 
        # 2.) Check if s[l] == s[r]

        while l < r: # iterating over entire string based on the condition that l will not pass r 
            if s[l].isalnum() == False: # skips non-alpanumeric values in string s 
                l += 1
                pass
            elif s[r].isalnum() == False: # skips non-alpanumeric values in string s 
                r -= 1
                pass
            elif s[l].lower() != s[r].lower(): #h != w
                return False
            else:
                l += 1
                r -= 1
        return True
            
            
