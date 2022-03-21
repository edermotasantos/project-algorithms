def study_schedule(permanence_period, target_time):
    count = 0
    if(target_time is None):
        return None
    for element in permanence_period:
        if (
            type(element[0]) != int or
            type(element[1]) != int
        ):
            return None
        if element[0] <= target_time <= element[1]:
            count = count + 1
    return count
