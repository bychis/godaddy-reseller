from shoppers import create_subaccount
from domains import retreive_legal_agreements,check_domain_availibity, purchase_domain, get_schema_for_tld, get_domain_details
from tld import get_tld
from schema import *
import json
from datetime import datetime
if __name__ == '__main__':
    domain = 'khosabrina.biz'
    schema = get_schema_for_tld(get_tld('https://www.{}'.format(domain)))
    print(schema)
    domain = 'skimpou.com'
    # # Create shopper account
    shopper_account = create_subaccount('niaha@niaho.nh','niaho','naihi','password1234+')
    if 'error' not in shopper_account:
        print('shopper account created successfuly')
    else:
        print('error creating subaccount')
    # # Checking domain availability
    domain_availibity = check_domain_availibity(domain)
    # print(domain_availibity)
    # print('******************')
    # print(type(domain_availibity))
    # if 'error' not in domain_availibity:
    if domain_availibity['available'] == True:
        keys = ['DNRA']
        print(keys)
        dt = str(datetime.now().isoformat())[:-3]+'Z'
        print(dt)
        
    consent = create_schema_consent_body(dt,requests.get('https://api.ipify.org').text,keys)
    contact_address_mailing = create_schema_contact_address_mailing('cite zed','site prr','Mostaganem','DZ',27000,'Mostaganem')
    contact = create_schema_contact_body(contact_address_mailing,'bychis6@gmail.com','+213.772047458','devops','chemsou','ismael','name','neofintech','+213.775858598')
    body_schema = create_schema_body(consent,'kiosotot.biz',contact,contact,contact,contact)
    print(body_schema)
    print('******************************************')
    print(validate_schema(schema=body_schema))
    if 'error' not in schema:
        schema_body = json.dumps(body_schema)
        purchase = purchase_domain(shopper_account.get('shopperId'),body_schema)
        print(purchase)
    else:
        print('domain availability check failed')