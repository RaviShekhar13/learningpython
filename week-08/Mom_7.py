def MoM7Pos(arr):
    if not arr:
        return -1
    
    n = len(arr)
    if n == 1:
        return 0
    
    # Step 1: Divide into groups of 7 and find their medians
    groups = [arr[i:i+7] for i in range(0, n, 7)]
    medians = [sorted(group)[len(group)//2] for group in groups]
    
    # Step 2: Find median of medians recursively
    mom_value = MoM7_value(medians)
    
    # Step 3: Find all positions of mom_value in original array
    positions = [i for i, x in enumerate(arr) if x == mom_value]
    
    # Step 4: Determine which occurrence corresponds to the median position
    less_count = sum(1 for x in arr if x < mom_value)
    
    # The first mom_value that has exactly 'less_count' elements before it
    current_less = 0
    for i, x in enumerate(arr):
        if x < mom_value:
            current_less += 1
        elif x == mom_value:
            if current_less == less_count:
                return i
    
    return positions[0] if positions else -1

def MoM7_value(arr):
    """Helper function to compute just the median of medians value"""
    if not arr:
        return None
    if len(arr) <= 7:
        return sorted(arr)[len(arr)//2]
    
    groups = [arr[i:i+7] for i in range(0, len(arr), 7)]
    medians = [sorted(group)[len(group)//2] for group in groups]
    return MoM7_value(medians)
