import json

api_key = open('/home/.openai/api_key.json', 'r')
json_load = json.load(api_key)

print(json_load['api_key']['test-hack-note'])
