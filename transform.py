from get_data_from_anlytics import analytics_data_keratoconus
from pprint import pprint
from datetime import datetime
def tranform_kera(table:list,catogry:str,Branch :str):
    data=[]
    for item in table:

        dt = datetime.strptime(item.get("VisitDate"), "%d/%m/%Y %H:%M:%S")

        formatted_date = dt.isoformat()

        patient={
            "Name": item.get("Name"),
            "Visitdate": formatted_date,
            "MR_NO": item.get("OldOPno"),
            "DiagnosisR":item.get("DiagnosisR"),
            "DiagnosisL":item.get("DiagnosisL"),
            "commets":item.get("Comments"),
            "Number": item.get("Tel"),
            "Consultent":item.get('Consultant'),
            "Category":catogry,
            "Branch":Branch
        }

        data.append(patient)

        #pprint(patient,indent=3)

    return data


def tranform_visthe(table:list,catogry:str,Branch :str):
    data=[]
    for item in table:

        dt = datetime.strptime(item.get("VisitDate"), "%d/%m/%Y %H:%M:%S")

        formatted_date = dt.isoformat()

        patient={
            "Name": item.get("Name"),
            "Visitdate": formatted_date,
            "MR_NO": item.get("OldOPno"),
            "Number": item.get("Tel"),
            "Consultent":item.get('Consultant'),
            "DVvaL":item.get('DVvaL'),
            "DVvaR":item.get('DVvaR') ,
            "Category":catogry,
            "Branch":Branch
        }

        data.append(patient)

        #pprint(patient,indent=3)

    return data

        
