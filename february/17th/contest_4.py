import bisect

def activityNotifications(expenditure, d):
    # Write your code here
    prev_days = []
    notif = 0

    for i in range(d):
        exp = expenditure[i]
        bisect.insort(prev_days, exp)

    for i in range(d, len(expenditure)):
        exp = expenditure[i]
        median = prev_days[d // 2] if d % 2 == 1 else (prev_days[d // 2] + prev_days[(d - 1) // 2]) / 2
        if exp >= median * 2:
            notif += 1
        bisect.insort(prev_days, exp)
        del prev_days[bisect.bisect_left(prev_days, expenditure[i - d])]

    return notif
