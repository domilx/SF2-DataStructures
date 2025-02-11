n, m, d = map(int, input("Enter n, m, d: ").split())

event_list = set(map(int, input("Event list: ").split()))

laundry_days = 0
dirty_shirts = 0

for day in range(1, d + 1):
    # If Ian has no clean shirts, he does laundry
    if n == 0:
        laundry_days += 1
        n = dirty_shirts
        dirty_shirts = 0
    
    # Ian wears a clean shirt
    n -= 1
    dirty_shirts += 1
    
    # If there's an event today, Ian gets a new clean shirt
    if day in event_list:
        n += 1

print(laundry_days)