import requests


class certificate:
    def __init__(self, base_url, key, secret):
        self.base_url = base_url
        self.key = key
        self.secret = secret
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Auhthorization': 'sso-key {}:{}'.format(key, secret)
        }

    def get_certificate(self, certificate_id):
        req_url = '{}/v1/certificates/{}'.format(self.base_url, certificate_id)
        response = requests.get(
            url=req_url,
            headers=self.headers
        )
        return response.json()

    def get_certificate_actions(self, certificate_id):
        req_url = '{}/v1/certificates/{}/actions'.format(
            self.base_url, certificate_id)
        response = requests.get(
            url=req_url,
            headers=self.headers
        )
        return response.json()

    def get_certificate_callback(self, certificate_id):
        req_url = '{}/v1/certificates/{}/callback'.format(
            self.base_url, certificate_id)
        response = requests.get(
            url=req_url,
            headers=self.headers
        )
        return response.json()

    def get_customer_certificate_details(self, customer_id, certificate_id):
        req_url = '{}/v2/customers/{}/certificates/{}'.format(
            self.base_url, customer_id, certificate_id)
        response = requests.get(
            url=req_url,
            headers=self.headers
        )
        return response.json()

    def get_customer_certificates(self, customer_id, offset=0, limit=100):
        req_url = '{}/v2/customers/{}/certificates?offset={}&limit={}'.format(
            self.base_url, customer_id, offset, limit)
        response = requests.get(
            url=req_url,
            headers=self.headers
        )
        return response.json()

    def get_detailed_info_for_supplied_domain(self, customer_id, certificate_id, domain):
        req_url = '{}/v2/customers/{}/certificates/{}/domainVerifications/{}'.format(
            self.base_url, customer_id, certificate_id, domain)
        response = requests.get(
            url=req_url,
            headers=self.headers
        )
        return response.json()

    def get_domain_verification_status(self, customer_id, certificate_id):
        req_url = '{}/v2/customers/{}/certificates/{}/domainVerifications'.format(
            self.base_url, customer_id, certificate_id)
        response = requests.get(
            url=req_url,
            headers=self.headers
        )
        return response.json()

    def get_download(self, certificate_id):
        req_url = '{}/v1/certificates/{}/download'.format(
            self.base_url, certificate_id)
        response = requests.get(
            url=req_url,
            headers=self.headers
        )
        return response.json()

    def get_email_history(self, certificate_id):
        req_url = '{}/v1/certificates/{}/email/history'.format(
            self.base_url, certificate_id)
        response = requests.get(
            url=req_url,
            headers=self.headers
        )
        return response.json()

    def get_external_account_binding_for_customer(self, customer_id):
        req_url = '{}/v2/customers/{}/cartificates/acme/externalAccountBindings'.format(
            self.base_url, customer_id)
        response = requests.get(
            url=req_url,
            headers=self.headers
        )
        return response.json()

    def get_site_seal(self, certificate_id, theme, local):
        req_url = '{}/v1/certificates/{}/siteSeal?theme={}&local={}'.format(
            self.base_url, certificate_id, theme, local)
        response = requests.get(
            url=req_url,
            headers=self.headers
        )
        return response.json()

    def post_certificate(self, certificate_create, x_market_id):
        req_url = '{}/v1/certificates'.format(self.base_url)
        response = requests.post(
            url=req_url,
            headers=self.headers,
            json=certificate_create,
            params={'x-market-id': x_market_id}
        )
        return response.json()

    def post_alternate_email(self, certificate_id, email_id, email_address):
        req_url = '{}/v1/certificates/{}/email/{}/resend/{}'.format(
            self.base_url, certificate_id, email_id, email_address)
        response = requests.post(
            url=req_url,
            headers=self.headers
        )
        return response.json()

    def post_cancel(self, certificate_id):
        req_url = '{}/v1/certificates/{}/cancel'.format(
            self.base_url, certificate_id)
        response = requests.post(
            url=req_url,
            headers=self.headers
        )
        return response.json()

    def post_check_domain_control(self, certificate_id):
        req_url = '{}/v1/certificates/{}/verifyDomainControl'.format(
            self.base_url, certificate_id)
        response = requests.post(
            url=req_url,
            headers=self.headers
        )
        return response.json()

    def post_reissue(self, certificate_id, reissue_create):
        req_url = '{}/v1/certificates/{}/reissue'.format(
            self.base_url, certificate_id)
        response = requests.post(
            url=req_url,
            headers=self.headers,
            json=reissue_create
        )
        return response.json()

    def post_renew(self, certificate_id, renew_create):
        req_url = '{}/v1/certificates/{}/renew'.format(
            self.base_url, certificate_id)
        response = requests.post(
            url=req_url,
            headers=self.headers,
            json=renew_create
        )
        return response.json()

    def post_resend_email(self, certificate_id, email_id):
        req_url = '{}/v1/certificates/{}/email/{}/resend'.format(
            self.base_url, certificate_id, email_id)
        response = requests.post(
            url=req_url,
            headers=self.headers
        )
        return response.json()

    def post_resend_email_to_email(self, certificate_id, email_id, email_address):
        req_url = '{}/v1/certificates/{}/email/{}/resend/{}'.format(
            self.base_url, certificate_id, email_id, email_address)
        response = requests.post(
            url=req_url,
            headers=self.headers
        )
        return response.json()

    def post_revoke(self, certificate_id, revoke_create):
        req_url = '{}/v1/certificates/{}/revoke'.format(
            self.base_url, certificate_id)
        response = requests.post(
            url=req_url,
            headers=self.headers,
            json=revoke_create
        )
        return response.json()

    def post_validate_certificate(self, certificate_create, x_market_id):
        req_url = '{}/v1/certificates/validate'.format(self.base_url)
        response = requests.post(
            url=req_url,
            headers=self.headers,
            json=certificate_create,
            params={'x-market-id': x_market_id}
        )
        return response.json()

    def delete_certificate_callback(self, certificate_id):
        req_url = '{}/v1/certificates/{}/callback'.format(
            self.base_url, certificate_id)
        response = requests.delete(
            url=req_url,
            headers=self.headers
        )
        return response.json()

    def put_certificate_callback(self, certificate_id, callback_url):
        req_url = '{}/v1/certificates/{}/callback?callbackUrl={}'.format(
            self.base_url, certificate_id, callback_url)
        response = requests.put(
            url=req_url,
            headers=self.headers
        )
        return response.json()
