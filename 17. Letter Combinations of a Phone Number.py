from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits.strip()=="":
            return list()
        letters={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        l=[letters[i] for i in digits]
        l=[''.join(i) for i in product(*l)]
        return l

        
