class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        start = 0
        end = len(rotateArray)-1
        if rotateArray[start] < rotateArray[end]:
            return rotateArray[start]
        while start != (end-1):
            mid = (start + end) // 2
            if rotateArray[mid] <= rotateArray[end]:
                end = mid
            if rotateArray[mid] >= rotateArray[start]:
                start = mid
        return rotateArray[end]