class Solution:
    def reverse(self, x: int) -> int:
        if x>(2**31):
            return 0
        self.num=x
        temp=0
        x=abs(x)
        while(x>0):
            temp=temp*10
            temp+=x%10
            x=x//10
        if self.num<0:
            temp=-temp
        if (temp >((2**31)-1)) or (temp < -(2**31)):
            return 0
        return temp
