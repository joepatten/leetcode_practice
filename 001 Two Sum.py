class Solution:
    """
    >>> s = Solution()

    >>> nums = [2,7,11,15]
    >>> target = 9
    >>> s.twoSum(nums, target)
    [0, 1]
    >>> nums = [3,2,4]
    >>> target = 6
    >>> s.twoSum(nums, target)
    [1, 2]
    >>> nums = [3,3]
    >>> target = 6
    >>> s.twoSum(nums, target)
    [0, 1]
    """
    def twoSum(self, nums, target):
        seen = {}
        for i, e in enumerate(nums):
            if e in seen.keys():
                return [seen[e], i]
            else:
                seen[target-e] = i

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())