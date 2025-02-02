"""
Given an integer array num sorted in non-decreasing order.
You can perform the following operation any number of times:
Choose two indices, i and j, where nums[i] < nums[j].
Then, remove the elements at indices i and j from nums. The remaining elements
retain their original order, and the array is re-indexed.
Return the minimum length of nums after applying the operation zero or more times.

Example 1:

Input: nums = [1,2,3,4]

Output: 0

Example 2:

Input: nums = [1,1,2,2,3,3]

Output: 0

Example 3:

Input: nums = [1000000000,1000000000]

Output: 2

Since both numbers are equal, they cannot be removed.

Example 4:

Input: nums = [2,3,4,4,4]

Output: 1

"""
import heapq
from collections import defaultdict
from typing import List


def min_length_after_removals (nums: List [int]) -> int:
    n = len(nums)

    if len(set(nums)) == 1:
        return n
    freq_dict = defaultdict(int)
    i = 0
    while i < len(nums):
        count = nums.count(nums [i])
        freq_dict [nums [i]] = count
        i += count
    # Create a max heap to store the counted values
    max_heap = [-count for count in freq_dict.values()]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        count1, count2 = -heapq.heappop(max_heap), -heapq.heappop(max_heap)

        count1 -= 1
        count2 -= 1
        if count1 > 0:
            heapq.heappush(max_heap, -count1)
        if count2 > 0:
            heapq.heappush(max_heap, -count2)
        n -= 2
    print(n)
    return n

if __name__ == '__main__':
    min_length_after_removals([1,2,3,4])
    min_length_after_removals([1,1,2,2,3,3])
    min_length_after_removals([1000000000,1000000000])
    min_length_after_removals([2,3,4,4,4])