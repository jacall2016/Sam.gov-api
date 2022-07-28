import json
import requests
import pandas as pd
from pandas.io.json import json_normalize
import datetime


#makes an api request to the opportunities contract api and saves the result to data.json in a json format.
def SaveAPIdata():
    x = datetime.datetime.now()
    postedTo = x.strftime("%d") + "/" + x.strftime("%m") + "/" + x.strftime("%Y")
    days = datetime.timedelta(30)
    new_date = x - days
    postedFrom = new_date.strftime("%d") + "/" + new_date.strftime("%m") + "/" + new_date.strftime("%Y")
    limit = '5'
    ptype = 'a'
    deptName = 'general'
    key = 'Q6Sgtaf4kiZS77RajWOn5O6ylRfluoF8tQNpsUXZ'
    url_start = 'https://api.sam.gov/prod/opportunities/v2/search?limit='
    url = url_start + limit + '&api_key=' + key + '&postedFrom=' + postedFrom + '&postedTo=' + postedTo + '&ptype=' + ptype + '&deptname=' + deptName

    url = 'https://api.sam.gov/prod/opportunities/v2/search?limit=2&api_key=FGTJQrYpZfifUA65pNNstMFwAjifNDFQLzWkGo6O&postedFrom=01/01/2022&postedTo=07/15/2022&ptype=a&deptname=general'
    #url = 'https://api.sam.gov/prod/opportunities/v2/search?limit=5&api_key=Q6Sgtaf4kiZS77RajWOn5O6ylRfluoF8tQNpsUXZ&postedFrom=01/01/2021&postedTo=07/15/2022&ptype=a&deptname=general'
    #url = 'https:api.sam.gov/prod/opportunities/v2/search?limit=1&api_key=FGTJQrYpZfifUA65pNNstMFwAjifNDFQLzWkGo6O&postedFrom=25/05/2022&postedTo=24/06/2022&ptype=a&deptname=general'
    #yrl = http://https//:api.sam.gov/prod/opportunities/v2/search?limit=1&api_key=FGTJQrYpZfifUA65pNNstMFwAjifNDFQLzWkGo6O&postedFrom=25/05/2022&postedTo=24/06/2022&ptype=a&deptname=general?

    resp = requests.get(url)
    data = resp.text
    json_data = json.loads(data)
    with open('data.json','w') as json_file:
        json.dump(json_data, json_file)

#searches each of the names in the headerlist and only adds new names
def searchHeaderList(headerList,name):

    if name in headerList:
        pass
    else:
        headerList.append(name)

#creates a dataframe from the data in data.json 
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
                name = 'Title_Start'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'uiLink':
                name = 'uiLink'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'typeOfSetAsideDescription':
                name = 'Small Business Set-Aside'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'baseType':
                name = 'Type'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'responseDeadLine':
                name = 'Response Date'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'description':
                name = 'COMMENT or Additional Information'
                searchHeaderList(headerList,name)
                value = makeDescriptionURL(value)
                oppList[0].append(value)
            if attribute == 'naicsCodes':
                name = 'NaicsCodes'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'award':
                name = 'Award'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'officeAddress':
                name = 'OfficeAddress'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
            if attribute == 'pointOfContact':
                name = 'PointOfContact'
                searchHeaderList(headerList,name)
                oppList[0].append(value)
                
        datalist.append(oppList)
        num +=1

    data_frame_list = []
    df = pd.DataFrame()

    for oppurtunity in datalist:
        df = pd.DataFrame(oppurtunity)
        df.columns = headerList
        df = df[['DATE POSTED',
                 'AGENCY',
                 'Announcement Number',
                 'Title_Start',
                 'uiLink',
                 'Small Business Set-Aside',
                 'Type',
                 'Response Date',
                 'COMMENT or Additional Information',
                 'NaicsCodes',
                 'Award',
                 'OfficeAddress',
                 'PointOfContact']]
        df['Title'] = df['Title_Start'] + ": " + df['uiLink']

        del df['uiLink']
        del df['Title_Start']

        new_cols = ['DATE POSTED',
                 'AGENCY',
                 'Announcement Number',
                 'Title',
                 'Small Business Set-Aside',
                 'Type',
                 'Response Date',
                 'COMMENT or Additional Information',
                 'NaicsCodes',
                 'Award',
                 'OfficeAddress',
                 'PointOfContact']

        df=df[new_cols]
        #df = df[['DATE POSTED','AGENCY','Announcement Number','Title','Small Business Set-Aside','Pre-Sol Synopsis','RFP','BAA','Award S=Sole Source','Response Date','RELEASE','COMMENT or Additional Information','Reviewed','Status']]
        data_frame_list.append(df)

    df = pd.concat(data_frame_list)
    df = df.reset_index(drop=True)

    #print(df)

    df.to_csv('data_files\oppData.csv')
    df.to_excel('data_files\oppData.xlsx')
    df.to_json(r'data_files\New_Json_file.json')

