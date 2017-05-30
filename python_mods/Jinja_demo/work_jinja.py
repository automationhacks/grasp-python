# xml_temp = """
# <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://schemas.planview.com/PlanviewEnterprise/Services/ProjectService3/2012/08" xmlns:ns1="http://schemas.planview.com/PlanviewEnterprise/OpenSuite/Dtos/ProjectDto2/2012/08" xmlns:plan="http://schemas.datacontract.org/2004/07/Planview.Enterprise.OpenSuite.Dtos.Configuration">
# 	<soapenv:Header/>
# 	<soapenv:Body>
# 		<ns:Create>
# 			<ns:dtos>
# 				<ns1:ProjectDto2>
# 					<ns1:Description> </ns1:Description>
# 					<ns1:FatherKey> </ns1:FatherKey>
# 					{{ lcycle }}
# 					{% if lcycle %}
# 					<ns1:LifecycleAdminUserKey> </ns1:LifecycleAdminUserKey>
# 					{% endif %}
# 				</ns1:ProjectDto2>
# 			</ns:dtos>
# 		</ns:Create>
# 	</soapenv:Body>
# </soapenv:Envelope>
# """

import sys, os
from jinja2 import Template

path = os.path.join(os.path.dirname(__file__), '.')
print(path)
sys.path.extend([path])

# from xml.etree import ElementTree

# xml = ElementTree.ElementTree(ElementTree.fromstring(xml_temp))
# print(type(xml))

with open('attrib_poc.xml', 'r') as f:
    temp = f.read()

print(temp)

t = Template(temp)
xml_after_render = t.render(lcycle=False)

print(xml_after_render, type(xml_after_render))



