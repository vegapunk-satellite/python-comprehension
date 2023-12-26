# Input : 11:21:30 PM
# Output : 23:21:30

# Input : 12:12:20 AM
# Output : 00:12:20

def convert_to_12(input_24):
    parts = input_24.split(":")
    hour = int(parts[0])
    output_hour = None
    am_pm = None
    if hour > 12:
        output_hour = str(hour - 12)
        am_pm = "PM"
    elif hour == 12:
        output_hour = 12
        am_pm = "PM"
    elif hour == 0:
        output_hour = 12
        am_pm = "AM"
    else:
        output_hour = str(hour)
        am_pm = "AM"
    return output_hour + ":" + parts[1] + ":" + parts[2] + " " + am_pm

# input_24 = "14:21:30"
# output_12 = convert_to_12(input_24)
# print(output_12)


def convert_to_24(input_12):
    time_and_am_pm = input_12.split(" ")
    time = time_and_am_pm[0]
    am_pm = time_and_am_pm[1]
    parts = time.split(":")
    hour = int(parts[0])
    output_hour = None
    if am_pm == "AM":
        output_hour = (str(hour) if hour != 12 else "00")
    else:
        output_hour = (str(hour + 12) if hour != 12 else "12")
    return output_hour + ":" + parts[1] + ":" + parts[2]


input_12 = "05:12:20 AM"
output_24 = convert_to_24(input_12)
print(output_24)

# TODO: başına 0 ekleme