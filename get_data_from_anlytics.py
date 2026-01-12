import requests
import json
import os
from token_gen import get_access_token

def analytics_data_keratoconus(workspace_id: str,view:str):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_dir = os.path.join(base_dir,"data","analyst_data")
    os.makedirs(file_dir,exist_ok=True)
    file_path=os.path.join(file_dir,"analytics_data_keratoconus.json")


    url_to_get_analytics = f"https://analyticsapi.zoho.com/restapi/v2/workspaces/{workspace_id}/views/{view}/data"

    headers = {
        "Authorization": f"Zoho-oauthtoken {get_access_token()}",
        "ZANALYTICS-ORGID": "659253158"
    }
    config = {
        "responseFormat":"json",
        "selectedColumns": ['Name',"Tel","OldOPno","DiagnosisR","DiagnosisL","Visitdate","Comments",'Consultant']
    }


    params = {
        "CONFIG": json.dumps(config)
    }

    response = requests.get(url_to_get_analytics, headers=headers,params=params)
    response_data = response.json()
    data = response_data.get('data',[])
    data_json= {"json":data}

    with open(file_path,'w') as f:
        json.dump(data_json,f,indent=3)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

    return data


def analytics_data_vision_therapy(workspace_id: str,view:str):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_dir = os.path.join(base_dir,"data","analyst_data")
    os.makedirs(file_dir,exist_ok=True)
    file_path=os.path.join(file_dir,"analytics_data_vision_therapy.json")


    url_to_get_analytics = f"https://analyticsapi.zoho.com/restapi/v2/workspaces/{workspace_id}/views/{view}/data"

    headers = {
        "Authorization": f"Zoho-oauthtoken {get_access_token()}",
        "ZANALYTICS-ORGID": "659253158"
    }
    config = {
        "responseFormat":"json",
        "selectedColumns": ['Name',"Tel","OldOPno","Visitdate",'DVvaR','DVvaL','Consultant']
    }


    params = {
        "CONFIG": json.dumps(config)
    }

    response = requests.get(url_to_get_analytics, headers=headers,params=params)
    response_data = response.json()
    data = response_data.get('data',[])
    data_json= {"json":data}

    with open(file_path,'w') as f:
        json.dump(data_json,f,indent=3)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

    return data




