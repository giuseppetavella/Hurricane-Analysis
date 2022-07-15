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

# write your update damages function here:


def damages_clean(values):
    values_new = []
    value_new = ''
    digit_map = {
        "M": 1000000,
        "B": 1000000000
    }
    for a in values:
        if a == "Damages not recorded":
            value_new = a
        else:
            last_char = a[-1]
            number = float(a[:-1])
            number_final = number * digit_map[last_char]
            value_new = number_final
        values_new.append(value_new)
    return values_new    

damages_cleaned = damages_clean(damages)


# write your construct hurricane dictionary function here:


def hurricanes_dict_names():
    dict = {}
    for i in range(len(names)):
        name = names[i]
        dict[name] = {
            "Month": months[i],
            "Year": years[i],
            "Max_sustained_winds": max_sustained_winds[i],
            "Areas_affected": areas_affected[i],
            "Damages": damages_cleaned[i],
            "Deaths": deaths[i]
        }
    return dict


hurricanes_by_names = hurricanes_dict_names()



# write your construct hurricane by year dictionary function here:


def hurricanes_dict_years():
    dict = {}
    for name, value in hurricanes_by_names.items():
        this_year = value["Year"]
        new_value = value
        new_value["Name"] = name
        if this_year not in dict:
            dict[this_year] = [new_value]
        else:
            dict[this_year].append(new_value)
    return dict


hurricanes_by_years = hurricanes_dict_years()



# write your count affected areas function here:

def count_affected_areas():
    dict = {}
    for value in hurricanes_by_names.values():
        this_areas = value["Areas_affected"]
        for area in this_areas:
            if area in dict:
                dict[area] += 1
            else:
                dict[area] = 0
    return dict

affected_areas = count_affected_areas()




# write your find most affected area function here:

def count_most_affected_areas():
    most_affected = {}
    min_hits = 1
    for name, hits in affected_areas.items():
        if hits > min_hits:
            min_hits = hits
            most_affected = {name: hits}
    return most_affected


most_affected_area = count_most_affected_areas()


# write your greatest number of deaths function here:


def find_deadliest_hurricane():
    deadliest_hurricane = {}
    min_deaths = 1
    for name, values in hurricanes_by_names.items():
        deaths = values["Deaths"]
        if deaths > min_deaths:
            min_deaths = deaths
            deadliest_hurricane = {name: deaths}
    return deadliest_hurricane


deadliest_hurricane = find_deadliest_hurricane()


# write your catgeorize by mortality function here:

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}


def initiate_scale(scale):
    result = {}
    for key in scale:
        result[key] = []
    result[len(scale)] = [] 
    return result



def get_rating(value, kind):
    if kind == "mortality":
        scale = mortality_scale
    elif kind == "damage":
        scale = damage_scale
    rating = 0
    for key, this_rating in scale.items():
        next_key = key + 1
        next_key_exists = next_key in scale
        if key in scale and next_key_exists == False:
            rating = next_key
            break
        if value > this_rating and value <= scale[next_key]:
            rating = next_key
            break        
    return rating



def categorize_by_mortality():
    mortality_result = initiate_scale(mortality_scale)
    for name, values in hurricanes_by_names.items():
        deaths = values["Deaths"]
        rating = get_rating(deaths, "mortality")
        mortality_result[rating].append(values)
    return mortality_result


hurricanes_by_mortality = categorize_by_mortality()


# write your greatest damage function here:


def find_greatest_damage_hurricane():
    greatest_damage_hurricane = {}
    min_damage = 0
    for name, values in hurricanes_by_names.items():
        this_damage = values["Damages"]
        if this_damage == "Damages not recorded":
            continue
        if this_damage > min_damage:
            min_damage = this_damage
            greatest_damage_hurricane = {name: this_damage}
    return greatest_damage_hurricane

  
greatest_damage_hurricane = find_greatest_damage_hurricane()



# write your catgeorize by damage function here:

def categorize_by_damage():
    damage_result = initiate_scale(damage_scale)
    for name, values in hurricanes_by_names.items():
        damages = values["Damages"]
        if damages == "Damages not recorded":
            continue
        rating = get_rating(damages, "damage")
        damage_result[rating].append(values)
    return damage_result


hurricanes_by_damage = categorize_by_damage()
print(hurricanes_by_damage)