"""
12/25/2020
April Leclair

PYTHON FUNDAMENTALS
Hurricane Analysis
Overview
This project is slightly different than others you have encountered thus far on Codecademy. Instead of a step-by-step tutorial, this project contains a series of open-ended requirements which describe the project you’ll be building. There are many possible ways to correctly fulfill all of these requirements, and you should expect to use the internet, Codecademy, and other resources when you encounter a problem that you cannot easily solve.

Project Goals
You will work to write several functions that organize and manipulate data about Category 5 Hurricanes, the strongest hurricanes as rated by their wind speed. Each one of these functions will use a number of parameters, conditionals, lists, dictionaries, string manipulation, and return statements.

Setup Instructions
If you choose to do this project on your computer instead of Codecademy, you can download what you’ll need by clicking the “Download” button below. If you need help setting up your computer, be sure to check out our setup guide.
"""

# Variables
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# Prerequisites
"""
1.
In order to complete this project, you should have completed the Loops and Dictionaries sections of the Learn Python 3 Course. This content is also covered in the Data Scientist Career Path.
"""


# Project Requirements
"""
2.
Hurricanes, also known as cyclones or typhoons, are one of the most powerful forces of nature on Earth. Due to climate change caused by human activity, the number and intensity of hurricanes has risen, calling for better preparation by the many communities that are devastated by them. As a concerned environmentalist, you want to look at data about the most powerful hurricanes that have occurred.

Begin by looking at the damages list. The list contains strings representing the total cost in USD($) caused by 34 category 5 hurricanes (wind speeds ≥ 157 mph (252 km/h )) in the Atlantic region. For some of the hurricanes, damage data was not recorded ("Damages not recorded"), while the rest are written in the format "Prefix-B/M", where B stands for billions (1000000000) and M stands for millions (1000000).

Write a function that returns a new list of updated damages where the recorded data is converted to float values and the missing data is retained as "Damages not recorded".

Test your function with the data stored in damages.
"""
# write your update damages function here:

# Version 1
def damage():
    nl = []
    for i in damages:
        if i[-1]=="B":
            nl.append(float(i[:len(i)-1])*1000000000)
        elif i[-1]=="M":
            nl.append(float(i[:len(i)-1])*1000000)
        else:
            nl.append(i)
    return nl

# Version 2
def damage():
    conversion = {"M": 1000000, "B": 1000000000}
    nl = []
    for i in damages:
        if i[-1] == "d":
            nl.append(i)
        else:
            nl.append(float(i[:-1])*conversion.get(i[-1]))
    return nl

# Version 3
def damage():
    conversion = {"M": 1000000, "B": 1000000000}
    nl = []
    for i in damages:
        try: nl.append(float(i[:-1])*conversion.get(i[-1]))
        except ValueError: nl.append(i)
    return nl

# Version 4
conversion = {"M": 1000000, "B": 1000000000}
damagesN = [i if i[-1] == "d" else float(i[:-1])*conversion.get(i[-1]) for i in damages]


"""
3.
Additional data collected on the 34 strongest Atlantic hurricanes are provided in a series of lists. The data includes:

names: names of the hurricanes
months: months in which the hurricanes occurred
years: years in which the hurricanes occurred
max_sustained_winds: maximum sustained winds (miles per hour) of the hurricanes
areas_affected: list of different areas affected by each of the hurricanes
deaths: total number of deaths caused by each of the hurricanes
The data is organized such that the data at each index, from 0 to 33, corresponds to the same hurricane.

For example, names[0] yields the “Cuba I” hurricane, which ouccred in months[0] (October) years[0] (1924).

Write a function that constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes, and the values are dictionaries themselves containing a key for each piece of data (Name, Month, Year,Max Sustained Wind, Areas Affected, Damage, Death) about the hurricane.

Thus the key "Cuba I" would have the value: {'Name': 'Cuba I', 'Month': 'October', 'Year': 1924, 'Max Sustained Wind': 165, 'Areas Affected': ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 'Damage': 'Damages not recorded', 'Deaths': 90}.

Test your function on the lists of data provided.
"""

# write your construct hurricane dictionary function here:
value = names
key = [{'Name': a, 'Month': b, 'Year': c, 'Max Sustained Wind': d,
        'Areas Affected': e, 'Damage': f, 'Deaths': g}
       for a,b,c,d,e,f,g in
       zip(names, months, years, max_sustained_winds,
           areas_affected, damagesN, deaths)]
hurricane = {k:v for k,v in zip(value,key)}


"""
4.
In addition to organizing the hurricanes in a dictionary with names as the key, you want to be able to organize the hurricanes by year.

Write a function that converts the current dictionary of hurricanes to a new dictionary, where the keys are years and the values are lists containing a dictionary for each hurricane that occurred in that year.

For example, the key 1932 would yield the value: [{'Name': 'Bahamas', 'Month': 'September', 'Year': 1932, 'Max Sustained Wind': 160, 'Areas Affected': ['The Bahamas', 'Northeastern United States'], 'Damage': 'Damages not recorded', 'Deaths': 16}, {'Name': 'Cuba II', 'Month': 'November', 'Year': 1932, 'Max Sustained Wind': 175, 'Areas Affected': ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 'Damage': 40000000.0, 'Deaths': 3103}].

Test your function on your hurricane dictionary.
"""

