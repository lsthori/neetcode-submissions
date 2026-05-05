class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {} # nums: count
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        for v, i in count.items():
            freq[i].append(v)

        output = []
        for x in range(len(freq) - 1, 0, -1):
            for num in freq[x]:
                output.append(num)
                if len(output) == k:
                    return output

            