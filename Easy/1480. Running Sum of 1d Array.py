class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:

        b = []

        b.append(nums[0])

        for i in range(1,len(nums)):

            xc = 0

            for j in range(i):

                xc += nums[j]

            b.append(nums[i] + xc)

        return b
