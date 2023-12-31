def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def longestPalindrome(s):
    if len(s) < 2:
        return s
    longest = ""
    for i in range(len(s)):
        #odd-length
        palindrome1 = expand_around_center(s, i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1
        #even-length
        palindrome2 = expand_around_center(s, i, i + 1)
        if len(palindrome2) > len(longest):
            longest = palindrome2
    return longest
s1 = "babad"
result1 = longestPalindrome(s1)
print(result1)

s2 = "cbbd"
result2 = longestPalindrome(s2)
print(result2) 
