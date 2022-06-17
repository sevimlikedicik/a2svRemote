def solution():
    n = input()
    days = [int(num) for num in input().split(' ')]
    rest_days = 0
    contest_yesterday = False
    gym_yesterday = False
    for day in days:
        if day == 3:
            if contest_yesterday:
                gym_yesterday = True
                contest_yesterday = False
            elif gym_yesterday:
                gym_yesterday = False
                contest_yesterday = True
        if day == 1:
            if contest_yesterday:
                rest_days += 1
                contest_yesterday = False
                gym_yesterday = False
            else:
                contest_yesterday = True
                gym_yesterday = False
        if day == 2:
            if gym_yesterday:
                rest_days += 1
                contest_yesterday = False
                gym_yesterday = False
            else:
                gym_yesterday = True
                contest_yesterday = False
        if day == 0:
            rest_days += 1
            contest_yesterday = False
            gym_yesterday = False
    print(rest_days)


solution()
