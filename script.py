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
updated_damages = []
def update_damage():
  for data in damages:
    if (data == 'Damages not recorded'):
      updated_damages.append(data)
    else:
      if (data[-1] == 'M'):
        float_data = float(data[:-1]) * 1000000
      elif (data[-1] == 'B'):
        float_data = float(data[:-1]) * 1000000000
      updated_damages.append(float_data)     

update_damage()
#print(updated_damages)

# write your construct hurricane dictionary function here:
hurricance_dict = {}
for i in range(0, len(names)):
  hurricance_dict.update({names[i]: {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max sustained wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': updated_damages[i], 'Deaths': deaths[i]}})
#print(hurricance_dict)

# write your construct hurricane by year dictionary function here:
def hurricane_by_year():
  unique_years = list(set(years))
  hurricane_by_years = {}
  for uni_year in unique_years:
    year_sorted = []
    for key,value in hurricance_dict.items():
      if (uni_year == value['Year']):
        year_sorted.append(value)
    hurricane_by_years[uni_year] = year_sorted
  return hurricane_by_years
#print(hurricane_by_year())

# write your count affected areas function here:
def area_affected_count():
  area_affected_count = {}
  area_affected_list = []
  for areas in areas_affected:
    area_affected_list = area_affected_list + areas
  unique_areas = list(set(area_affected_list))
  for area in unique_areas:
    x = area_affected_list.count(area)
    area_affected_count[area] = x
  return area_affected_count
 
#print(area_affected_count())
# write your find most affected area function here:
def most_affected_area():
 area_dict = area_affected_count()
 num_list = list(area_dict.values())
 max_damaged_count = max(num_list)
 i = num_list.index(max_damaged_count)
 area_list = list(area_dict.keys())
 most_affected_area = area_list[i]
 print ("{} is the most affected area by hurricane. It was struck {} times.".format(most_affected_area, max_damaged_count))
 #print (num_list)
 #print (i)
 #print (max_damaged_count)
 #print(area_list)
 #print(most_affected_area)
most_affected_area()
# write your greatest number of deaths function here:
def deadliest_hurricane():
  max_deaths = max(deaths)
  i = deaths.index(max_deaths)
  deadly_hurricane = names[i]
  print ("{} is the deadliest hurricane in the history causing {} deaths.".format(deadly_hurricane, max_deaths))

deadliest_hurricane()





# write your catgeorize by mortality function here:
def mortality_scale_dict():
  mortality_scale = {}
  scale_0 = []
  scale_1 = []
  scale_2 = []
  scale_3 = []
  scale_4 = []
  scale_5 = []

  for i in range(len(names)):
    if deaths[i] == 0:
      scale_0.append(hurricance_dict[names[i]])
    elif deaths[i] <= 100:
      scale_1.append(hurricance_dict[names[i]])
    elif deaths[i] <= 500:
      scale_2.append(hurricance_dict[names[i]])
    elif deaths[i] <= 1000:
      scale_3.append(hurricance_dict[names[i]])
    elif deaths[i] <= 10000:
      scale_4.append(hurricance_dict[names[i]])
    elif deaths[i] > 10000:
      scale_5.append(hurricance_dict[names[i]])

  mortality_scale.update({0:scale_0, 1:scale_1, 2:scale_2, 3:scale_3, 4:scale_4, 5:scale_5})

  return mortality_scale

# write your greatest damage function here:
def greatest_damage():
  index = updated_damages.index(max([num for num in updated_damages if isinstance(num, float)]))
  max_damage_hurr = list(hurricance_dict)[index]
  max_damage = hurricance_dict[max_damage_hurr]['Damage']
  return (max_damage_hurr, max_damage)

print(greatest_damage())






# write your catgeorize by damage function here:

def damage_function():
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for i in range(len(updated_damages)):
    if isinstance(updated_damages[i], float):
      if updated_damages[i] == 0:
        hurricanes_by_damage[0].append(hurricance_dict[names[i]])
      elif updated_damages[i] <= 100000000:
        hurricanes_by_damage[1].append(hurricance_dict[names[i]])
      elif updated_damages[i] <= 1000000000:
        hurricanes_by_damage[2].append(hurricance_dict[names[i]])
      elif updated_damages[i] <= 10000000000:
        hurricanes_by_damage[3].append(hurricance_dict[names[i]])
      elif updated_damages[i] <= 50000000000:
        hurricanes_by_damage[4].append(hurricance_dict[names[i]])
      elif updated_damages[i] > 50000000000:
        hurricanes_by_damage[5].append(hurricance_dict[names[i]])
    else:
      pass
  return hurricanes_by_damage

print(damage_function())


