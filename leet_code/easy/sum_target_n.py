class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        
        for count, value in enumerate(nums):
            #find compliment
            compliment = target - value
            
            #if the compliment is present in dic, we already have it in there so
            #return previous index in dic associalted with that value-key and current index
            if compliment in compliments.keys():
                compliement_index = compliments[compliment]
                return [compliement_index, count]
            #if the compliment is not present, add current value in the dictionary with key:value is  value:index
            compliments[value] = count

#Space complexity: O(n)
#Time  complexity: O(n)