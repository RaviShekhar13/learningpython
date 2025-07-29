def MoM7Pos(arr):
    return median_of_medians(arr,0,len(arr)-1,len(arr)//2)
    
def median_of_medians(arr, left, right, k):
    """
    Finds the index of the k-th smallest element in arr[left..right] using MoM.
    :param arr: The input array.
    :param left: Starting index of the subarray.
    :param right: Ending index of the subarray.
    :param k: Desired rank (0-based).
    :return: Index of the k-th smallest element.
    """
    if left == right:
        return left

    # Step 1: Divide into groups of 5 and find their medians
    groups = [arr[i:i+7] for i in range(left, right+1, 7)]
    medians = [sorted(group)[len(group)//2] for group in groups]

    # Step 2: Find the median of medians (pivot)
    median_of_medians_val = median_of_medians(
        medians, 0, len(medians)-1, len(medians)//2
    )
    pivot = medians[median_of_medians_val]

    # Step 3: Partition the array around the pivot
    pivot_idx = partition(arr, left, right, pivot)

    # Step 4: Recurse into the correct subarray
    if k == pivot_idx:
        return pivot_idx
    elif k < pivot_idx:
        return median_of_medians(arr, left, pivot_idx-1, k)
    else:
        return median_of_medians(arr, pivot_idx+1, right, k)

def partition(arr, left, right, pivot):
    """
    Partitions arr[left..right] around the pivot and returns its final index.
    """
    # Find the pivot's index
    pivot_idx = arr.index(pivot, left, right+1)
    # Move pivot to the end
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]

    # Standard partition (like in QuickSort)
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Move pivot to its correct place
    arr[i], arr[right] = arr[right], arr[i]
    return i

def find_median_index(arr):
    """
    Finds the index of the median in O(n) time.
    """
    n = len(arr)
    return median_of_medians(arr, 0, n-1, n//2)
