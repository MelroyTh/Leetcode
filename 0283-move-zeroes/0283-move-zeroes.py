class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        res=[]
        for num in nums:
            if num!=0:
                 res.append(num)
        diff=len(nums)-len(res)
        for i in range(diff):
              res.append(0)
        for i in range(len(nums)):
            nums[i] = res[i]
        