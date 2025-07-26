def minimum_platform(intervals):
    # Convert time strings to minutes for easier comparison
    time_points = []
    for time in intervals:
        start = convert_to_minutes(time[1])
        end = convert_to_minutes(time[2])
        time_points.append((start, 'start'))
        time_points.append((end, 'end'))
    print(time_points)
    
    # Sort all time points (if times are equal, 'end' comes before 'start')
    time_points.sort(key=lambda x: (x[0], x[1] == 'start'))
    print("--------------")
    print("Sorted Time Points : ",time_points)
    max_resources = 0
    current_resources = 0
    
    for time, typ in time_points:
        if typ == 'start':
            current_resources += 1
            if current_resources > max_resources:
                max_resources = current_resources
        else:
            current_resources -= 1
    
    return max_resources

def convert_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes


l=[(1,'09:00','09:10'),(2,'09:40','12:00'),(3,'09:50','11:20'),(4,'11:00','11:30'),(5,'11:40','12:10'),(6,'12:05','19:00'),(7,'12:06','13:00'),(8,'13:05','14:00'),(9,'14:05','15:00'),(10,'18:00','20:00')]
minimum_platform(l)