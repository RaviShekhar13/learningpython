def countIntersection(A, B):
    """
    Count the number of intersecting pairs (inversions) between two lists of points.
    Uses a modified Merge Sort for O(n log n) time.
    """
    # Pair each element of A with the corresponding element in B
    pairs = list(zip(A, B))
    
    # Sort the pairs based on A's values (since A is already sorted, this step is redundant here)
    pairs.sort()
    
    # Extract B's values in the order sorted by A
    B_sorted_by_A = [b for a, b in pairs]
    
    # Count inversions in B_sorted_by_A using modified Merge Sort
    def merge_sort_and_count(arr):
        if len(arr) <= 1:
            return arr, 0
        
        mid = len(arr) // 2
        left, inv_left = merge_sort_and_count(arr[:mid])
        right, inv_right = merge_sort_and_count(arr[mid:])
        merged, inv_merge = merge_and_count(left, right)
        
        total_inversions = inv_left + inv_right + inv_merge
        return merged, total_inversions
    
    def merge_and_count(left, right):
        merged = []
        inversions = 0
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inversions += len(left) - i  # All remaining left elements > right[j]
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inversions
    
    _, total_inversions = merge_sort_and_count(B_sorted_by_A)
    return total_inversions