class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not target or not array:
            return False
        row = 0
        col = len(array[0])-1
        while col >= 0 and row < len(array):
            if target == array[row][col]:
                return True
            elif target > array[row][col]:
                row += 1
            elif target < array[row][col]:
                col -= 1
        return False