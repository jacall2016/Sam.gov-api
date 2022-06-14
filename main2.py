import csv
import requests
import pandas as pd

url = 'https://api.sam.gov/prod/opportunities/v2/search?limit=10&api_key=FGTJQrYpZfifUA65pNNstMFwAjifNDFQLzWkGo6O&postedFrom=01/01/2022&postedTo=05/10/2022&ptype=a&deptname=general'
df = pd.read_json(r'https://api.sam.gov/prod/opportunities/v2/search?limit=10&api_key=FGTJQrYpZfifUA65pNNstMFwAjifNDFQLzWkGo6O&postedFrom=01/01/2022&postedTo=05/10/2022&ptype=a&deptname=general')

df.to_csv(r'data_files\oppurtunityTracker.csv', index = None)

