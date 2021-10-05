import json
import requests

class shoppers:
    def __init__(self, base_url, key, secret):
        self.base_url = base_url
        self.key = key
        self.secret = secret
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'sso-key {}:{}'.format(key, secret)
        }
        
    def create_subaccount(self, email, nameFirst, nameLast, password):
        req_url = '{}/v1/shoppers/subaccount'.format(shoppers.base_url)
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
            headers=shoppers.headers)
        return response

    # Function to get shopper details
    def get_shopper_details(self, shopperId):
        req_url = '{}/v1/shoppers/{}'.format(shoppers.base_url, shopperId)
        response = requests.get(
            url=req_url,
            headers=shoppers.headers,
        )
        return response

    # Function to update the subaccount shopper details
    def update_shopper_details(self, shopperId, email, externalId, marketId, nameFirst, nameLast):
        req_url = '{}/v1/shoppers/{}'.format(shoppers.base_url, shopperId)
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
            headers=shoppers.headers,
            data=data
        )
        return response

    # Function to delete subaccount or shopper (works only on prod, non in sandbox !)
    def delete_shopper(self, shopperId, auditClientIp):
        req_url = '{}/v1/shoppers/{}?auditClientIp={}'.format(
            shoppers.base_url, shopperId, auditClientIp)
        response = requests.delete(
            url=req_url,
            headers=shoppers.headers
        )
        return response

    # Function to get subaccount details
    def get_shopper_status(self, shopperId, auditClientIp):
        req_url = '{}/v1/shoppers/{}/status?auditClientIp={}'.format(
            shoppers.base_url, shopperId, auditClientIp
        )
        response = requests.get(
            url=req_url,
            headers=shoppers.headers
        )
        return response

    # Function to change password of shopper account
    def change_subaccount_password(self, shopperId, password):
        req_url = '{}/v1/shoppers/{}/factors/password'.format(
            shoppers.base_url, shopperId
        )
        body = {
            'secret': '{}'.format(password)
        }
        data = json.dumps(body)
        response = requests.put(
            url=req_url,
            data=data,
            headers=shoppers.headers
        )
        return response
