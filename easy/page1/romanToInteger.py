class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        value = 0
        i = 1
        n = len(s)
        s += " "
        while(i<=n):
            s1 = s[i-1]
            s2 = s[i] 
            value +=  romanDict[s1]
            if s2 in ['V', 'X']:
                if s1 == 'I':
                  value += romanDict[s2] - romanDict[s1] - 1
                  i += 2
                  continue
            elif s2 in ['L', 'C']:
                if s1 == 'X':
                    value += romanDict[s2] - romanDict[s1]- 10
                    i += 2
                    continue
            elif s2 in ['D', 'M']:
                if s1 == 'C':
                    value += romanDict[s2] - romanDict[s1] - 100
                    i += 2
                    continue
            i += 1
        return value

test = Solution()
print(test.romanToInt("MCMXCIV"))