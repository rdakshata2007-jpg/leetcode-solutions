class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0

        while x > 0:
            m = x % 10
            rev = rev * 10 + m
            x = x // 10

        return temp == rev