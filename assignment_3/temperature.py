"""
1. (time estimate: 5 minutes) Write a function called toCelsius that takes a temperature in
Fahrenheit and returns the corresponding temperature in Celsius rounded to 2 decimal places.
Here is the formula that you can use: C = (F - 32)*(5/9).
For example:
If the temperature in Fahrenheit is 77, then your function returns 25.0.
"""
def toCelsius(temperature):
    celsius = (float(temperature) - 32) * (5/9)
    return round(celsius, 2)
"""
3. (time estimate: 10 minutes) Write a function called avgTempYear that takes two arguments: a
dictionary (of same format as you read from the data.txt file) and year. The function returns
the average temperature for the given year in the dictionary rounded to 2 decimal places. If the
provided year is not in the dictionary, your code should use exceptions to handle it as we have
done in class by using the try-except-else block as needed. In the case of invalid year,
you should print a friendly message and your function in such a case should return nothing.
"""
def avgTempYear(d: dict, year: int):
    try:
        return(round(sum(d[year])/len(d[year]), 2))
    except KeyError:
        print("idiot, not a year")
"""
4. (time estimate: 10 minutes) Write a function topThreeYears that takes a dictionary (of
same format as you read from the data.txt file) and returns a list of the three largest averages
in descending order among all the years. Pay attention to what data structures you may use for
efficiency.
"""
def topThreeYears(d: dict):
    sorted = []
    lst = []
    for year in d:
        lst.append(avgTempYear(d, year))

    for _ in range(3):
        data = lst.pop(lst.index(max(lst)))
        sorted.append(data)
    return sorted
"""
5. (time estimate: 15 minutes) Write a function called avgTempMonth that takes a dictionary (of
same format as you read from the data.txt file) and a month (as a string of 3 characters) and
returns the average temperature for the given month across all years rounded to 2 decimal places.
Note that you may create a dictionary in your function to help you go back and forth between
string and integer representation of months.
For example: month_dict = {"JAN": 1, "FEB": 2, "MAR": 3, etc.}
"""
def avgTempMonth(d:dict, month:str):
    month_dict = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12} 
    month_total = 0
    count = 0
    for year in d:
        if month in month_dict:
            month_index = month_dict[month]
            month_total += d[year][month_index - 1]
            count += 1
    if count > 0:
        return round(month_total / count, 2)
    else:
        return None
"""
2. (time estimate: 15 minutes) Download the file data.txt from Moodle. In your main
program, open the file data.txt for reading only. From this file you are to read all the lines
from the year 1964 to 1975 into a dictionary temp_dict. That is, all the lines in your file
before 1964 should not appear in temp_dict dictionary. In temp_dict the keys are the
years (as an integer), and the values are the list of temperatures from JAN to DEC (as floats and
changed to Celsius).
HINT: the map function may be useful to do fast change of floats from strings and from
Fahrenheit to Celsius.
"""
temp_dict = {}
file = open('assignment_3/data.txt', 'r')
reached_1964 = False
for line in file:
    if line.startswith('1964'):
        reached_1964 = True
    if(reached_1964):
        year, temperatures = line.strip().split()[0], line.strip().split()[1:]  
        year = int(year)
        celsius_temperatures = list(map(toCelsius, temperatures))  
        temp_dict[year] = celsius_temperatures
file.close()