def MoM7Pos(arr):
    """
    Computes the median of medians (using blocks of 7) and returns its position
    in the original array as if it were sorted. Returns the first occurrence if duplicates exist.
    """
    if not arr:
        return -1

    # Make a copy to avoid modifying original array
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    def select(arr, left, right, k):
        """Select k-th smallest element in arr[left..right]"""
        while True:
            if left == right:
                return left
            
            # Choose pivot using median of medians
            pivot_index = pivot(arr, left, right)
            pivot_index = partition(arr, left, right, pivot_index)
            
            if k == pivot_index:
                return k
            elif k < pivot_index:
                right = pivot_index - 1
            else:
                left = pivot_index + 1
    
    def pivot(arr, left, right):
        """Select pivot using median of medians"""
        # For 5 or fewer elements, get median directly
        if right - left < 5:
            return median5(arr, left, right)
        
        # Otherwise move medians to front
        for i in range(left, right + 1, 5):
            sub_right = min(i + 4, right)
            median5_index = median5(arr, i, sub_right)
            
            # Swap median to front
            swap_pos = left + (i - left) // 5
            arr[median5_index], arr[swap_pos] = arr[swap_pos], arr[median5_index]
        
        # Compute median of medians
        median_count = (right - left) // 5 + 1
        return select(arr, left, left + median_count - 1, left + median_count // 2)
    
    def median5(arr, left, right):
        """Get median of <=5 elements using insertion sort"""
        sub = arr[left:right+1]
        sub.sort()
        median_val = sub[len(sub)//2]
        # Find first occurrence of median in original subarray
        for i in range(left, right + 1):
            if arr[i] == median_val:
                return i
        return left
    
    def partition(arr, left, right, pivot_index):
        """Partition around pivot"""
        pivot_val = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot_val:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        
        # Move pivot to final position
        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index
    
    # Find the median index in the copy
    median_pos_in_copy = select(arr_copy, 0, n - 1, n // 2)
    median_val = arr_copy[median_pos_in_copy]
    
    # Now find first occurrence of this value in original array
    # that would appear at median position in sorted array
    less_count = sum(1 for x in arr if x < median_val)
    equal_count = 0
    
    for i, x in enumerate(arr):
        if x == median_val:
            if equal_count == 0 and less_count == 0:
                return i
            if x < median_val:
                less_count -= 1
            elif x == median_val:
                equal_count += 1
    
    # Fallback: find first occurrence in original array
    for i, x in enumerate(arr):
        if x == median_val:
            return i
    
    return -1