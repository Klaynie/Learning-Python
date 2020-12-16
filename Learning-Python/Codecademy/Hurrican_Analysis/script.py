# names of hurricanes
names = [
    'Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II',
    'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet',
    'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
    'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina',
    'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael'
]

# months of hurricanes
months = [
    'October', 'September', 'September', 'November', 'August', 'September',
    'September', 'September', 'September', 'September', 'September', 'October',
    'September', 'August', 'September', 'September', 'August', 'August',
    'September', 'September', 'August', 'October', 'September', 'September',
    'July', 'August', 'September', 'October', 'August', 'September', 'October',
    'September', 'September', 'October'
]

# years of hurricanes
years = [
    1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961,
    1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004,
    2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018
]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [
    165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
    175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175,
    165, 180, 175, 160
]

# areas affected by each hurricane
areas_affected = [
    ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
    [
        'Lesser Antilles', 'The Bahamas', 'United States East Coast',
        'Atlantic Canada'
    ], ['The Bahamas', 'Northeastern United States'],
    [
        'Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas',
        'Bermuda'
    ], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'],
    ['Jamaica', 'Yucatn Peninsula'],
    ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
    [
        'Southeastern United States', 'Northeastern United States',
        'Southwestern Quebec'
    ], ['Bermuda', 'New England', 'Atlantic Canada'],
    ['Lesser Antilles', 'Central America'],
    ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
    ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
    ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'],
    ['Mexico'], ['The Caribbean', 'United States East coast'],
    ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
    ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
    ['The Caribbean', 'United States East Coast'],
    ['The Bahamas', 'Florida', 'United States Gulf Coast'],
    ['Central America', 'Yucatn Peninsula', 'South Florida'],
    ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
    ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
    ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'],
    ['Bahamas', 'United States Gulf Coast'],
    ['Cuba', 'United States Gulf Coast'],
    ['Greater Antilles', 'Central America', 'Florida'],
    ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
    [
        'Antilles', 'Venezuela', 'Colombia', 'United States East Coast',
        'Atlantic Canada'
    ],
    [
        'Cape Verde', 'The Caribbean', 'British Virgin Islands',
        'U.S. Virgin Islands', 'Cuba', 'Florida'
    ],
    [
        'Lesser Antilles', 'Virgin Islands', 'Puerto Rico',
        'Dominican Republic', 'Turks and Caicos Islands'
    ],
    [
        'Central America',
        'United States Gulf Coast (especially Florida Panhandle)'
    ]
]

# damages (USD($)) of hurricanes
damages = [
    'Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M',
    '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M',
    '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
    '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B',
    '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B'
]

# deaths for each hurricane
deaths = [
    90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11,
    2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603,
    138, 3057, 74
]


# write your update damages function here:
def convert_damages(damages):
    result = []
    for item in damages:
        last_letter = item[-1]
        if last_letter == 'M':
            damage = float(item[:len(item) - 1]) * 1000000
        elif last_letter == 'B':
            damage = float(item[:len(item) - 1]) * 1000000000
        else:
            damage = 'Damages not recorded'
        result.append(damage)
    return result


converted_damages = convert_damages(damages)


# write your construct hurricane dictionary function here:
def construct_hurricane_dict(names, months, years, max_sustained_winds,
                             areas_affected, deaths):
    result = {}
    for i in range(len(names)):
        result[names[i]] = {
            'Name': names[i],
            'Month': months[i],
            'Year': years[i],
            'Max Sustained Wind': max_sustained_winds[i],
            'Areas Affected': areas_affected[i],
            'Deaths': deaths[i]
        }
    return result


hurricane_dict = construct_hurricane_dict(names, months, years,
                                          max_sustained_winds, areas_affected,
                                          deaths)


# write your construct hurricane by year dictionary function here:
def hurricans_by_year(hurricane_dict):
    result = {}
    for value in hurricane_dict.values():
        if value['Year'] in result:
            result[value['Year']].append(value)
        else:
            result[value['Year']] = [value]
    return result


year_dict = hurricans_by_year(hurricane_dict)


# write your count affected areas function here:
def count_affected_areas(areas_affected):
    result = {}
    for areas in areas_affected:
        for area in areas:
            result[area] = 1 + result.get(area, 0)
    return result


affected_areas_count = count_affected_areas(areas_affected)


# write your find most affected area function here:
def find_most_affected_area(affected_areas_count):
    result = {}
    max_count = 0
    for key, value in affected_areas_count.items():
        if value > max_count:
            max_count = value
            result = {key: value}
    return result


most_affected_area = find_most_affected_area(affected_areas_count)


# write your greatest number of deaths function here:
def find_max_deaths(names, deaths):
    result = {}
    max_count = 0
    for i in range(len(names)):
        if deaths[i] > max_count:
            max_count = deaths[i]
            result = {names[i]: deaths[i]}
    return result


max_deaths = find_max_deaths(names, deaths)


# write your catgeorize by mortality function here:
def categorize_mortality_rate(names, deaths):
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    result = {}
    for i in range(len(names)):
        max_rating = 0
        for rating, upper_bond in mortality_scale.items():
            max_rating = rating
            if deaths[i] <= upper_bond:
                break
        if max_rating in result:
            result[max_rating].append(names[i])
        else:
            result[max_rating] = [names[i]]
    return result


mortality_ratings = categorize_mortality_rate(names, deaths)


# write your greatest damage function here:
def find_max_damage(names, converted_damages):
    result = {}
    max_damage = 0
    for i in range(len(names)):
        try:
            float(converted_damages[i])
            if converted_damages[i] > max_damage:
                max_damage = converted_damages[i]
                result = {names[i]: converted_damages[i]}
        except ValueError:
            pass
    return result


max_damage = find_max_damage(names, converted_damages)


# write your catgeorize by damage function here:
def categorize_damage_rate(names, converted_damages):
    damage_scale = {
        0: 0,
        1: 100000000,
        2: 1000000000,
        3: 10000000000,
        4: 50000000000
    }
    result = {}
    for i in range(len(names)):
        try:
            float(converted_damages[i])
            max_rating = 0
            for rating, upper_bond in damage_scale.items():
                max_rating = rating
                if converted_damages[i] <= upper_bond:
                    break
            if max_rating in result:
                result[max_rating].append(names[i])
            else:
                result[max_rating] = [names[i]]
        except ValueError:
            pass
    return result


damage_ratings = categorize_damage_rate(names, converted_damages)
print(damage_ratings)