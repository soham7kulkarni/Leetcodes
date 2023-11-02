# Approach - length of first array should be less than second array. We will partition the array and will focus on partitions. If arr = [0,1,2] then partitions are 4 - | 0 | 1 | 2 | 
# -On this small/first array calculate mid and declare it as a partX. Calculate partY using (n1+n2)/2 - partX
# -Logically speaking the left half should have smallest elements from both of the array and right half will have bigger elements. If not, we will adjust the partition accordingly by adjusting low and high on first array. 
# -When total elements are even, median is sum of max element from left half and min element from right half. IF total elements are odd, left half will have 1 element less than right half. median will be just 1 place right of partX
# TC - O(log(m+n)) 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0 and len(nums2) == 0: return 0
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2 : return self.findMedianSortedArrays(nums2, nums1)
        low = 0
        high = n1
        while low <= high:
            partX = low + (high-low)//2
            partY = (n1+n2)//2 - partX
            L1 = float('-inf') if partX == 0 else nums1[partX-1]
            L2 = float('-inf') if partY == 0 else nums2[partY-1]
            R1 = float('+inf') if partX == n1 else nums1[partX]
            R2 = float('+inf') if partY == n2 else nums2[partY]
            if L1 <= R2 and L2 <= R1:
                if (n1+n2)%2 == 0: 
                    left = max(L1,L2)
                    right = min(R1,R2)
                    return (left+right)/2
                else:
                    return min(R1,R2)
            elif (L2 > R1):
                low = partX+1
            else:
                high = partX-1

        