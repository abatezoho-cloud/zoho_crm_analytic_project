from config import settings
from token_gen import get_access_token
from get_data_from_anlytics import analytics_data_keratoconus,analytics_data_vision_therapy
from push_to_crm import pushing_crm
from transform import tranform_kera,tranform_visthe

if __name__=="__main__":

    #keratocounus Pmna
    data = analytics_data_keratoconus(workspace_id='1573373000039085753',view='1573373000111209050')
    trans_data=tranform_kera(table=data,catogry='Keratoconus',Branch='Perinthalmanna')
    pushing_crm(data=trans_data)

    #vision_therphy pmna
    data = analytics_data_vision_therapy(workspace_id='1573373000039085753',view='1573373000111704927')
    trans_data = tranform_visthe(data,catogry='Orthoptics',Branch='Perinthalmanna')
    pushing_crm(data=trans_data)

    print(f'original data = {data[4:5]} length is {len(data)} type is {type(data)}')
    print(f'original data = {trans_data[4:5]} length is {len(trans_data)} type is {type(trans_data)}')