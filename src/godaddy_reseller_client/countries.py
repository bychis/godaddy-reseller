

import requests


class countries:
    def __init__(self, base_url, key, secret):
        self.base_url = base_url
        self.key = key
        self.secret = secret
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'sso-key {}:{}'.format(key, secret)
        }

    def get_countries(self, market_id, region_type_id, region_name, fate, order):
        req_url = '{}/v1/countries?marketId={}&regionTypeId={}&regionName={}&sort={}&order={}'.format(
            self.base_url, market_id, region_type_id, region_name, fate, order)
        r = requests.get(req_url, headers=self.headers)
        return r.json()

    def get_country(self, country_key, market_id, fate, order):
        req_url = '{}/v1/countries/{}?marketId={}&sort={}&order={}'.format(
            self.base_url, country_key, market_id, fate, order)
        r = requests.get(req_url, headers=self.headers)
        return r.json()
