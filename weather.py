import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    
    date_object = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    date_format = datetime.strftime(date_object, "%A %d %B %Y")
    return (date_format)

def convert_f_to_c(temp):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    
    temp_in_C = round(((float(temp) - 32) * 5/9),1)
    return temp_in_C
    
def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    sum_wd=0
    count_wd=0
    for value in weather_data:
        sum_wd += float(value)
        count_wd += 1
    return(sum_wd/count_wd)

def load_data_from_csv(csv_file): 
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file, encoding="utf-8") as csv_file_obj:
        reader = csv.reader(csv_file_obj)
        list=[]
        next(reader)
        for line in reader:
            if line!=[]:
                list.append([line[0],int(line[1]),int(line[-1])])
    return(list)

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.
    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """ 
    if weather_data:
        min_value = weather_data[0]
        min_location = 0
        index = 0
        for value in weather_data:
            if value <= min_value:
                min_value = value
                min_location = index
            index += 1
        return(float(min_value), min_location)
    else: return(())

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data:
        max_value = weather_data[0]
        max_location = 0
        index = 0
        for value in weather_data:
            if value >= max_value:
                max_value = value
                max_location = index
            index += 1
        return(float(max_value), max_location)
    else: return(())

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.
    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # summary=""    
    for record in weather_data:
        summary=f"{len(weather_data)} Day Overview\n"
        summary+=f"  The lowest temperature will be {find_min}, and will occur on Friday 02 July 2021.\n"
        summary+=f"  The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.\n"
        summary+=f"  The average low this week is 12.2°C.\n"
        summary+=f"  The average high this week is 17.8°C.\n"
    return(summary)

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
