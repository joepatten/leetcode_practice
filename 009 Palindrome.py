class Solution:
    """
    >>> s = Solution()

    >>> x = 121
    >>> s.isPalindrome(x)
    True
    >>> x = -121
    >>> s.isPalindrome(x)
    False
    >>> x = 10
    >>> s.isPalindrome(x)
    False
    """
    def isPalindrome(self, x):
        str_num = str(x)
        return str_num == str_num[::-1]

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())