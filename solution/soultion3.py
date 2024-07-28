from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
        descend = ['']*len(names)
        for i in range(len(names)):
            d[heights[i]] = names[i]
        h = sorted(heights)
        return [d[height] for height in h[::-1]]