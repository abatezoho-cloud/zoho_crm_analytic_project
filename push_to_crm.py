import requests
from config import settings
from token_gen import get_access_token

def pushing_crm(data: list,set_len=100):
 


    first_cut=0
    while True:

        last_cut=first_cut+set_len
        sub_data= data[first_cut:last_cut]
        print(f"legth={len(sub_data)},sliced_by start {first_cut} end {last_cut}",end='\n')



        url_to_push_kera = "https://www.zohoapis.com/crm/v8/keratoconus"

        header = {
             "Authorization":  f"Zoho-oauthtoken {get_access_token()}"
             }
        push_data = {"data":sub_data}
        
        resp= requests.post(url_to_push_kera,headers=header,json=push_data)
        print(resp.status_code)


        if len(sub_data)<set_len:
            break
        first_cut=last_cut



