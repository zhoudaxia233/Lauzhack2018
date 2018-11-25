# coding: utf-8
import pandas as pd
from utils import *

file_parking_lot = 'mobilitat.json'
file_nearby_station = 'linie-mit-betriebspunkten.json'

df_parking_lot = pd.read_json(file_parking_lot)
df_nearby_station = pd.read_json(file_nearby_station)

# print(get_all_station_of_a_linie(df_nearby_station, '300'))
# print(get_all_linie_num_in_str_form(df_nearby_station))
# print(get_nearest_station_name(df_nearby_station, '300', 'Frutigen'))
