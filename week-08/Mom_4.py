def MoM7Pos(arr):
    return median_of_medians(arr,0,len(arr)-1,len(arr)//2,7)
    
def median_of_medians(arr, left, right, k, group_size=7):
    """Finds the k-th smallest element's index in the partitioned array"""
    if left == right:
        return left

    groups = [arr[i:i+group_size] for i in range(left, right+1, group_size)]
    medians = [sorted(group)[len(group)//2] for group in groups]
    
    mom_val = median_of_medians(medians, 0, len(medians)-1, len(medians)//2, group_size)
    pivot = medians[mom_val]

    pivot_idx = partition(arr, left, right, pivot)

    if k == pivot_idx:
        return pivot_idx
    elif k < pivot_idx:
        return median_of_medians(arr, left, pivot_idx-1, k, group_size)
    else:
        return median_of_medians(arr, pivot_idx+1, right, k, group_size)

def partition(arr, left, right, pivot):
    """Partitions array around pivot and returns its final index"""
    pivot_idx = next((i for i in range(left, right+1) if arr[i] == pivot), right)
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    
    store_idx = left
    for i in range(left, right):
        if arr[i] <= pivot:
            arr[store_idx], arr[i] = arr[i], arr[store_idx]
            store_idx += 1
    
    arr[store_idx], arr[right] = arr[right], arr[store_idx]
    return store_idx

def find_median_positions(arr, group_size=7):
    """Finds all positions of the median value in original array"""
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    # Find the median value
    median_idx = median_of_medians(arr_copy, 0, n-1, n//2, group_size)
    median_val = arr_copy[median_idx]
    
    # Get all positions of median value in original array
    positions = [i for i, x in enumerate(arr) if x == median_val]
    return positions