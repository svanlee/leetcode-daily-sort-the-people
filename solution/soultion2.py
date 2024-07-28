class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        return [person[0] for person in sorted(zip(names, heights), key=lambda person: -person[1])]