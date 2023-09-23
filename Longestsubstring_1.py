class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        start = 0
        char_set = set() 
        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(s[end])
            max_length = max(max_length, end - start + 1)
        return max_length
solution = Solution()
s = "abcabcbb"
result = solution.lengthOfLongestSubstring(s)
print(result)