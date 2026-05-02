class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        numbers = set()

        for x in nums:
            if x in numbers:
                return True
            numbers.add(x)
        return False
        