# write your code here
def hours(duration):
    hour=3600
    return duration//3600 

def minutes(duration):
    minutes=60
    return duration//60

def seconds(duration):
    duration=60
    return seconds//60

#ans
def hours(duration):
    return duration // 3600

def minutes(duration):
    h = hours(duration)
    remaining_seconds = duration - (h * 3600)
    return remaining_seconds // 60

def seconds(duration):
    h = hours(duration)
    remaining_seconds = duration - (h * 3600)
    m = minutes(remaining_seconds)
    remaining_seconds -= (m * 60)
    return remaining_seconds