def create_specific_data_frame():
    df = pd.read_csv ('oppData.csv')
    search_column = input("What column do you wish to search for ['DATE POSTED','AGENCY','Announcement Number','Title','Small Business Set-Aside','Type','Response Date','COMMENT or Additional Information','NaicsCodes','Award','OfficeAddress']: ")
    while search_column != 'DATE POSTED' or search_column != 'AGENCY' or search_column != 'Announcement Number' or search_column != 'Title' or search_column != 'Small Business Set-Aside' or search_column != 'Title' or search_column != 'Type' or search_column != 'Response Date' or search_column != 'COMMENT or Additional Information' or search_column != 'NaicsCodes' or search_column != 'Award' or search_column != 'OfficeAddress':
        print(search_column + ' is not a column')
        search_column = input("What column do you wish to search for ['DATE POSTED','AGENCY','Announcement Number','Title','Small Business Set-Aside','Type','Response Date','COMMENT or Additional Information','NaicsCodes','Award','OfficeAddress']: ")
    
    search_value = input("what value do you wish to search for: ")

    if df[search_column].value == search_value:
        new_df = df.append( df[search_column])

def pritifyJson():

    with open("data.json", "w") as json_file:
        a_json = json.load(json_file)
        json_formatted_str = json.dumps(a_json, indent=2)
        print(json_formatted_str)

def makeDescriptionURL(attribute):
    API_key = "api_key=FGTJQrYpZfifUA65pNNstMFwAjifNDFQLzWkGo6O"
    URL_List = attribute.split('?')
    new_URL = URL_List[0] + "?" + API_key + "&" + URL_List[1]

    return get_description(new_URL)

def get_description(new_URL):
    resp = requests.get(new_URL)
    data = resp.text
    json_data = json.loads(data)
    with open('description.json','w') as json_file:
        json.dump(json_data, json_file)

    a_file = open("description.json", "r")
    a_json = json.load(a_file)
    
    #if a_json['error']['code'] == 'OVER_RATE_LIMIT':
    #    data = "Over_Rate_Limit"
    #elif a_json['errorMessage'] == 'Description Not Found':
    #    data = 'Description Not Found'
    #else:
    #    data = a_json['description']

    return(data)

def main():
    #SaveAPIdata()
    createDataFrame()
    #makeDescriptionURL()
    #pritifyJson()

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
#Status -- df.opportunitiesData.

#"https://api.sam.gov/prod/opportunities/v1/noticedesc?api_key=Q6Sgtaf4kiZS77RajWOn5O6ylRfluoF8tQNpsUXZ&noticeid=ffe28b6704e24bcf9fed89a23bc045d1"
#"https://api.sam.gov/prod/opportunities/v1/noticedesc?api_key=Q6Sgtaf4kiZS77RajWOn5O6ylRfluoF8tQNpsUXZ&noticeid=ffc178d6dfb54b3fa08256b31f78a4a2"