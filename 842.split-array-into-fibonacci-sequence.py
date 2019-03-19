class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res=[]
        if self.checkFibonacci(S,res,0):
            return res
        return []
    
    
    def checkFibonacci(self,S,result,index):
        
        if index==len(S) and len(result)>=3:
            return True
        
        for i in range(index,len(S)):
            if S[index] == "0" and i > index:
                break
            num = int(S[index:i + 1])
            if num > 2147483647:
                break
            if len(result)<2:
                result.append(num)
                if self.checkFibonacci(S,result,i+1):
                    return True
                continue
            if result[-2]+result[-1]==num:
                result.append(num)
                if self.checkFibonacci(S,result,i+1):
                    return True
                continue
        if len(result)>0:
            result.pop()
        return False
        pass

def stringToString(input):
    return input[1:-1].decode('string_escape')

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            S = stringToString(line)
            
            ret = Solution().splitIntoFibonacci(S)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
