class Solution(object):
    def trap(self, height):
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0

        while r > l:
            if maxL < maxR:
                l += 1
                maxL = max(height[l], maxL)
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(height[r], maxR)
                res += maxR - height[r]
        return res