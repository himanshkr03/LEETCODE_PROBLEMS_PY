class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        if x==0:
            return True
        if x%10==0:
            return False
        orgX=x
        numRev=0
        while x>0:
            lasdigit= x%10
            numRev= numRev*10+lasdigit
            x=x//10
        return orgX==numRev
        