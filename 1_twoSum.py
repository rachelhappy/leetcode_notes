class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i    #dic后面是[]  遍历nums，创建哈希表
            for j in range(len(nums)):    #从第一个元素开始，寻找符合条件的value和key，此行寻找value1
                diff = target - nums[j]   #此行寻找key2
                if (diff in dic and dic[diff] != j):  # 因为value具有唯一性，所以要key1的value1≠key2的value2，且key2存在         外面的大括号不要忘了加  
                  result.append(j)
                  result.append(dic[diff])
                  return result



        # result = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         sum = nums[i] + nums[j]
        #         if sum == target:
        #             result = [i,j]
        #             return result
#两个for，双指针，右指针永远在左指针的右边，再遍历，俗称暴力破解
