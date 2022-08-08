import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        conv_str = ""
        for ch in s:
            if 'a' <= ch <= 'z' or '0' <= ch <= '9':  # alpha_numeric
                conv_str += ch

        return conv_str == conv_str[::-1]

#
# sol=Solution()
# s=" "
# print(sol.isPalindrome(s))

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         s=re.sub('^[a-z0-9]','',s)
#         return s== s[::-1]
