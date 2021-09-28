import requests
import json

# Credentials for sandbox of goddady reseller api
base_url='https://api.ote-godaddy.com'
key='UzQxLikn_B6N4aNAciZV7smWHj2d1WC'
secret='B6N7swL5PzVCXKeh2VQyMn'

# You must ask api@godaddy.com for testing api keys or just use sandbox keys in reseller.godaddy.com
# And then place them in all of your request headers
headers= {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'sso-key {}:{}'.format(key,secret)
}

def retreive_countries():
    print('yes')