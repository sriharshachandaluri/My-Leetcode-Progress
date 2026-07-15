class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l = len(x)
        for i in range(l//2):
            if x[i] != x[int(l) - i - 1]:
                return False 
                break
        else:
            return True
