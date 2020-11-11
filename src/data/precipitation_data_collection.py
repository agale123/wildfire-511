import requests
from datetime import date
import pandas as pd
import json
import csv

from pprint import pprint as pp

def parse_stations(file_path: str) -> list:
    """
    Read in a csv file and extract the stations out of it

    :param file_path: CSV file path
    """
    df = pd.read_csv(file_path)
    station_id_list = [v.strip() for v in list(df['ID'])]

    return station_id_list

def create_cdec_json_api_str(station_ids: list) -> str:
    """
    Function to call an api for the station ids and get the
    date from the start date to today.

    :param station_ids: List of station ids
    """
    api_str = "https://cdec.water.ca.gov/dynamicapp/req/JSONDataServlet"
    
    # seperator for these is '%2C' --> meaning a ','
    stations_str = '%2C'.join(station_ids)
    payload = {
        'Stations': stations_str,
        'SensorNums': 2,
        'dur_code': 'D',
        'Start': '1970-11-10',
        'End': '2020-11-10'
    }

    res = requests.get(api_str, params=payload)

    return res.json()

def json_to_csv(json_data, csv_filename, is_header=False):
    """
    Converting JSON data to CSV and saving locally

    :param json_file: JSON file to convert
    :param csv_filename: Filename to save csv
    :param is_header: Whether header should be written or not
    """
    data_file = open(csv_filename, 'a')

    csv_writer = csv.writer(data_file)
    
    for item in json_data:
        if is_header:
            is_header = False
            
            header = item.keys()
            csv_writer.writerow(header)
        
        csv_writer.writerow(item.values())
    
    data_file.close()

if __name__ == "__main__":
    precip_stations_file_path = "../../references/cdec-daily-reporting-precipitation-stations.csv"
    
    station_id_list = parse_stations(precip_stations_file_path)

    for i in range(0, len(station_id_list)-5, 5):
        json_obj = create_cdec_json_api_str(station_id_list[i:i+5])
        print(i)
        if i == 0:
            json_to_csv(json_obj, 'test.csv', is_header=True)
        else:
            json_to_csv(json_obj, 'test.csv')