def MoM7Pos(arr):
    if not arr:
        return -1
    
    # Create a list that remembers original indices
    indexed_arr = [(val, i) for i, val in enumerate(arr)]
    n = len(indexed_arr)
    
    def select(l, r, k):
        """Select k-th smallest element in indexed_arr[l..r] and return its original index"""
        while True:
            if l == r:
                return indexed_arr[l][1]
            
            # Choose pivot using median of medians
            pivot_idx = pivot(l, r)
            pivot_idx = partition(l, r, pivot_idx)
            
            if k == pivot_idx:
                return indexed_arr[k][1]
            elif k < pivot_idx:
                r = pivot_idx - 1
            else:
                l = pivot_idx + 1
    
    def pivot(l, r):
        """Select pivot using median of medians of 7"""
        if r - l < 7:
            # For small groups, sort and return median
            sub = sorted(indexed_arr[l:r+1], key=lambda x: x[0])
            median_pos = l + (r - l) // 2
            # Update the subarray with sorted values
            for i in range(l, r+1):
                indexed_arr[i] = sub[i-l]
            return median_pos
        
        # Move medians to front
        for i in range(l, r+1, 7):
            sub_r = min(i + 6, r)
            sub = indexed_arr[i:sub_r+1]
            sub.sort(key=lambda x: x[0])
            median_pos = i + (sub_r - i) // 2
            # Put median at position l + (i-l)//7
            swap_pos = l + (i - l) // 7
            indexed_arr[swap_pos], indexed_arr[median_pos] = indexed_arr[median_pos], indexed_arr[swap_pos]
        
        # Compute median of medians
        median_count = (r - l) // 7 + 1
        return select(l, l + median_count - 1, l + median_count // 2)
    
    def partition(l, r, pivot_idx):
        """Partition around pivot"""
        pivot_val = indexed_arr[pivot_idx][0]
        indexed_arr[pivot_idx], indexed_arr[r] = indexed_arr[r], indexed_arr[pivot_idx]
        
        store_idx = l
        for i in range(l, r):
            if indexed_arr[i][0] < pivot_val:
                indexed_arr[store_idx], indexed_arr[i] = indexed_arr[i], indexed_arr[store_idx]
                store_idx += 1
        
        # Move pivot to final position
        indexed_arr[r], indexed_arr[store_idx] = indexed_arr[store_idx], indexed_arr[r]
        return store_idx
    
    # Find the median's original position
    k = n // 2  # median position
    return select(0, n-1, k)