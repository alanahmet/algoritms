class Solution:
    def maxArea(self, height) -> int:
        max_permutation = height[0] * (len(height)-1) if height[0] <= height[len(height )- 1] else height[len(height) - 1] * (len(height)-1)
        first_pointer = 0
        second_pointer = len(height) - 1
        while second_pointer - first_pointer != 1:
            if height[first_pointer] > height[second_pointer]:
                second_pointer-=1
            else:
                first_pointer+=1
            lower_line = height[first_pointer] if height[first_pointer] < height[second_pointer] else height[second_pointer]
            new_area = (second_pointer - first_pointer)*lower_line
            max_permutation = new_area if new_area > max_permutation else max_permutation
        return max_permutation