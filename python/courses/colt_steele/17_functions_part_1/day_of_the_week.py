def return_day(num_in):
    day_dict = {
        1 : "Sunday",
        2 : "Monday",
        3 : "Tuesday",
        4 : "Wednesday",
        5 : "Thursday",
        6 : "Friday",
        7 : "Saturday"
    }
    try:
        return day_dict.get(num_in)
    except:
        return None

print(return_day(1))
print(return_day(2))
print(return_day(9))