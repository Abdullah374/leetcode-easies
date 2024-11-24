from typing  import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
            # answer = []
            # list1 = []
            
            # for number in nums1:
            #     if number not in nums2 and number not in list1:
            #         list1.append(number)
            # answer.append(list1)
            # list1 = []
            # for number in nums2:
            #     if number not in nums1 and number not in list1:
            #         list1.append(number)
            # answer.append(list1)
            # return answer
            set1 = set(nums1)
            set2 = set(nums2)

            list1 = list(set1-set2)
            list2 = list(set2-set1)

            return [list1,list2]