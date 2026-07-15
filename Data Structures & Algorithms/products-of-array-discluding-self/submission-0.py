class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        myDict = defaultdict(int)

        for i in range(len(nums)):
            myDict[i] = nums[i]
        
        arr = []
        count = 0
        while count < len(nums):
            x = 1
            for i in range(len(nums)):
                if i == count:
                    pass
                else:
                    x *= nums[i]
            arr.append(x)
            count += 1
        return arr


