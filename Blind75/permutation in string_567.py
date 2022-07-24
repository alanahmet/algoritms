import copy


class Solution(object):
    def checkInclusion(self, s1, s2):
        l = 0
        l_copy = 0
        hashL = {}
        for i in s1:
            if i in hashL:
                hashL[i] += 1
            else:
                hashL[i] = 1
        hash_copy = copy.deepcopy(hashL)
        while l < len(s2):
            if s2[l] in hash_copy:
                con = True
                while hash_copy and con:
                    if s2[l] in hash_copy:
                        print(s2[l:])
                        if hash_copy[s2[l]] > 1:
                            hash_copy[s2[l]] -= 1
                        else:
                            hash_copy.pop(s2[l])
                        l += 1
                    else:
                        con = False
                        l = l_copy
                        break
                    if not hash_copy:
                        return True
            hash_copy = hashL
            l += 1
            l_copy = l
        return False


print(Solution().checkInclusion("hello", "ooolleoooleh"))
