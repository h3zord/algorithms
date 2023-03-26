def study_schedule(permanence_period, target_time):
    if (not target_time):
        return None

    time_list = []
    for time1, time2 in permanence_period:
        if (not str(time1) or not str(time2) or type(time1) != int or type(time2) != int):
            return None
        
        time_list.extend(list(range(time1, time2 + 1)))

    return time_list.count(target_time)

