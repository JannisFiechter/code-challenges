class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num1 in range(0,len(nums)):
            for num2 in range(len(nums)):
                if num1 != num2:
                    if nums[num1] + nums[num2] == target:
                        list = [num1, num2]
                        return list