from json import loads
from sys import stdin
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [n for h, n in sorted(zip(heights, names), reverse=True)]


with open('user.out', 'w') as f: 
    iterator = map(loads, stdin)
    s = Solution()
    while True:
        try:
            print(str(s.sortPeople(next(iterator), next(iterator))).replace('\'', '"').replace(', ', ','), file=f)
        except StopIteration:
            exit()