import requests
import json
class domains:
    def __init__(self, base_url, key, secret):
        self.key = key
        self.secret = secret
        self.base_url = base_url
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'sso-key {}:{}'.format(key,secret)
        }
    # Function to get a list of purchased domains for a shopper account (subaccount) 
    def get_shopper_domains(shopperId):
        req_url = '{}/v1/domains'.format(domains.base_url)
        headers_={**domains.headers,
                'shopperId':'{}'.format(shopperId)}
        
        response = requests.get(
            url=req_url,
            headers=headers_
        )
        return response.json()

    # Function to get legal agreements
    def retreive_legal_agreements(X_Market_Id,tlds,privacy,forTransfer):
        req_url = '{}/v1/domains/agreements?tlds={}&privacy={}&forTransfer={}'.format(
            domains.base_url,tlds,privacy,forTransfer
        )
        headers_={
            **domains.headers,
            'X-Market-Id': '{}'.format(X_Market_Id)
        } 
        response = requests.get(
            url=req_url,
            headers=headers_
        )
        return response

    # Function to check domain availibity for purchase
    def check_domain_availibity(domain):
        req_url = '{}/v1/domains/available?domain={}'.format(domains.base_url,domain)
        response = requests.get(
            url=req_url,
            headers=domains.headers)
        return response

    # Function to determine whether or not the specified domains are availabe for purchase
    def check_domains_availibity(domains_array):
        req_url = '{}/v1/domains/available'.format(domains.base_url)
        body = json.dumps(domains_array)
        response = requests.post(
            url=req_url,
            data=body,
            headers=domains.headers
        )
        return response
        
    # Function to purchase and register the specified domain
    def purchase_domain(shopperId,schema):
        req_url = '{}/v1/domains/purchase'.format(domains.base_url)
        headers_ = {
            **domains.headers,
            'X-Shopper-Id': '{}'.format(shopperId)
            }
        body = json.dumps(schema)
        response = requests.post(
            url=req_url,
            data=body,
            headers=headers_
        )
        return response
        
    # Function to get schema to be submitted for purchasing domain
    def get_schema_for_tld(tld):
        req_url = '{}/v1/domains/purchase/schema/{}'.format(
            domains.base_url,tld
        )
        response = requests.get(
            url=req_url,
            headers=domains.headers
        )
        return response.json()

    # Function to validate if the request body using domain purchase schema for the specified TLD
    def validate_schema(schema):
        req_url = '{}/v1/domains/purchase/validate'.format(domains.base_url)
        body = json.dumps(schema)
        response = requests.post(
            url=req_url,
            data=body,
            headers=domains.headers
        )
        return response
        
    # Funtion which suggest alternate domain names based on a seed domain, a set of keywords, or the shopper's purchase history
    def suggest_domains_to_shopper(shopperId,domain):
        req_url = '{}/v1/domains/suggest?querry={}'.format(
            domains.base_url,domain
        )
        headers_ = {
            **domains.headers,
            'X-Shopper-Id': '{}'.format(shopperId)
        }
        response = requests.get(
            url=req_url,
            headers=headers_
        )
        return response

    # Function to retreive a list of supported TLDs
    def get_supported_tlds():
        req_url = '{}/v1/domains/tlds'.format(domains.base_url)
        response = requests.get(
            url=req_url,
            headers=domains.headers
        )
        return response
        
    # Function to cancel a purchased domain
    def cancel_purchased_domain(domain):
        req_url = '{}/v1/domains/{}'.format(domains.base_url,domain)
        response = requests.delete(
            url=req_url,
            headers=domains.headers
        )
        return response
        
    # GET /v1/domains/{domain}
    # Function to get details of specified Domain
    def get_domain_details(domain,shopperId):
        req_url = '{}/v1/domains/{}'.format(domains.base_url,domain)
        headers_ = {
            **domains.headers,
            'X-Shopper-Id': '{}'.format(shopperId)
        }
        response = requests.get(
            url=req_url,
            headers=headers_
        )
        return response

    # Function to update details for the specified Domain
    def update_domain_details(domain,body,shopperId=None):
        req_url = '{}/v1/domains/{}'.format(domains.base_url,domain)
        data = json.dumps(body)
        headers_ = domains.headers
        if(shopperId != None):
            headers_ = {
                **domains.headers,
                'X-Shopper-Id': '{}'.format(shopperId)
            }
        response =requests.patch(
            url=req_url,
            data=data,
            headers=headers_
        )
        return response
        
    # Function to update domain contacts
    def update_domain_contacts(domain,contacts_body,shopperId=None):
        req_url = '{}/v1/domains/{}/contacts'.format(domains.base_url,domain)
        headers_ = domains.headers
        if(shopperId != None):
            headers_ = {
                **domains.headers,
                'X-Shopper-Id': '{}'.format(shopperId)
            }
        data = json.dumps(contacts_body)
        response = requests.patch(
            url=req_url,
            data=data,
            headers=headers_
        )
        return response
        
    # Function to submit privacy calcellation requets for the give domain
    def cancel_domain_privacy(domain,shopperId):
        req_url = '{}/v1/domains/{}/privacy'.format(domains.base_url,domain)
        headers_ = {
            **domains.headers,
            'X-Shopper-Id': '{}'.format(shopperId)
        }
        response = requests.delete(
            url=req_url,
            headers=headers_
        )
        return response
        
    # Function to purchase privacy for a specified domain
    def purchase_domain_privacy(domain,shopperId,purchasing_options_body):
        req_url = '{}/v1/domains/{}/privacy/purchase'.format(
            domains.base_url,domain
        )
        headers_ = {
            **domains.headers,
            'X-Shopper-Id': '{}'.format(shopperId)
        }
        data = json.dumps(purchasing_options_body)
        response = requests.post(
            url=req_url,
            data=data,
            headers=headers_
        )
        return response
        
    # Function to add the specified DNS Records to the specified Domain
    def add_records(domain,shopperId,records_body):
        req_url = '{}/v1/domains/{}/records'.format(domains.base_url,domain)
        headers_ = {
            **domains.headers,
            'X-Shopper-Id': '{}'.format(shopperId)
        }
        data = json.dumps(records_body)
        response = requests.patch(
            url=req_url,
            data=data,
            headers=headers_
        )
        return response
        
    # Function to replace all DNS Records for the specified domain
    def replace_records(domain,shopperId,records_body):
        req_url = '{}/v1/domains/{}/records'.format(domains.base_url,domain)
        headers_ = {
            **domains.headers,
            'X-Shopper-Id': '{}'.format(shopperId)
        }
        data = json.dumps(records_body)
        response = requests.put(
            url=req_url,
            data=data,
            headers=headers_
        )
        return response
        
    # Function to get DNS Records for the specified domain, optionally with the specified Type and/or Name
    def get_dns_records(domain,shopperId,type=None,name=None,offset=None,limit=None):
        req_url = '{}/v1/domains/{}/records'.format(domains.base_url,domain)
        # Handling optional argument: Type and/or Name
        if (type != None):
            req_url = req_url + '/{}'.format(type)
            if (name != None):
                req_url = req_url + '/{}'.format(name)
            else: 
                pass
        else:
            pass
        # Handling pagination
        if (offset != None & limit != None):
            req_url = req_url + '?offset={}&limit={}'.format(offset,limit)
        else:
            pass
        # Handling the X-Shopper-Id header
        headers_ = {
            **domains.headers,
            'X-Shopper-Id': '{}'.format(shopperId)
        }
        # Requesting api
        response = requests.get(
            url=req_url,
            headers=headers_
        )
        return response
        
    # Function to replace all DNS record for the specified Domain with the specified Type and Name
    def replace_dns_records(domain,shopperdId,type,name,records_body):
        req_url = '{}/v1/domains/{}/records/{}/{}'.format(
            domains.base_url,domain,type,name
        )
        data = json.dumps(records_body)
        headers_ = {
            **domains.headers,
            'X-Shopper-Id': '{}'.format(shopperdId)
        }
        response = requests.put(
            url=req_url,
            data=data,
            headers=headers_
        )
        return response
        
    # Function to delete all DNS Records for the specified Domain with the specified Type and Name
    def delete_dns_record(domain,shopperId,type,name):
        req_url = '{}/v1/domains/{}/records/{}/{}'.format(
            domains.base_url,domain,type,name
        )
        headers_ = {
            **domains.headers,
            'X-Shopper-Id': '{}'.format(shopperId)
        }
        response = requests.delete(
            url=req_url,
            headers=headers_
        )
        return response
        
    # Function to replace all DNS records for the specified domain with the specified Type
    def replace_dns_records(shopperId,domain,type,records_body):
        req_url = '{}/v1/domains/{}/records/{}'.format(
            domains.base_url,domain,type
        )
        headers_ = {
            **domains.headers,
            'X-Shopper-Id': '{}'.format(shopperId)
        }
        data = json.dumps(records_body)
        response = requests.put(
            url=req_url,
            data=data,
            headers=headers_
        )
        return response
        
    # Function to renew the specified Domain
    def renew_domain(shopperId,domain,period=1):
        req_url = '{}/v1/domains/{}/renew'.format(domains.base_url,domain)
        headers_ = {
            **domains.headers,
            'X-Shopper-Id': '{}'.format(shopperId)
        }
        body = { "period": period }
        data = json.dumps(body)
        response = requests.post(
            url=req_url,
            data=data,
            headers=headers_
        )
        return response