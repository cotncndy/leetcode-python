class Solution:
    # @param a list of integers
    # @return an integer

    def removeDuplicates(self, A):
        if not A:
            return 0
        last, i = 0, 1
        while i < len(A):
            if A[i] != A[last]:
                last += 1
                A[last] = A[i]

            i += 1

        return last + 1


if __name__ == "__main__":
    print Solution().removeDuplicates([1, 1,1, 2,3,3,4,4,5])
