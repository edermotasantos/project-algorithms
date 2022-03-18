def study_schedule(permanence_period, target_time):
    count = 0
    previous_count = 0
    for element in permanence_period:
        if (
            target_time == "" or
            type(element[0]) is not int or
            type(element[1]) is not int
            ):
            return None
        if element[0] <= target_time <= element[1]:
            count = count + 1
        if count > previous_count:
            previous_count = count
    return previous_count

