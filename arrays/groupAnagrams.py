from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in dic:
                dic[sorted_str].append(str)
            else:
                dic[sorted_str] = [str]
        return dic.values()