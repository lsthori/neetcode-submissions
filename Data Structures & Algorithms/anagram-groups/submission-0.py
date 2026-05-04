class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = []
        visited = set()

        for x in range(len(strs)):
            if x in visited:
                continue
                
            group = []
            for y in range(len(strs)):
                if sorted(strs[x]) == sorted(strs[y]):
                    group.append(strs[y])
                    visited.add(y)
            output.append(group)

        return output


                                                                    


        