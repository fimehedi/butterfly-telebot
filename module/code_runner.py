from module.bot import config
import requests
import json

def CodeRunner(code, language):
    if language == 'py': language = 'python3'
    url = config['CODE_RUNNER_API']
    program = {
    'script' : code,
    'language': language,
    'versionIndex': "0",
    'clientId': config['CLIENT_ID'],
    'clientSecret': config['CLIENT_SECRET']
    } # Properties that we need to send to the API

    response = requests.post(url, json=program)
    response_json = json.loads(response.text)
    return response_json


