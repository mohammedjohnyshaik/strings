class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur, till, start = 0, 0, 0
        N = len(s)
        i = 0
        charset = {}
        while i < N:
            if s[i] not in charset:
                cur += 1
            else:
                start = max(start, charset[s[i]] + 1)
                cur = i - start + 1
            charset[s[i]] = i
            till = max(cur, till)
            i += 1
        return till

solution = Solution()
s = "abcabcbb"
result = solution.lengthOfLongestSubstring(s)
print(result)

