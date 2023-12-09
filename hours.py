# Passes the three parameters as the arguments
def time(hours, minutes, period): 
    if period.lower() == "am":
# Makes 12am equal to 0
        if hours == 12:
            hours = 0
    elif period.lower() == "pm":
        if hours != 12:
            hours += 12
    return f"{hours:02d}{minutes:02d}hrs"

print(time(3, 34, "am"))

