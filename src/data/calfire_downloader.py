import urllib.request
import json
import pandas as pd

years = [str(y) for y in range(2003, 2020 + 1)]
frames = [] #will store dataframes in here pre-concatenation

for year in years: #request data for each year
    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/Api/IncidentApi/GetIncidents?year=" + year) as url:
        data = json.loads(url.read().decode())
        df = pd.DataFrame.from_dict(data['Incidents'])
        frames.append(df)

total_df = pd.concat(frames) #concatenate yearly fire data
total_df.to_csv('calfire.csv')
