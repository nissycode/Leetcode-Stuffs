class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Convert the list of digits into a string, join them, and cast the result to an integer.
        plusone = int("".join([str(d) for d in digits])) + 1

        # Convert the incremented number back into a list of digits and return it.
        return [int(d) for d in str(plusone)]
