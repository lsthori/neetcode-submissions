class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num = {}

        for n in range(len(nums)):
            diff = target - nums[n]
            if diff in num:
                return [num[diff], n]
            num[nums[n]] = n
                
        