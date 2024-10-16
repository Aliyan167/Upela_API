import json

import requests
from django.shortcuts import render

from core.settings import LOGIN, CREDENTIALS, API


# Create your views here.
def index(request):
    return render(request, 'shipping/index.html')


def rates(request):
    if request.method == "POST":
        url = "https://api.upela.com/api/v3/rate/"

        payload = json.dumps({
            "account": {
                "login": LOGIN,
                "password": CREDENTIALS
            },
            "ship_from": {
                "country_code": "us",
                "postcode": "60290",
                "city": "Chicago",
                "pro": 1
            },
            "ship_to": {
                "country_code": "de",
                "postcode": "10117",
                "city": "Berlin",
                "pro": 1
            },
            "parcels": [
                {
                    "number": 2,
                    "weight": 1,
                    "x": 10,
                    "y": 10,
                    "z": 10
                },
                {
                    "number": 1,
                    "weight": 2,
                    "x": 10,
                    "y": 10,
                    "z": 10
                }
            ],
            "shipment_date": "2024-09-15",
            "unit": "fr",
            "selection": "all"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return render(request, 'shipping/response.html', {'response': response.text})
    return render(request, 'shipping/rates.html')


def login(request):
    url = "https://api.upela.com/api/v3/login/"

    payload = json.dumps({
        "account": {
            "login": LOGIN,
            "password": CREDENTIALS
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return render(request, 'shipping/response.html', {'response': response.text})


def create_store(request):
    url = "https://api.upela.com/api/v3/create_store/"
    data = {
        'store': {
            'store_name': "STORENAME",
            'address': "St 1, Northren Hemisphere",
            'zip_code': "zip_code",
            'city': "city",
            'country': "country",
            'phone': "phone"
        }
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, headers=headers, data=data)
    print(response.text)
    return render(request, 'shipping/response.html', {'response': response.text})


def get_payments(request):
    url = "https://api.upela.com/api/v3/get_payments/"

    payload = json.dumps({
        "account": {
            "login": LOGIN,
            "password": CREDENTIALS
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return render(request, 'shipping/response.html', {'response': response.text})


def select_offer(request):
    url = "https://api.upela.com/api/v3/select_offer/"

    payload = json.dumps({
        "account": {
            "login": LOGIN,
            "password": CREDENTIALS
        },
        "shipment_id": 2349548,
        "offer_id": 18514030
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return render(request, 'shipping/response.html', {'response': response.text})


def cancel_ship(request):
    url = "https://api.upela.com/api/v3/select_offer/"

    if request.method == 'POST':
        try:
            # Extracting shipment_id from the request body
            data = json.loads(request.body)
            shipment_id = data.get("shipment_id")

            # Building the payload for the Cancel Pickup API request
            payload = json.dumps({
                "account": {
                    "login": LOGIN,
                    "password": CREDENTIALS
                },
                "shipment_id": shipment_id
            })

            headers = {
                'Content-Type': 'application/json'
            }

            # Send the request to the external Cancel Pickup API
            response = requests.post(url, headers=headers, data=payload)

            # Render the response in the response.html template
            return render(request, 'shipping/response.html', {'response': response.text})

        except json.JSONDecodeError:
            return render(request, 'shipping/response.html', {'response': 'Invalid JSON request body'})

    # For non-POST requests, render an error message
    return render(request, 'shipping/response.html', {'response': 'Invalid request method. Only POST is allowed.'})
