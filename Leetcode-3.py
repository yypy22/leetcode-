class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = []
        maxi = 0
        for i in s:
            if i in l:
                l = l[l.index(i)+1:]
            l.append(i)
            maxi = max(maxi, len(l))
        return maxi