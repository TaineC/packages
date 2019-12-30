#package install already in env/bin file --> VSCode claims error of import requests
import requests
import json

response = requests.get('http://api.open-notify.org/astros.json')

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=2)
    print(text)

results = response.json()
jprint(results)
print()
# print(results['name'])

for item in results['people']:
    print(item)