def hurricane_yr():
    import numpy as np
    hurricane_by_year = {}
    yr = np.unique(sorted(years))
    for y in yr:
        hurricane_by_year[y] = [hurricane[key] for key in hurricane if y == hurricane[key]["Year"]]
    return hurricane_by_year

hurricane_by_yr = hurricane_yr()
hurricane_by_yr


"""
5.
You believe that knowing how often each of the areas of the Atlantic are affected by these strong hurricanes is important for making preparations for future hurricanes.

Write a function that counts how often each area is listed as an affected area of a hurricane. Store and return the results in a dictionary where the keys are the affected areas and the values are counts of how many times the areas were affected.

Test your function on your hurricane dictionary.
"""

# write your count affected areas function here:
import numpy as np
def hurricane_freq():
    hurricane_by_freq = {}
    areas = list(np.concatenate(areas_affected))
    for area in areas:
        hurricane_by_freq[area] = areas.count(area)
    return hurricane_by_freq

hurricane_by_freq = hurricane_freq()
hurricane_by_freq

# def hurricane_freq():
#     hurricane_by_freq = {}
#     areas = []
#     areas_flatten = [[[areas.append(j) for j in i] for i in areas_affected]]
#     for area in areas:
#         hurricane_by_freq[area] = areas.count(area)
#     return hurricane_by_freq


"""
6.
Write a function that finds the area affected by the most hurricanes, and how often it was hit.

Test your function on your affected area dictionary.
"""

# write your find most affected area function here:
def mostaffected():
    for area, freq in list(hurricane_by_freq.items()):
        if freq == max(list(hurricane_by_freq.values())):
            return area

most_affected_area = mostaffected()
most_affected_area


"""
7.
Write a function that finds the hurricane that caused the greatest number of deaths, and how many deaths it caused.

Test your function on your hurricane dictionary.
"""
# write your greatest number of deaths function here:
def greatest_deaths():
    for name, info in hurricane.items():
        if info.get("Deaths") == max(deaths):
            return name


"""
8.
Just as hurricanes are rated by their windspeed, you want to try rating hurricanes based on other metrics.

Write a function that rates hurricanes on a mortality scale according to the following ratings, where the key is the rating and the value is the upper bound of deaths for that rating.

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
                   
For example, a hurricane with a 1 mortality rating would have resulted in greater than 0 but less than or equal to 100 deaths. A hurricane with a 5 mortality rating would have resulted in greater than 10000 deaths.

Store the hurricanes in a new dictionary where the keys are mortality ratings and the values are lists containing a dictionary for each hurricane that falls into that mortality rating.

Test your function on your hurricane dictionary.
"""

# write your catgeorize by mortality function here:
# Make a mortality scale variable
def mort_scale(d):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    scales = sorted(mortality_scale.keys(), reverse=1)[1:]
    for scale in scales:
        if d > mortality_scale[scale]:
            return scale+1
    return 0

# Add the mortality scale variable to the hurricane dictionary
for key, value in hurricane.items():
  value["Mortality Scale"] = mort_scale(value["Deaths"])

# Make a new hurricane by mortality dictionary
def hurricane_mort():
    hurricane_by_mort = {}
    scales_unique = np.unique([hurricane[key]["Mortality Scale"] for key in hurricane])
    for scale in scales_unique:
        hurricane_by_mort[scale] = [value for key,value in hurricane.items() if value["Mortality Scale"] == scale]
    return hurricane_by_mort

hurricane_by_mort = hurricane_mort()
hurricane_by_mort


"""
9.
Write a function that finds the hurricane that caused the greatest damage, and how costly it was.

Test your function on your hurricane dictionary.
"""

# write your greatest damage function here:
for key,value in hurricane.items():
    for i in range(len(damages)):
        value["Damage Str"] = damages[i]

def greatest_damage():
    for key,value in hurricane.items():
        if value["Damage"] == max([0 if type(i) == str else i for i in damagesN]):
            return key + ", $" + str(value["Damage Str"])


"""
10.
Lastly, you want to rate hurricanes according to how much damage they cause.

Write a function that rates hurricanes on a damage scale according to the following ratings, where the key is the rating and the value is the upper bound of damage for that rating.

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
                
For example, a hurricane with a 1 damage rating would have resulted in damages greater than 0 USD but less than or equal to 100000000 USD. A hurricane with a 5 damage rating would have resulted in damages greater than 50000000000 USD (talk about a lot of money).

Store the hurricanes in a new dictionary where the keys are damage ratings and the values are lists containing a dictionary for each hurricane that falls into that damage rating.

Test your function on your hurricane dictionary.
"""

# write your catgeorize by damage function here:
def dam_scale(damage):
    hurricane_by_damScale = {}
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}
    scales = sorted(damage_scale.keys(),reverse=1)[1:]
    if type(damage) == str:
        return damage
    else:
        for scale in scales:
            if damage > damage_scale[scale]:
                return scale+1
        return 0

for key,value in hurricane.items():
    value["Damage Scale"] = dam_scale(value["Damage"])

def hurricane_damScale():
    hurricane_by_damScale = {}
    scales_unique = set([value["Damage Scale"] for value in hurricane.values()])
    for scale in scales_unique:
        hurricane_by_damScale[scale] = [value for key,value in hurricane.items() if value["Damage Scale"] == scale]
    return hurricane_by_damScale

hurricane_by_damScale = hurricane_damScale()
hurricane_by_damScale