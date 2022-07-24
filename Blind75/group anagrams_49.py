class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        res = {}
        for i in strs:
            s = str("".join(sorted(i)))
            if s not in res:
                res[s] = [i]
            else:
                res[s].append(i)
        return res.values()



Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])