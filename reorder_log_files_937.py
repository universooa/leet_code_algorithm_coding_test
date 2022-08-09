from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_arr=[]
        digit_arr=[]

        for log in logs:
            spt_log=log.split(" ")
            if spt_log[1].isalpha():
                letter_arr.append(log)
            else:
                digit_arr.append(log)


        letter_arr.sort(key=lambda x:(x.split()[1:],x.split()[0]))


        return letter_arr+digit_arr

#
# if __name__=='__main__':
#     logs = ["dig1 8 1 5 1" ,"let1 art can" ,"dig2 3 6" ,"let2 own kit dig" ,"let3 art zero"]
#
#
#     sol=Solution()
#     print(sol.reorderLogFiles(logs))
#
