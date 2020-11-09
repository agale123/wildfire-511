import requests
import json

email = 'TODO'
key = 'TODO'

# Get air quality data for PM2.5 (param=88101) each year from 2003 till today
for year in range(2003, 2020):
    r = requests.get('https://aqs.epa.gov/data/api/dailyData/byState?email=' + email + '&key=' + key + '&param=88101&bdate=' + str(year) + '0101&edate=' + str(year) + '1231&state=06')
    f = open('../data_raw/airquality/'str(year) + '.json', 'w')
    f.write(r.text)
    f.close()