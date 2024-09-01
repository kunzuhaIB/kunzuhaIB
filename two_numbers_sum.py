class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        Approaches:

        Iteration 1:

            - Maintain a list of indexes of numbers which add up to target.
            - Iterate each element in nums with all others.
        
        Input: nums = [2,7,11,15], target = 9

        Iteration 2:
            - create a copy of nums.
            - Maintain a list of indexes of numbers which add up to target.
            - Iterate each element in nums with all others.
        """
        index_list = []

        # Iteration 1
        for ind1,x in enumerate(nums):
            for ind2,y in enumerate(nums):
                if ind1 != ind2 and x+y == target and ind1 not in index_list:
                    index_list.append(ind1)
                    index_list.append(ind2)

        return index_list
