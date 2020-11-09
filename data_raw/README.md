# data_raw
This directory contains all the raw data sources used in the project. Here is where each file came from:

* `CDEC_Stations.csv`: List of all weather stations and what sensors are used at that station. Sourced from [California Data Exchange Center](https://cdec.water.ca.gov/webgis/?appid=cdecstation) and clicking to download all station data.
* `wildfires/*.json`: Set of json objects representing all the wildfires in California from 2003 to 2020. Sourced from [CalFire](https://www.fire.ca.gov/umbraco/Api/IncidentApi/GetIncidents?year=2019) where you can update the year query parameter to see data from other years.
* `airquality/*.json`: Set of json objects representing all air quality readings from California for each year from 2003 to 2020. Sourced from [EPA](https://aqs.epa.gov/aqsweb/documents/data_api.html#sample).