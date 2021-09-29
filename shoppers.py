import json
import requests
from domains import *
# Credentials for sandbox of goddady reseller api
base_url = 'https://api.ote-godaddy.com'
key = 'UzQxLikn_B6N4aNAciZV7smWHj2d1WC'
secret = 'B6N7swL5PzVCXKeh2VQyMn'

# You must ask api@godaddy.com for testing api keys or just use sandbox keys in reseller.godaddy.com/docs#/
# And then place them in all of your request headers
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'sso-key {}:{}'.format(key, secret)
}

# Function to create a sub account (shopper) from a reseller account


def create_subaccount(email, nameFirst, nameLast, password):
    req_url = '{}/v1/shoppers/subaccount'.format(base_url)
    data = {
        'email': email,
        'externalId': 0,
        'marketId': 'en-US',
        'nameFirst': nameFirst,
        'nameLast': nameLast,
        'password': password
    }
    body = json.dumps(data)
    response = requests.post(
        url=req_url,
        data=body,
        headers=headers)
    return response

# Function to get shopper details


def get_shopper_details(shopperId):
    req_url = '{}/v1/shoppers/{}'.format(base_url, shopperId)
    response = requests.get(
        url=req_url,
        headers=headers,
    )
    return response

# Function to update the subaccount shopper details


def update_shopper_details(shopperId, email, externalId, marketId, nameFirst, nameLast):
    req_url = '{}/v1/shoppers/{}'.format(base_url, shopperId)
    body = {
        'email': '{}'.format(email),
        'externalId': externalId,
        'marketId': '{}'.format(marketId),
        'nameFirst': '{}'.format(nameFirst),
        'nameLast': '{}'.format(nameLast)
    }
    data = json.dumps(body)
    response = requests.post(
        url=req_url,
        headers=headers,
        data=data
    )
    return response

# Function to delete subaccount or shopper (works only on prod, non in sandbox !)


def delete_shopper(shopperId, auditClientIp):
    req_url = '{}/v1/shoppers/{}?auditClientIp={}'.format(
        base_url, shopperId, auditClientIp)
    response = requests.delete(
        url=req_url,
        headers=headers
    )
    return response

# Function to get subaccount details


def get_shopper_status(shopperId, auditClientIp):
    req_url = '{}/v1/shoppers/{}/status?auditClientIp={}'.format(
        base_url, shopperId, auditClientIp
    )
    response = requests.get(
        url=req_url,
        headers=headers
    )
    return response

# Function to change password of shopper account


def change_subaccount_password(shopperId, password):
    req_url = '{}/v1/shoppers/{}/factors/password'.format(
        base_url, shopperId
    )
    body = {
        'secret': '{}'.format(password)
    }
    data = json.dumps(body)
    response = requests.put(
        url=req_url,
        data=data,
        headers=headers
    )
    return response
