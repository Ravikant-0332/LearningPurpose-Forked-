def find_subarrays_with_max_sum_k(nums, k):
    """
    Finds all subarrays within a given list that have a sum equal to k, using a stack-based approach.

    Args:
        nums: A list of integers.
        k: The target sum.

    Returns:
        A list of lists, where each inner list represents a subarray with sum k.
    """
    result = []
    # Stack to store tuples of (start_index, current_sum)
    stack = []

    for i, num in enumerate(nums):
        # Start a new potential subarray from this index
        stack.append((i, num))

        # Check if the single element equals k
        if num == k:
            result.append([num])

        # Update all existing potential subarrays by adding the current element
        for j in range(len(stack) - 2, -1, -1):
            start_index, current_sum = stack[j]
            current_sum += num
            stack[j] = (start_index, current_sum)

            # If the subarray sum equals k, add it to the result
            if current_sum == k:
                result.append(nums[start_index:i + 1])

    return result
