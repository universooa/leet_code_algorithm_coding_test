import re
from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        str_arr=[]

        paragraph= re.sub(r'[^\w]',' ',paragraph)
        spt_arr=paragraph.split()
        for i in spt_arr:

            i=i.lower()

            if i in banned:
                continue
            str_arr.append(i)

        cnt=Counter(str_arr)

        return cnt.most_common(1)[0][0]

#
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# sol=Solution()
# sol.mostCommonWord(paragraph,banned)