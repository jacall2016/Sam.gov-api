import pandas as pd

import requests

from pandas.io.json import json_normalize

#makes an API request to the oppurtunity tracker and saves the data in a database
def APIRequest():
    url = 'https://api.sam.gov/prod/opportunities/v2/search?limit=10&api_key=FGTJQrYpZfifUA65pNNstMFwAjifNDFQLzWkGo6O&postedFrom=01/01/2022&postedTo=05/10/2022&ptype=a&deptname=general'
    resp = requests.get(url=url)

    df = json_normalize(resp.json())

    df.to_csv('data_files\oppurtunityTracker.csv')

def retriveCSV():
    df = pd.read_csv('data_files\oppurtunityTracker.csv')
    
    df['opportunitiesData'].str.split(',', expand=True)
    df = df.opportunitiesData
    df.to_csv('data_files\opp1.csv')
    #
    print(df[0])
    #print()
    #print(df[0])
    #createDatabase(df)

#creates a dataframe in the desired format
def createDatabase():
    df = pd.DataFrame()

    #df['oppurtunity'] = [opp.ooppurtunity.postedDate]]

    df = pd.DataFrame({'oppurtunity':{'DATE POSTED': [],
                            'AGENCY': [], 
                            'Announcement Number': [],
                            'Title':[],
                            'Small Business Set-Aside':[],
                            'Pre-Sol Synopsis':[],
                            'RFP':[],
                            'BAA':[],
                            'Award S=Sole Source':[],
                            'Response Date':[],
                            'RELEASE':[],
                            'COMMENT or Additional Information':[],
                            'Reviewed':[],
                            'Status':[]}})

    print(df)
    #df.to_csv('data_files\dataRepo.csv')
    #df.to_excel('data_files\dataRepo.xlsx')

def main():
    createDatabase()
    #retriveCSV()

main()

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
