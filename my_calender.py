import calendar


def get_cal_list():
    converter = {0: "Saturday", 1: "Friday", 2: "Thursday", 3: "Wednesday", 4: "Tuesday", 5: "Monday", 6: "Sunday"}

    cal_list = []

    cal = calendar.TextCalendar(calendar.SUNDAY)
    cal_str = cal.formatmonth(2022, 12)

    for line in cal_str.split("\n")[2:-1]:
        counter = 0
        week = {}
        for day in line.split()[::-1]:
            week[converter[counter]] = day
            counter += 1
        cal_list.append(week)

    print(cal_list)
    return cal_list
