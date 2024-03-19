from datetime import datetime

def parse_timestamp(timestamp):
    # Split the timestamp string
    day, day_num, month, year, time, tz = timestamp.split()
    
    # Create a dictionary to map month names to their numerical representation
    months = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
        'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
        'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }
    
    # Parse the timestamp components
    dt = datetime(int(year), months[month], int(day_num),
                  *map(int, time.split(':')))
    
    # Handle the timezone
    sign = -1 if tz[0] == '-' else 1
    tz_offset = int(tz[1:]) // 100 * 60 + int(tz[1:]) % 100
    dt += sign * timedelta(minutes=tz_offset)
    
    return dt

def time_delta(t1, t2):
    # Parse the timestamps
    dt1, dt2 = parse_timestamp(t1), parse_timestamp(t2)
    
    # Calculate the time difference in seconds
    diff_seconds = abs((dt1 - dt2).total_seconds())
    
    return str(int(diff_seconds))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
