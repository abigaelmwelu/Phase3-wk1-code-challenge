def convert_to_24_hour_format(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    
    time_24_hour = f"{hour:02d}{minute:02d}"
    return time_24_hour

# Test cases
print(convert_to_24_hour_format(12, 0, "pm"))  # Output: 1200
print(convert_to_24_hour_format(12, 15, "am"))  # Output: 0015
print(convert_to_24_hour_format(5, 30, "pm"))  # Output: 1730

