class Solution:
    def myAtoi(self, str: str) -> int:
        result=""
        str=str.strip()
        for i in str:
            if i in ["-","+"] and result=="":
                result+=i
            elif i.isdigit():
                result+=i
            else:
                break
        if result=="" or result=="+" or result=="-" :
            return 0
        elif int(result) <-2147483648:
            return -2147483648
        elif int(result)>(2**31)-1:
            return (2**31)-1
        else:
            return int(result)

             
