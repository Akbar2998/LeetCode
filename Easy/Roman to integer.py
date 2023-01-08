class Solution:
    def romanToInt(self, s: str) -> int:
        son = 0
        rn = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        x = 0
        for i in range(1,len(s)+1):
            if int(rn.get(s[-1*i])) >= x:
                son += rn.get(s[-1*i])
                x = rn.get(s[-1*i])
            else:
                son -= rn.get(s[-1*i])
                x = rn.get(s[-1*i])
        return son  
