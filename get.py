import os
import requests
import json
import sys

# Grab the query
args = sys.argv[1]

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

querystring = {
    'ipAddress': args,
}

headers = {
    'Accept': 'application/json',
    'Key': os.getenv('API')
}

response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# Formatted output
decodedResponse = json.loads(response.text)
finalResponse = json.dumps(decodedResponse, sort_keys=True, indent=4)

json_dict = json.loads(finalResponse)
json_list = json_dict['data']
#for key, value in json_list.items():
#    print(value)
result = {"items": [
    {
        "type": "file",
        "title": "Abuse confidencescore: " + str(json_list['abuseConfidenceScore']) + "%" ,
        "subtitle": "Press enter to copy to clipboard",
        "arg": "Abuse confidencescore: " + str(json_list['abuseConfidenceScore']) + "%",
        "icon": {
            "path": "icon.png"
        }
    },
    {
        "type": "file",
        "title": "Country Code: " + str(json_list['countryCode']),
        "subtitle": "Press enter to copy to clipboard",
        "arg": "Country Code: " + str(json_list['countryCode']),
        "icon": {
            "path": "icon.png"
        }
    },
    {
        "type": "file",
        "title": "Domain: " + str(json_list['domain']),
        "subtitle": "Press enter to copy to clipboard",
        "arg": "Domain: " + str(json_list['domain']),
        "icon": {
            "path": "icon.png"
        }
    },
    {
        "type": "file",
        "title": "is whitelisted: " + str(json_list['isWhitelisted']),
        "subtitle": "Press enter to copy to clipboard",
        "arg": "is whitelisted: " + str(json_list['isWhitelisted']),
        "icon": {
            "path": "icon.png"
        }
    },
    {
        "type": "file",
        "title": "ISP: " + str(json_list['isp']),
        "subtitle": "Press enter to copy to clipboard",
        "arg": "ISP: " + str(json_list['isp']),
        "icon": {
            "path": "icon.png"
        }
    },
    {
        "type": "file",
        "title": "Total reports: " + str(json_list['totalReports']),
        "subtitle": "Press enter to copy to clipboard",
        "arg": "Total reports: " + str(json_list['totalReports']),
        "icon": {
            "path": "icon.png"
        }
    },
    {
        "type": "file",
        "title": "Is public: " + str(json_list['isPublic']),
        "subtitle": "Press enter to copy to clipboard",
        "arg": "Is public: " + str(json_list['isPublic']),
        "icon": {
            "path": "icon.png"
        }
    },
    {
        "type": "file",
        "title": "Last reported at: " + str(json_list['lastReportedAt']),
        "subtitle": "Press enter to copy to clipboard",
        "arg": "Last reported at: " + str(json_list['lastReportedAt']),
        "icon": {
            "path": "icon.png"
        }
    },
    {
        "type": "file",
        "title": "Usage Type: " + str(json_list['usageType']),
        "subtitle": "Press enter to copy to clipboard",
        "arg": "Usage Type: " + str(json_list['usageType']),
        "icon": {
            "path": "icon.png"
        }
    }

]}
output = json.dumps(result)
print(output)