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

    def get_certificate(self):
        pass

    def get_certificate_actions(self):
        pass

    def get_certificate_callback(self):
        pass

    def get_customer_certificate_details(self):
        pass

    def get_customer_certificates(self):
        pass

    def get_detailed_info_for_supplied_domain(self):
        pass

    def get_domain_verification_status(self):
        pass

    def get_download(self):
        pass

    def get_email_history(self):
        pass

    def get_external_account_binding_for_customer(self):
        pass

    def get_site_seal(self):
        pass
