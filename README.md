Contains Duplicate_2.py

Problem

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that:



Approach

Use a HashMap (Dictionary) to store each number and its most recent index.

Traverse the array using enumerate().

For each element:

- Check if the number already exists in the HashMap.
- If it exists, calculate the distance between the current index and the previous index.
- If the distance is less than or equal to k, return True.
- Otherwise, update the HashMap with the current index.

If no valid duplicate is found, return False.

Complexity

Time Complexity: O(n)

Space Complexity: O(n)

Key Insight

A HashMap allows fast lookup of previously seen numbers and their indices.

Instead of comparing every pair of elements using nested loops (O(n²)), we store the latest index of each number and check the distance in O(1) time.

Example

Input:
nums = [1,2,3,1]
k = 3

Output:
True

Explanation:
The number 1 appears at indices 0 and 3.

Distance = 3 - 0 = 3

Since 3 <= k, the answer is True.

Input:
nums = [1,2,3,4,1]
k = 3

Output:
False

Explanation:
The number 1 appears at indices 0 and 4.

Distance = 4 - 0 = 4

Since 4 > k, the answer is False.

Code

def containsNearbyDuplicate(nums, k):
    hashmap = {}

    for i, num in enumerate(nums):
        if num in hashmap:
            if i - hashmap[num] <= k:
                return True

        hashmap[num] = i

    return False

nums = [1,2,3,1]
k = 3

print(containsNearbyDuplicate(nums, k))

