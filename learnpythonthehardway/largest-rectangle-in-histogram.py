# Time:  O(n)
# Space: O(n)
#
# Given n non-negative integers representing the histogram's bar
# height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.
#
# For example,
# Given height = [2,1,5,6,2,3],
# return 10.
#

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        stack, area, i = [], 0, 0

        while i < len(height):
            if not stack or height[i] > stack[-1]:
                stack.append(i)
                i += 1
            else:
                last = stack.pop()
                if not stack:
                    area = max(area, height[last] * i)
                else:
                    area = max(area, height[last] * (i - stack[-1] - 1))
        return area


if __name__ == "__main__":
    print Solution().largestRectangleArea([2, 0, 2])
    print Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
    print Solution().largestRectangleArea([2, 3, 4, 5, 6, 7])
