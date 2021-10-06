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

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def convert_damages_data(damages):
  damages_updated = []
  for cost in damages:
    if cost == 'Damages not recorded':
      damages_updated.append(cost)
    elif cost.find('M') != -1:
      damages_updated.append(float(cost[0:cost.find('M')])*conversion['M'])
    elif cost.find('B') != -1:
      damages_updated.append(float(cost[0:cost.find('B')])*conversion['B'])
  return damages_updated

updated_damages = convert_damages_data(damages)
print(updated_damages)
print('###')
#2
# Create a dictionary with name as its key 
def hurricanes_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  hurricanes_info = {}
  hurricanes = len(names)
  for i in range(hurricanes):
    hurricanes_info[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': updated_damages[i], 'Deaths': deaths[i]}
  return hurricanes_info
hurricanes_data = hurricanes_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

print(hurricanes_data['Cuba I'])
print('###')
# 3
# Create a Dictionary with Year as its keys
def hurricane_year_dictionary(hurricanes_data):
  hurricanes_by_date = {}
  for hurricane in hurricanes_data:
    current_year = hurricanes_data[hurricane]['Year']
    hurricane_info = hurricanes_data[hurricane]
    if not current_year  in hurricanes_by_date:
      hurricanes_by_date[current_year] = [hurricane_info]
    else:
      hurricanes_by_date[current_year].append(hurricane_info)
  return hurricanes_by_date

hurricanes_by_year = hurricane_year_dictionary(hurricanes_data)
print(hurricanes_by_year[1932])
print('###')
# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def counting_areas(hurricanes):
  areas_affected = {}
  for hurricane in hurricanes:
    for area in hurricanes[hurricane]['Areas Affected']:
      if area not in areas_affected:
        areas_affected[area] = 1
      else:
        areas_affected[area] +=1
  return areas_affected
areas_affected = counting_areas(hurricanes_data)
print(areas_affected)
# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def most_affected_area(areas_affected):
  most_affected = 0
  for area in areas_affected:
    if areas_affected[area] > most_affected:
      most_affected = areas_affected[area]
      most_affected_hurricane = area
  return most_affected_hurricane, most_affected
print(most_affected_area(areas_affected)
)
# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths
def most_deadly_hurricane(hurricanes_data):
  death_count = 0
  for hurricane in hurricanes_data:
    if hurricanes_data[hurricane]['Deaths'] > death_count:
      death_count = hurricanes_data[hurricane]['Deaths']
      deadliest_hurricane = hurricane
    elif hurricanes_data[hurricane]['Deaths'] == death_count:
      deadliest_hurricane += ', ' + hurricane 
  return deadliest_hurricane, death_count
print(most_deadly_hurricane(hurricanes_data))
print('###')
# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
def hurricane_mortality(hurricanes):
  mortality_dictionary = {1: [], 2: [], 3: [], 4: [], 5: []}
  for hurricane in hurricanes:
    num_deaths = hurricanes[hurricane]['Deaths']
    if num_deaths <= mortality_scale[1]:
      mortality_dictionary[1].append(hurricanes[hurricane])
    elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
      mortality_dictionary[2].append(hurricanes[hurricane])
    elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
      mortality_dictionary[3].append(hurricanes[hurricane])
    elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
      mortality_dictionary[4].append(hurricanes[hurricane])
    else:
      mortality_dictionary[5].append(hurricanes[hurricane])

  return mortality_dictionary
  
# categorize hurricanes in new dictionary with mortality severity as key
mortality_of_hurricanes = hurricane_mortality(hurricanes_data)
print(mortality_of_hurricanes[5])

# 8 Calculating Hurricane Maximum Damage
def finding_greatest_damage(hurricanes):
  damaged_caused = 0 
  for hurricane in hurricanes:
    hurricane_damage = hurricanes[hurricane]['Damage']
    if hurricane_damage == 'Damages not recorded':
      continue
    elif hurricane_damage > damaged_caused:
      damaged_caused = hurricane_damage
    
  return damaged_caused, hurricane

damage_caused, hurricane = finding_greatest_damage(hurricanes_data)
print('The hurricane that made the greatest damage was {hurricane} and the repairment costed {damage_caused}$.'.format(hurricane = hurricane, damage_caused = damage_caused))
# find highest damage inducing hurricane and its total cost
print('###')

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
def scaling_damage(hurricanes):
  scale_hurricane_by_damage = {1: [], 2: [], 3: [], 4: [], 5: []}
  for hurricane in hurricanes:
    hurricane_info = hurricanes[hurricane]
    damage_by_hurricane = hurricanes[hurricane]['Damage']
    if damage_by_hurricane == 'Damages not recorded':
      pass
    elif damage_by_hurricane <= damage_scale[1]:
      scale_hurricane_by_damage[1].append(hurricane_info)
    elif damage_by_hurricane > damage_scale[1] and damage_by_hurricane <= damage_scale[2]:
      scale_hurricane_by_damage[2].append(hurricane_info) 
    elif damage_by_hurricane > damage_scale[2] and damage_by_hurricane <= damage_scale[3]:
      scale_hurricane_by_damage[3].append(hurricane_info)
    elif damage_by_hurricane > damage_scale[3] and damage_by_hurricane <= damage_scale[4]:
      scale_hurricane_by_damage[4].append(hurricane_info)
    else:
        scale_hurricane_by_damage[5].append(hurricane_info)
  return scale_hurricane_by_damage
# categorize hurricanes in new dictionary with damage severity as key
damage_severity = scaling_damage(hurricanes_data)
print(damage_severity[5])
