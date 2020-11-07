class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign=-1 if((dividend<0)^(divisor<0)) else 1
        if dividend>(2**31)-1 or dividend< (-2**31):
            return (2**31)-1
        dividend=abs(dividend)
        divisor=abs(divisor)
        quotient=0
        temp=0
        for i in range(31, -1, -1):
            if (temp + (divisor << i) <= dividend):
                temp += divisor << i;
                quotient |= 1 << i;
        if sign * quotient>(2**31)-1:
            return (2**31)-1
        return sign * quotient;
        
