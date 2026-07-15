class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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


