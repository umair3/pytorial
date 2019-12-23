class Solution:

    def reverse_string(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


a = Solution()
print(a.reverse_string("hello"))

