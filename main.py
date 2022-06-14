import json
import requests
import pandas as pd
from pandas.io.json import json_normalize


def SaveAPIdata():
    #url = 'https://api.sam.gov/prod/opportunities/v2/search?limit=10&api_key=FGTJQrYpZfifUA65pNNstMFwAjifNDFQLzWkGo6O&postedFrom=01/01/2022&postedTo=05/10/2022&ptype=a&deptname=general'

    #url = 'https://api.sam.gov/prod/opportunities/v2/search?limit=1&api_key=Q6Sgtaf4kiZS77RajWOn5O6ylRfluoF8tQNpsUXZ&postedFrom=01/01/2021&postedTo=05/10/2021&ptype=a&deptname=general'

    resp = requests.get('https://api.sam.gov/prod/opportunities/v2/search?limit=10&api_key=Q6Sgtaf4kiZS77RajWOn5O6ylRfluoF8tQNpsUXZ&postedFrom=01/01/2022&postedTo=06/13/2022&ptype=a&deptname=general')
    data = resp.text
    json_data = json.loads(data)
    with open('data.json','w') as json_file:
        print('hi')
        json.dump(json_data, json_file)
    print(json_data)
    #writeFile = open('data.json','w')
    #writeFile.write(resp)
    #writeFile.close()


def searchHeaderList(headerList,name):

    if name in headerList:
        pass
    else:
        headerList.append(name)

def createDataFrame():

    a_file = open("data.json", "r")
    a_json = json.load(a_file)
    num = 0

    headerList = []
    oppList = []
    datalist = []
    for i in a_json['opportunitiesData']:
        oppList = []
        opp = []

        oppList.append(opp)
        for attribute, value in i.items():
            if attribute == 'postedDate':
                name = 'DATE POSTED'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'fullParentPathName':
                name = 'AGENCY'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'solicitationNumber':
                name = 'Announcement Number'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'title':
                name = 'Title'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'typeOfSetAsideDescription':
                name = 'Small Business Set-Aside'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'baseType':
                name = 'Pre-Sol Synopsis'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'noticeId':
                name = 'RFP'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'noticeId':
                name = 'BAA'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'noticeId':
                name = 'Award S=Sole Source'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'responseDeadLine':
                name = 'Response Date'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'noticeId':
                name = 'RELEASE'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'noticeId':
                name = 'COMMENT or Additional Information'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'noticeId':
                name = 'Reviewed'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'active':
                name = 'Status'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
        datalist.append(oppList)
        #print(oppList)
        #print()
        num +=1

    data_frame_list = []
    df = pd.DataFrame()

    for oppurtunity in datalist:

        df = pd.DataFrame(oppurtunity)
        df.columns = headerList
        df = df[['DATE POSTED','AGENCY','Announcement Number','Title','Small Business Set-Aside','Pre-Sol Synopsis','RFP','BAA','Award S=Sole Source','Response Date','RELEASE','COMMENT or Additional Information','Reviewed','Status']]
        data_frame_list.append(df)

    #print(new_list)

    df = pd.concat(data_frame_list)
    print(df)
    df.to_csv('data_files\oppData.csv')
    df.to_excel('data_files\oppData.xlsx')

def main():
    #SaveAPIdata()
    createDataFrame()

main()

#--formate of the list
#DATE POSTED --- df.opportunitiesData.postedDate
#AGENCY --- df.opportunitiesData.fullParentPathName*
#Announcement Number --- df.opportunitiesData.solicitationNumber*
#Title --- df.opportunitiesData.title
#Small Business Set-Aside --- df.opportunitiesData.typeOfSetAsideDescription*
#Pre-Sol Synopsis --- df.opportunitiesData.baseType*
#RFP --- df.opportunitiesData.
#BAA --- df.opportunitiesData.
#Award S=Sole Source --- df.opportunitiesData.
#Response Date --- df.opportunitiesData.responseDeadLine*
#RELEASE --- df.opportunitiesData.
#COMMENT or Additional Information --- df.opportunitiesData.
#Reviewed --- df.opportunitiesData.
#Status --- df.opportunitiesData.active*



#DATE POSTED --- df.opportunitiesData.postedDate
#Title --- df.opportunitiesData.title

#AGENCY --- df.opportunitiesData.fullParentPathName*
#Announcement Number --- df.opportunitiesData.solicitationNumber*
#Small Business Set-Aside --- df.opportunitiesData.typeOfSetAsideDescription*
#Pre-Sol Synopsis --- df.opportunitiesData.baseType*
#Response Date --- df.opportunitiesData.responseDeadLine*
#Status --- df.opportunitiesData.active*

#RFP --- df.opportunitiesData.
#BAA --- df.opportunitiesData.
#Award S=Sole Source --- df.opportunitiesData.
#RELEASE --- df.opportunitiesData.
#COMMENT or Additional Information --- df.opportunitiesData.
#Reviewed --- df.opportunitiesData.
