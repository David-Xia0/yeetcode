from ast import List


class Solution:


    directions = [[1,0], [-1,0], [0,1], [0,-1]]

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int, start = -1) -> List[List[int]]:
        if sr == len(image) or sc == len(image[0]) or sr == -1 or sc == -1 or image[sr][sc] == color:
            return image
        if start == -1:
            start = image[sr][sc]
        elif image[sr][sc] != start:
            return image
        image[sr][sc] = color
        
        for direction in self.directions:
            self.floodFill(image, sr + direction[0], sc + direction[1], color, start)
        
        return image

        
