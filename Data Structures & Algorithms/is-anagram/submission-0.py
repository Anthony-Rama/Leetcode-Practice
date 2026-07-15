class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = defaultdict(int)
        tCount = defaultdict(int)

        for letter in s:
            sCount[letter] += 1
        
        for letter in t:
            tCount[letter] += 1
        
        return sCount == tCount