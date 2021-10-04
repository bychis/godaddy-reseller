from shoppers import create_subaccount
from domains import retreive_legal_agreements,check_domain_availibity, purchase_domain, get_schema_for_tld, get_domain_details
from tld import get_tld
from schema import *
import json
from datetime import datetime
if __name__ == '__main__':
    # domain name to purchase
    domain = 'khousabrina.biz'
    # getting the schema for tld just to  check agreements keys as i know there is two values right?
    # DNPA and DNTA ?? but it wont work unless i use DNRA instead
    # schema = get_schema_for_tld(get_tld('https://www.{}'.format(domain)))
    # print(schema)
    # creating the shopper account to be able to make requests with shopperId in the header
    shopper_account = create_subaccount('ismael@gmail.dz','foofoo','barbar','password1234+')
    if shopper_account.status_code != 201:
        print('shopper account created successfuly')
    else:
        print('error creating subaccount')
    # # Checking domain availability
    domain_availibity = check_domain_availibity(domain)
    
    if domain_availibity.json()['available'] == True:
        # Here comes were i had to use DNRA instead of the two values returned by the get_schema_for_tld
        keys = ['DNRA']
        
        # getting the timestamp as the requested regex format 
        agreed_at = str(datetime.utcnow().isoformat())[:-3]+'Z'
        print(agreed_at)
    ## Creating schema body    
    consent = create_schema_consent_body(agreed_at,requests.get('https://api.ipify.org').text,keys)
    contact_address_mailing = create_schema_contact_address_mailing('cite zed','site prr','Mostaganem','DZ',27000,'Mostaganem')
    contact = create_schema_contact_body(contact_address_mailing,'bychis6@gmail.com','+213.772047458','devops','chemsou','ismael','name','neofintech','+213.775858598')
    body_schema = create_schema_body(consent,domain,contact,contact,contact,contact)
    print(body_schema)
    print('******************************************')
    # validating schema this is were i got 200 OK 
    is_valid_schema = validate_schema(schema=body_schema)
    if(is_valid_schema.status_code == 200):
        print('schema is valid')
        with open('data.json', 'w') as f:
            json.dump(body_schema, f)
        print('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
        print(shopper_account.json()['shopperId'])
        print('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')

        schema_body = json.dumps(body_schema)
        purchase = purchase_domain(shopper_account.json().get('shopperId'),body_schema)
        print(purchase.json())
        print(purchase.headers)
    else:
        print('domain availability check failed')