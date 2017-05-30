from lxml import etree
from xml.dom.minidom import parseString

xml_str = """
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
	<s:Body>
		<ReadResponse xmlns="http://schemas.planview.com/PlanviewEnterprise/Services/QueryService/2012/12">
			<ReadResult xmlns:a="http://schemas.planview.com/PlanviewEnterprise/OpenSuite/OpenSuiteResult/2010/01/01" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
				<a:Failures xmlns:b="http://schemas.planview.com/PlanviewEnterprise/OpenSuite/OpenSuiteStatus/2010/01/01"/>
				<a:GeneralErrorMessage i:nil="true"/>
				<a:Successes xmlns:b="http://schemas.planview.com/PlanviewEnterprise/OpenSuite/OpenSuiteStatus/2010/01/01">
					<b:OpenSuiteStatus i:type="c:QueryStatus" xmlns:c="http://schemas.planview.com/PlanviewEnterprise/OpenSuite/QueryStatus/2012/12">
						<b:Code i:nil="true"/>
						<b:ErrorMessage i:nil="true"/>
						<b:SourceIndex>0</b:SourceIndex>
						<c:Dto xmlns:d="http://schemas.planview.com/PlanviewEnterprise/OpenSuite/Dtos/QueryDto/2012/12">
							<d:ColumnNames xmlns:e="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
								<e:string>structure_code</e:string>
							</d:ColumnNames>
							<d:ColumnTypes xmlns:e="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
								<e:string>string</e:string>
							</d:ColumnTypes>
							<d:ParsedSqlQuery>
SELECT structure_code
FROM ext_struc_key_map
WHERE xid = '2218537'</d:ParsedSqlQuery>
							<d:QueryResults xmlns:e="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
								<e:ArrayOfanyType>
									<e:anyType i:type="f:string" xmlns:f="http://www.w3.org/2001/XMLSchema">22792</e:anyType>
								</e:ArrayOfanyType>
								<e:ArrayOfanyType>
									<e:anyType i:type="f:string" xmlns:f="http://www.w3.org/2001/XMLSchema">22792</e:anyType>
								</e:ArrayOfanyType>
							</d:QueryResults>
							<d:SqlQuery>
SELECT structure_code
FROM ext_struc_key_map
WHERE xid = '2218537'</d:SqlQuery>
						</c:Dto>
					</b:OpenSuiteStatus>
				</a:Successes>
				<a:Warnings xmlns:b="http://schemas.planview.com/PlanviewEnterprise/OpenSuite/OpenSuiteStatus/2010/01/01"/>
			</ReadResult>
		</ReadResponse>
	</s:Body>
</s:Envelope>
"""

parser = etree.XMLParser()
root = etree.fromstring(xml_str, parser=parser)

print(root)

dom = parseString(xml_str)
print(dom)

nodes = dom.getElementsByTagName('e:ArrayOfanyType')

print(nodes)


lst = []

for node in nodes:
    print(node)
    inner_lst = []
    for child_node in node.childNodes:


        if child_node.nodeType != child_node.TEXT_NODE:
            inner_lst.append(child_node.firstChild.nodeValue)
    tup = tuple(inner_lst)
    lst.append(tup)

print(lst)



        # inner_xml = child_node.toxml()
        #
        # inner_nodes = dom.getElementsByTagName('e:anyType')
        #
        # for inner_node in inner_nodes:
        #     print(inner_node.firstChild.nodeValue)

        # if not isinstance(child_node, str):
        #     print(child_node.childNodes[0].nodeValue)


