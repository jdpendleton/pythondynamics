from configFile import config
import requests
import json

orgname = config["OrgName"]
clientid = config['ApplicationID']
tenantid = config['DirectoryID']
secret = config['ClientSecret']

oauth2endpoint = f'https://login.microsoftonline.com/{tenantid}/oauth2/token'

crmorg = f'https://{orgname}.crm.dynamics.com'

tokenpost = {
    'client_id': clientid,
    'resource': crmorg,
    'client_secret': secret,
    'grant_type': 'client_credentials'
}

response = requests.post(oauth2endpoint, data=tokenpost)

data = response.json()

token = ''
try:
    token = data['access_token']
    print('Access token retrieved')
except KeyError:
    print('Could not get access token')

headers = {
    'Authorization': f'Bearer {token}',
    'OData-MaxVersion': '4.0',
    'OData-Version': '4.0',
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=utf-8',
    'Prefer': 'odata.maxpagesize=500',
    'Prefer': 'odata.include-annotations=OData.Community.Display.V1.FormattedValue',
    'Prefer': 'return=representation'
}

crmwebapi = f'https://{orgname}.api.crm.dynamics.com/api/data/v9.1'

query = 'contacts?$select=fullname,contactid'

response = requests.get(f'{crmwebapi}/{query}', headers=headers)

import pandas as pd
from pandas.io.json import json_normalize

data = response.json()
df = json_normalize(data['value'])
print(df.head(50))