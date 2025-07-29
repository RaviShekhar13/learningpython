def MoM7Pos(arr):
    if arr==[]:
        return 0
    def chunk_list(lst, size):
        return [lst[i:i + size] for i in range(0, len(lst), size)]

    def median(lst):
        lst_sorted = sorted(lst)
        mid = len(lst_sorted) // 2
        return lst_sorted[mid]  # Works for both even/odd; returns middle or lower middle

    # Step 1 & 2: Get medians of chunks of 7
    chunks = chunk_list(arr, 7)
    medians = [median(chunk) for chunk in chunks]

    # Step 3: Median of medians
    M = median(medians)

    # Step 4: Sort original array
    sorted_arr = sorted(arr)

    # Step 5: Return first index of M in sorted array
    for i, val in enumerate(sorted_arr):
        if val == M:
            return i

    return 0  # fallback (shouldn't happen unless M is missing)


arr=[44,9,31,12,15,98,48,45,13,75,23,6,35,74]
arr=[2,-1,0,-2,3,2,4,2]
position = MoM7Pos(arr)
print(position)