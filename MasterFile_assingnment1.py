import json
import os
import pprint
import plotly.express as px
from itertools import chain
import folium
import pandas as pd
import requests
import pprint
from folium.plugins import HeatMap, heat_map

os.chdir("C:\\Users\\abhin\\OneDrive\\Documents\\Course Content\\Python programming")

def load_json_file_named(file_name):
    try:
        loaded_data = []
        file_location = f"data/{file_name}"
        with open(file_location, 'r') as file: # or f"data/{file_name}" depending on your files
            loaded_data =  json.load(file)
    except OSError as e:
        print(f"Error. Does the file exist in this folder? {file_location}\n\n {e}")
    return loaded_data

file_path = "nhs_scotland_boards.json"
with open(file_path, 'r') as json_file:
    data = json.load(json_file)



# Function to parsse through various nested dictionary dimensions
def extract_all_values(dict_temp, dimension):
    # Clear the list before appending new values
    value_list_def = list(value for key, value in dict_temp.items())
    key_list_def = list(key for key, value in dict_temp.items())
    result = key_list_def if dimension == "key" else value_list_def

    return result


budget_count = list(chain(*list(extract_all_values(i['budget_billions'], "values") for i in data)))
# regions= list(i['name'] for i in data for _ in range(3))
regions = list(i['name'] for i in data)
regions
year_mapping = list(chain(*list(extract_all_values(i['budget_billions'], "key") for i in data)))
staff_count = list(extract_all_values(i['people'], "values") for i in data)
staff_count = [list(i) for i in zip(*staff_count)][1]
area_in_km2 = list(extract_all_values(i['geographic'], "values") for i in data)
area_in_km2 = [list(i) for i in zip(*area_in_km2)][0]

staff_per_area = [round(staff/area,2) for staff,area in zip(staff_count, area_in_km2)]
staff_per_area


staff_count
area_in_km2

data_sunburst = dict(
    budget_count = budget_count,
    regions = list(i for i in regions for _ in range(3)) ,
    years = year_mapping
)



fig = px.sunburst(data_sunburst,path= ['regions', 'years'], values = 'budget_count',color = 'budget_count', title = "SunBurst Chart of Accumulated Budgets over years for different NHS bases")

fig.show()


# map_nhs_hosp = folium.Map(location=[28.644800, 77.216721]).show_in_browser()

regions[2]



def lat_lng_builder(regions):
    url = 'https://api.geoapify.com/v1/geocode/search'
    params = dict(
    text= regions,
    apiKey='c4380cfb076b4cdab76c167d26d5467c' )
    resp = requests.get(url=url, params=params)
    datamap = resp.json()
    return datamap['features'][0]["geometry"]["coordinates"][::-1]
 

regions
regions_coordinates = list(lat_lng_builder(region) for region in regions)

len(regions_coordinates)


# lat_lng_builder(regions[5])
# print(regions_coordinates)

fig_layout=folium.Figure(height=350,width=550)
map_main=folium.Map(location= lat_lng_builder("University of Edinburgh Business School, 29 Buccleuch Place ,Edinburgh"),tiles='cartodbpositron',zoom_start=8)
fig_layout.add_child(map_main)
custom_icon = folium.DivIcon(html='<i class="fas fa-person-dress fa-2x"></i>', icon_size=(30, 30))


for index, nhslocs in enumerate(regions_coordinates):
    folium.Marker(location = nhslocs, popup = f"""
    <h1> {regions[index]}</h1><br>
   <h2> Number of Staff{staff_count[index]} </h2><br>
   <h2> Area in Km^2{area_in_km2[index]}""").add_to(map_main)

map_main.show_in_browser()

# regions[1]

regions_coordinates[2]
heat_map_list.clear()
nhslocs = []



combined_list = []

for index, (nhslocs, staff) in enumerate(zip(regions_coordinates, staff_per_area)):
    combined_list = nhslocs + [staff]
    HeatMap([combined_list]).add_to(map_main)


map_main.show_in_browser()




combined_list



# Create a heatmap layer


nhslocs.extend([(staff_count[1]/area_in_km2[1])])


for index, (a, b) in enumerate(zip([1, 2], [4, 5])):
    print(str(a) + " " + str(b))


