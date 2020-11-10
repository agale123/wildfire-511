**Webpages**

1. [Daily Reporting Stations](https://info.water.ca.gov/misc/dailyStations.html)
    * Allows user to view all the stations that report *some information* daily
2. [Daily Precipitation Stations](https://cdec.water.ca.gov/reportapp/javareports?name=DailyPrecip)
    * Allows user to view all the stations that report *some information* daily

**APIs**
1. [Precipitation API per station](https://cdec.water.ca.gov/dynamicapp/QueryDaily?s=ELK&end=2020-11-10&span=30days)
    * Allows user to query, for a given station, the weather data
    * The format is not computer-friendly. Most likley will require web scraping
    * Station names in *cdec-daily-reporting-precipitation-stations.csv* can be used with this API
2. [Precipitation API multiple station](https://cdec.water.ca.gov/dynamicapp/req/CSVDataServlet?Stations=ELK%2CGAS%2CDRF%2COLS&SensorNums=2&dur_code=D&Start=2010-11-10&End=2020-11-10)
    * Allows user to query the data from multiple stations


### Misc. Information:
**PRECIPITATION, ACCUMULATED**
A sensor type where the field measuring device accumulates precipitation during the water year. Some stations accumulation tanks periodically dump the accumulated precipitation to make room for more precipitation. This may cause the value transmitted to jump backward several inches. The value usually accumulates or gets larger until it is reset. A reset may occur if a technician visits the site or it is near the beginning of the season. The dates that designate a season varies according to different agencies (ie. July-June, October-September). Generally, this sensor type is used for real-time collection duration of hourly or event data.

**PRECIPITATION, TIPPING BUCKET**
A sensor type where the field measuring device uses a calibrated bucket that tips when full of precipitation. The amount of precipitation at which the device tips is usually 0.04 inches. There are some gages that tip at 0.01 inches. The value usually accumulates or gets larger until it is reset. A reset may occur if a technician visits the site or it is near the beginning of the season. The dates that designate a season varies according to different agencies (ie. July-June, October-September). Generally, this sensor type is used for real-time collection duration of hourly or event data.

**PRECIPITATION, INCREMENTAL**
A sensor type where the value is either calculated from real-time data or manually entered from an observers report. Generally, this sensor type is used for daily and monthly data.