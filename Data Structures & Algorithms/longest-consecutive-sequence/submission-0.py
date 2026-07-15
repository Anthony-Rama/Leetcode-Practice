class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)

        longest = 0 
        for num in nums:
            if num - 1 not in myset:
                streak = 1
                curr = num
                while num + streak in myset:
                    streak += 1
                longest = max(streak, longest)
        
        return longest
                