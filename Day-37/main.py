from calendar import month

import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_USERNAME = "shashank1292"
PIXELA_TOKEN = "tsds23dcsSDlcs6dZfhSD"
PIXELA_GRAPH_ID = "graph1"
PIXELA_HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# new_user_param = {
#     "token": "tsds23dcsSDlcs6dZfhSD",
#     "username": "shashank1292",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(PIXELA_NEW_USER_ENDPOINT, json=new_user_param)

# PIXELA_NEW_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
# new_graph_headers = {
#     "X-USER-TOKEN": PIXELA_TOKEN
# }
# new_graph_param = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "momiji",
# }
# response = requests.post(PIXELA_NEW_GRAPH_ENDPOINT, headers=new_graph_headers, json=new_graph_param)

PIXELA_ADD_GRAPH_DATA_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"
date = datetime.now()
add_data_params = {
    "date": date.strftime("%Y%m%d"),
    "quantity": input("How many Km did you cycle today?")
}
response = requests.post(PIXELA_ADD_GRAPH_DATA_ENDPOINT, headers=PIXELA_HEADERS, json=add_data_params)

# date = datetime.now()
# PIXELA_EDIT_GRAPH_DATA_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{date.strftime('%Y%m%d')}"
# edit_data_params = {
#     "quantity": "100.0"
# }
# response = requests.put(PIXELA_EDIT_GRAPH_DATA_ENDPOINT, headers=PIXELA_HEADERS, json=edit_data_params)

# date = datetime.now()
# PIXELA_DELETE_GRAPH_DATA_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{date.strftime('%Y%m%d')}"
# response = requests.delete(PIXELA_DELETE_GRAPH_DATA_ENDPOINT, headers=PIXELA_HEADERS)
# print(response.text)