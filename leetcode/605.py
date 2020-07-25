#  种花问题
'''
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。
能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。
示例:  输入: flowerbed = [1,0,0,0,1], n = 1       输出: True

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/can-place-flowers
'''


class Solution:
    # 连续三个0则可以种一盆花
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed = [0]+flowerbed
        flowerbed = flowerbed+[0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n = n-1
                flowerbed[i] = 1
        return n <= 0

    # 不改变原数组的解法
    def canPlaceFlowers2(self, flowerbed, n):
        if n == 0:
            return True
        total = 0
        pre = -2
        for i, num in enumerate(flowerbed):
            if num == 1:
                if i - pre > 3:
                    total += (i - pre - 2) >> 1
                    if total >= n:
                        return True
                pre = i
        if len(flowerbed) - pre > 2:
            total += (len(flowerbed) - pre -1) >> 1
            if total >= n:
                return True
        return False

    # 贪心算法
    def canPlaceFlowers3(self, flowerbed, n):
        if n == 0:
            return True
        total = 0
        arr_len = len(flowerbed)
        if arr_len == 0:
            return False
        if arr_len == 1:
            if flowerbed[0] == 1:
                return False
            else:
                return True
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            total += 1
            if total >= n:
                return True
            flowerbed[0] = 1
        for i in range(1, arr_len - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                total += 1
                if total >= n:
                    return True
                flowerbed[i] = 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            total += 1
            if total >= n:
                return True
        return False


a = Solution()
print(a.canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(a.canPlaceFlowers2([1, 0, 0, 0, 1], 1))
print(a.canPlaceFlowers3([1, 0, 0, 0, 1], 2))