# import pandas as pandas
# import requests
# import json

# url = "https://archive-api.open-meteo.com/v1/archive"


#?latitude=9.769181&longitude=139.01135&start_date=2023-09-11&end_date=2023-09-25&hourly=temperature_2m,rain,snowfall&daily=temperature_2m_max,temperature_2m_min&timezone=America%2FNew_York


# headers = {
#     "Content-Type": "application/json"  # Set the content type to JSON
# }

# # Convert the payload to a JSON string
# payload_json = json.dumps(payload)

# response = requests.request("GET", url, headers=headers, data=payload_json)

# print(response)


import requests

url = "https://archive-api.open-meteo.com/v1/archive?latitude=9.769181&longitude=139.01135"


payload = {
    "latitude": 9.769181,
    "longitude": 139.01135,
    "start_date": "2019-12-01",
    "end_date": "2019-12-30",
    "hourly": ["temperature_2m","rain","snowfall"],
    "daily": ["temperature_2m_max","temperature_2m_min"],
    "timezone": "America/New_York"
}

headers = {}
payload = {}

response = requests.request("GET", url, headers=headers, payload=payload)

print(response.status_code,response.text)