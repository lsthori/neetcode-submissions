class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        the_hold = set()
        for n in nums:
            if n in the_hold:
                return True
            the_hold.add(n)
        return False
                            