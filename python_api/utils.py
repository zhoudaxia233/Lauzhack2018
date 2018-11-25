# coding: utf-8

def get_all_name_of_station_with_parking_lot(df_parking_lot):
    station_names = set()
    for i in range(len(df_parking_lot)):
        record = df_parking_lot.iloc[i]['fields']
        try:
            if int(record['parkrail_anzahl']) > 0:
                station_names.add(record['stationsbezeichnung'])
        except KeyError:
            continue
    return station_names

def _divide_df_by_linie_num(df_nearby_station):
    from collections import defaultdict 
    df_dict = defaultdict(list)
    for i in range(len(df_nearby_station)):
        record = df_nearby_station.iloc[i]['fields']
        try:
            df_dict[str(record['linie'])].append(dict(geopos=record['geopos'], linie=record['linie'], km=record['km'], abkurzung_bpk=record['abkurzung_bpk'], bezeichnung_bpk=record['bezeichnung_bpk']))
        except KeyError:
            continue
    return df_dict

def get_all_station_of_a_linie(df_nearby_station, linie_num):
    """Param
    linie_num: e.g. '300'
    """
    linie_list = _divide_df_by_linie_num(df_nearby_station)[linie_num]
    station_dist_tuple_pair = []
    for station in linie_list:
        station_dist_tuple_pair.append((station['bezeichnung_bpk'], station['km']))
    station_dist_tuple_pair_ascending = sorted(station_dist_tuple_pair, key=lambda i: i[1])
    return station_dist_tuple_pair_ascending

def get_all_linie_num_in_str_form(df_nearby_station):
    return list(_divide_df_by_linie_num(df_nearby_station).keys())

def get_nearest_station_name(df_nearby_station, linie_num, station_name):
    from collections import deque
    nearest_stations = deque(maxlen=2)
    nearest_stations_reverse = deque(maxlen=2)
    all_station_of_linie = get_all_station_of_a_linie(df_nearby_station, linie_num)
    all_station = []
    for station in all_station_of_linie:
        all_station.append(station[0])
    if station_name in all_station:
        for station in all_station:
            if station_name == station:
                break
            nearest_stations.append(station)

        for station in all_station[::-1]:
            if station_name == station:
                break
            nearest_stations_reverse.append(station)
    
    return list(nearest_stations) + list(nearest_stations_reverse)

