class certificate:
    def __init__(self, base_url, key, secret):
        self.base_url = base_url
        self.key = key
        self.secret = secret
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Auhthorization': 'sso-key {}:{}'.format(key,secret)
        }
    
