class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return len(str(bin(n)).split('1'))-1

    def hammingWeightSolution2(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        while n:
            ans+=n%2
            n /= 2
        return ans

def stringToInt(input):
    return int(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            n = stringToInt(line)
            
            ret = Solution().hammingWeight(n)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
