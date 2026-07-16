class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits)-1] = digits[len(digits)-1]+1
        i = len(digits)-1
        while i >= 0 and digits[i] >=  10:
            if i == 0:
                digits.insert(0,digits[i]//10)
                digits[i+1] = digits[i+1]%10
            else:
                digits[i-1] += digits[i]//10
                digits[i] = digits[i]%10
            i -= 1
        return digits