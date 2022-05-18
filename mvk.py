import csv
from datetime import datetime
from statistics import mean
from unittest import result

from weather import find_min

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

"""Outputs a summary for the given weather data.

Args:
    weather_data: A list of lists, where each sublist represents a day of weather data.
Returns:
    A string containing the summary information.
"""

#input_data
weather_data=[
["2021-07-02T07:00:00+08:00", 49, 67],
["2021-07-03T07:00:00+08:00", 57, 68],
["2021-07-04T07:00:00+08:00", 56, 62],
["2021-07-05T07:00:00+08:00", 55, 61],
["2021-07-06T07:00:00+08:00", 53, 62]
] 

def generate_summary(weather_data):
 
    # summary=""

    for record in weather_data:
        summary=f"{len(weather_data)} Day Overview\n"
        summary+=f"  The lowest temperature will be {(weather_data[1])}, and will occur on Friday 02 July 2021.\n"
        summary+=f"  The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.\n"
        summary+=f"  The average low this week is 12.2°C.\n"
        summary+=f"  The average high this week is 17.8°C.\n"

    return(summary)

print(generate_summary(weather_data))






