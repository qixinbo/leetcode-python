class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        to_str = [str(i) for i in digits]
        plus_one = int(''.join(to_str)) + 1
        return [int(j) for j in list(str(plus_one))]
