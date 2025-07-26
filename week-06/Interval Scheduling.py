def interval_scheduling(intervals):
    intervals.sort(key=lambda x: x[1])
    selected_intervals = []
    last_end_time = -1
    for start, end in intervals:
        if start >= last_end_time:
            selected_intervals.append((start, end))
            last_end_time = end
    return selected_intervals

print(interval_scheduling([(1, 3), (2, 4), (3, 6), (5, 7), (8, 9), (5, 9)]))

# def minimum_platform(intervals):
    
#     intervals.sort(key=lambda x: datetime.strptime(x[2], "%H:%M").time())
#     print(intervals)
#     selected_intervals = []
#     last_end_time = '00:00'
#     for id, start, end in intervals:
#         if datetime.strptime(start, "%H:%M").time() >= datetime.strptime(last_end_time, "%H:%M").time():
#             selected_intervals.append((start, end))
#             last_end_time = end
#     return selected_intervals
    