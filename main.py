from datetime import date

import requests

service_number = "L76389"
trainStation = "crs:ROM"
appId = "c02b6c79"
date = date.today().strftime("%Y-%m-%d")
appKey = "f79fc709f32fa004762ca701f249b26c"
data_url = f"http://transportapi.com/v3/uk/train/service_timetables/{service_number}:{date}?live=true"
print(data_url)
