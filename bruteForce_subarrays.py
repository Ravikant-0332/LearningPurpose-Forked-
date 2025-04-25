def find_subarrays_with_max_sum_k(nums, k):
    """
    Finds all subarrays within a given list that have a sum equal to k, using a brute force approach.

    Args:
        nums: A list of integers.
        k: The target sum.

    Returns:
        A list of lists, where each inner list represents a subarray with sum k.
    """
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            current_subarray = nums[i:j+1]
            if sum(current_subarray) == k:
                result.append(current_subarray)
    return result