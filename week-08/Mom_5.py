def MoM7Pos(arr):
    """
    Computes the median of medians (using blocks of 7) and returns its position
    in the original array as if it were sorted. If the median appears multiple times,
    returns the first occurrence's index in the sorted order.
    """
    if not arr:
        return -1
    
    # Step 1: Divide into groups of 7 and find their medians
    groups = [arr[i:i+7] for i in range(0, len(arr), 7)]
    medians = [sorted(group)[len(group)//2] for group in groups]
    
    # Step 2: Recursively find the median of medians if needed
    if len(medians) <= 7:
        mom = sorted(medians)[len(medians)//2]
    else:
        mom = MoM7Pos(medians)
    
    # Step 3: Partition the array around mom and find its sorted position
    # We need to find where mom would be in the sorted array
    less = [x for x in arr if x < mom]
    equal = [x for x in arr if x == mom]
    
    # The first occurrence in sorted array would be at position len(less)
    first_occurrence_pos = len(less)
    
    # Now find which index in original array corresponds to this position
    # We need to find the first 'mom' in original array that would appear
    # at this position in the sorted array
    
    # Collect all positions of mom in original array
    mom_positions = [i for i, x in enumerate(arr) if x == mom]
    
    # The one that would appear first in sorted order is the one that has
    # exactly 'len(less)' elements before it that are <= mom
    # So we need to find the first mom in original array where:
    # count of elements < mom before it + count of mom's before it == len(less)
    
    count_less = 0
    count_mom = 0
    for i, x in enumerate(arr):
        if x < mom:
            count_less += 1
        elif x == mom:
            if count_less + count_mom == first_occurrence_pos:
                return i
            count_mom += 1
    
    # If not found (shouldn't happen if mom is correct)
    return -1