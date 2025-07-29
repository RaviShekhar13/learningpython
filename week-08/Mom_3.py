def MoM7Pos(arr):
    return median_of_medians(arr,0,len(arr)-1,len(arr)//2,7)
    
def median_of_medians(arr, left, right, k, group_size=7):
    """
    Finds the index of the k-th smallest element using groups of specified size.
    Returns the index in the original array.
    """
    if left == right:
        return left

    # Divide into groups of specified size
    groups = [arr[i:i+group_size] for i in range(left, right+1, group_size)]
    
    # Find medians of each group
    medians = [sorted(group)[len(group)//2] for group in groups]
    
    # Find the median of medians (pivot)
    median_of_medians_val = median_of_medians(
        medians, 0, len(medians)-1, len(medians)//2, group_size
    )
    pivot = medians[median_of_medians_val]

    # Partition the array around the pivot and get its final index
    pivot_idx = partition(arr, left, right, pivot)

    # Recurse into the appropriate subarray
    if k == pivot_idx:
        return pivot_idx
    elif k < pivot_idx:
        return median_of_medians(arr, left, pivot_idx-1, k, group_size)
    else:
        return median_of_medians(arr, pivot_idx+1, right, k, group_size)

def partition(arr, left, right, pivot):
    """
    Partitions the array around the pivot value and returns its final index.
    Preserves original indices by tracking pivot positions.
    """
    # Find all occurrences of pivot
    pivot_indices = [i for i in range(left, right+1) if arr[i] == pivot]
    if not pivot_indices:
        return right  # Fallback if pivot not found (shouldn't happen)
    
    # Use the first occurrence as the pivot
    pivot_idx = pivot_indices[0]
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    
    # Standard partition
    store_idx = left
    for i in range(left, right):
        if arr[i] <= pivot:
            arr[store_idx], arr[i] = arr[i], arr[store_idx]
            store_idx += 1
    
    # Move pivot to its final place
    arr[store_idx], arr[right] = arr[right], arr[store_idx]
    return store_idx

def find_median_position(arr, group_size=7):
    """
    Finds the position of the median in the original array.
    """
    if not arr:
        return -1
    
    # Create a copy to avoid modifying original
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    # Find the index of the median
    median_idx = median_of_medians(arr_copy, 0, n-1, n//2, group_size)
    
    # Find all positions of this median value in original array
    median_value = arr_copy[median_idx]
    positions = [i for i, x in enumerate(arr) if x == median_value]
    
    # Return the first occurrence (can be modified to return all)
    return positions[0] if positions else -1
