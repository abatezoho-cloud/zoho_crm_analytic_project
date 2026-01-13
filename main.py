from get_data_from_anlytics import analytics_data_keratoconus,analytics_data_vision_therapy
from push_to_crm import pushing_crm
from transform import tranform_kera,tranform_visthe

if __name__=="__main__":
    #__________________________________________KERATOCONUS______________________________________________________

    #keratocounus Pmna -----------------------------------------------------------------------------------------
    data = analytics_data_keratoconus(workspace_id='1573373000039085753',view='1573373000111209050')
    if data is not None:
        trans_data=tranform_kera(table=data,catogry='Keratoconus',Branch='Perinthalmanna')
        pushing_crm(data=trans_data)
    #------------------------------------------------------------------------------------------------------------
    #
    #keratocounus clt -------------------------------------------------------------------------------------------
    data = analytics_data_keratoconus(workspace_id='1573373000039085753',view='1573373000111907469')
    if data is not None:
        trans_data=tranform_kera(table=data,catogry='Keratoconus',Branch='Calicut')
        pushing_crm(data=trans_data)
    #------------------------------------------------------------------------------------------------------------
    #
    #keratocounus Knr -------------------------------------------------------------------------------------------
    data = analytics_data_keratoconus(workspace_id='1573373000039085753',view='1573373000111907730')
    if data is not None:
        trans_data=tranform_kera(table=data,catogry='Keratoconus',Branch='Kannur')
        pushing_crm(data=trans_data)
    #------------------------------------------------------------------------------------------------------------
    #
    #keratocounus chn -------------------------------------------------------------------------------------------
    data = analytics_data_keratoconus(workspace_id='1573373000039085753',view='1573373000111907991')
    if data is not None:
        trans_data=tranform_kera(table=data,catogry='Keratoconus',Branch='Chennai')
        pushing_crm(data=trans_data)
    #------------------------------------------------------------------------------------------------------------

    #___________________________________________VISION_THERAPHY__________________________________________________

    #vision_therphy pmna-----------------------------------------------------------------------------------------
    data = analytics_data_vision_therapy(workspace_id='1573373000039085753',view='1573373000111704927')
    if data is not None:
        trans_data = tranform_visthe(data,catogry='Orthoptics',Branch='Perinthalmanna')
        pushing_crm(data=trans_data)
    #------------------------------------------------------------------------------------------------------------
    #
    #vision_therphy clt------------------------------------------------------------------------------------------
    data = analytics_data_vision_therapy(workspace_id='1573373000039085753',view='1573373000111956252')
    if data is not None:
        trans_data = tranform_visthe(data,catogry='Orthoptics',Branch='Calicut')
        pushing_crm(data=trans_data)
    #-------------------------------------------------------------------------------------------------------------
    #
    #vision_therphy knr-------------------------------------------------------------------------------------------
    data = analytics_data_vision_therapy(workspace_id='1573373000039085753',view='1573373000111956413')
    if data is not None:
        trans_data = tranform_visthe(data,catogry='Orthoptics',Branch='Kannur')
        pushing_crm(data=trans_data)
    #-------------------------------------------------------------------------------------------------------------
    #
    #vision_therphy chn-------------------------------------------------------------------------------------------
    data = analytics_data_vision_therapy(workspace_id='1573373000039085753',view='1573373000111956574')
    if data is not None:
        trans_data = tranform_visthe(data,catogry='Orthoptics',Branch='Chennai')
        pushing_crm(data=trans_data)
    #-------------------------------------------------------------------------------------------------------------

