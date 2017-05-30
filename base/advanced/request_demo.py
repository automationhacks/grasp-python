import requests


request = requests.session()

headers = {'content-type': 'application/json'}
url = 'https://rally1.rallydev.com/slm/webservice/v2.0/security/authorize'
user = 'gsingh@planview.com'
pwd = 'pvmaster'
get_resp = request.get(url, auth=(user, pwd))
token = get_resp.json()['OperationResult']['SecurityToken']


us = '59870389671'
url = 'https://rally1.rallydev.com/slm/webservice/v2.0/hierarchicalrequirement/'+us+'?fetch=Name,Workspace,Project,Initiative,Feature'
get_resp = request.get(url=url, headers=headers)
raise NameError(get_resp.content)

data = {'HierarchicalRequirement': {'Name': 'PythonUserStory1'}}


get_resp = requests.get(url, headers=headers)
request.post(url=url, data=data, headers=headers)