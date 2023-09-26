def is_palindrome(s):
    return s == s[::-1]
def longestPalindrome(s):
    if len(s) < 2:
        return s
    longest = s[0]
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring
    return longest
s1 = "babad"
result1 = longestPalindrome(s1)
print(result1)  # Output: "bab" or "aba"
s2 = "cbbd"
result2 = longestPalindrome(s2)
print(result2)  # Output: "bb"