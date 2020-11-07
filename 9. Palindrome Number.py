class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.num=x
        temp=0
        while(x>0):
            temp=temp*10

            temp+=x%10
            x=x//10
        if temp==self.num:
            return True
        else:
            return False
        
