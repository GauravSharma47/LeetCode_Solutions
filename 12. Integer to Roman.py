class Solution:
    def intToRoman(self, num: int) -> str:
        d={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        result=""
        while num>0:
            if num>=1000:
                result+=d[1000]
                num-=1000
            elif num>=500:
                result+=d[500]
                num-=500
            elif num>=100:
                result+=d[100]
                num-=100
            elif num>=50:
                result+=d[50]
                num-=50
            elif num>=10:
                result+=d[10]
                num-=10
            elif num>=5:
                result+=d[5]
                num-=5
            elif num>=1:
                result+=d[1]
                num-=1
        amc={"DCCCC":"CM","CCCC":"CD","LXXXX":"XC","XXXX":"XL","VIIII":"IX","IIII":"IV"}
        for i in amc.keys():
            if i in result:
                result=result.replace(i,amc[i])
        return result
