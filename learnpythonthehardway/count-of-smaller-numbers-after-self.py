# Time:  O(nlogn)
# Space: O(n)

# You are given an integer array nums and you have to
# return a new counts array. The counts array has the
# property where counts[i] is the number of smaller
# elements to the right of nums[i].
#
# Example:
#
# Given nums = [5, 2, 6, 1]
#
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# Return the array [2, 1, 1, 0].

# Divide and Conquer solution.
# todo merge sort
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def count_and_mergesort(num_idxs, start, end, counts):
            if end - start <= 0:
                return 0

            mid = start + (end - start) / 2;
            count_and_mergesort(num_idxs, start, mid, counts)
            count_and_mergesort(num_idxs, mid + 1, end, counts)
            r, temp = mid + 1, []
            for i in xrange(start, mid + 1):
                # merge 2 sorted array into temp
                while r <= end and num_idxs[r][0] < num_idxs[i][0]:
                    temp.append(num_idxs[r])
                    r += 1
                temp.append(num_idxs[i])  # dont' forget this
                counts[num_idxs[i][1]] += r - (mid + 1)

            # copy temp back to num_idxz
            num_idxs[start:start + len(temp)] = temp

        num_idx = []
        counts = [0] * len(nums)
        for i, n in enumerate(nums):
            num_idx.append((n, i))

        count_and_mergesort(num_idx, 0, len(nums) - 1, counts)

        return counts

    # todo using BIT to do it
    def countSmaller(self, nums):
        pass


if __name__ == '__main__':
    print Solution().countSmaller([5, 2, 6, 1])
