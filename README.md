Contains Duplicate_2
Problem
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that:
Approach
Use a HashMap (Dictionary) to store each number and its most recent index.
Traverse the array using enumerate().
For each number:
Check if it already exists in the HashMap.
If it exists, calculate the distance between the current index and the previous index.
If the distance is less than or equal to k, return True.
Update the HashMap with the current index.
If no valid duplicate is found, return False.
Complexity
Time Complexity: O(n)
Space Complexity: O(n)
Key Insight
A HashMap allows us to:
Quickly check if a number has appeared before.
Retrieve its previous index in O(1) time.
This avoids using nested loops and improves the solution from O(n²) to O(n).
Example
Input
Python
nums = [1,2,3,1]
k = 3
Output
Python
True
Explanation
First 1 appears at index 0
Second 1 appears at index 3
Distance = 3 - 0 = 3
Since 3 <= k, return True
Code
Python
def containsNearbyDuplicate(nums, k):
    hashmap = {}

    for i, num in enumerate(nums):
        if num in hashmap:
            if i - hashmap[num] <= k:
                return True

        hashmap[num] = i

    return False
print(containsNearbyDuplicate(nums, k))
Output
True
