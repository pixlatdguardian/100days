import requests
import datetime

user = "username"
token = "token"
pix_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": token,
}

user_params = {
    "token": token,
    "username": user,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pix_endpoint}/{user}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Workout",
    "unit": "minutes",
    "type": "float",
    "color": "sora"
}

graph1 = f"{pix_endpoint}/{user}/graphs/graph1"

date = datetime.datetime.now()
formatted_date = date.strftime('%Y%m%d')

graph_post = {
    "date": formatted_date,
    "quantity": "1",
}

post_today = requests.post(url=graph1, headers=headers, json=graph_post)
