def prepare_payload(key, rally_sync, rally_workspace, rally_project, pf_type, wrk_status, *args):
    list_attr_values = [
        {'ns1:DeleteValue': 'false', 'ns1:EntityKey': key, 'ns1:Id': 'RallySync', 'ns1:Value': rally_sync},
        {'ns1:DeleteValue': 'false', 'ns1:EntityKey': key, 'ns1:Id': 'RalWspace', 'ns1:Value': rally_workspace},
        {'ns1:DeleteValue': 'false', 'ns1:EntityKey': key, 'ns1:Id': 'RallyProj', 'ns1:Value': rally_project},
        {'ns1:DeleteValue': 'false', 'ns1:EntityKey': key, 'ns1:Id': 'RalPfITyp', 'ns1:Value': pf_type}]
    if args:
        list_of_keys = args[0]
        print('list_of_keys ', list_of_keys)
        # for val in list_of_keys:
        #     for item in list_attr_values:
        #         if item['ns1:Id'] == val:
        #             print('Found key and substituting')
        #             item['ns1:DeleteValue'] = 'true'

        for val in list_of_keys:
            list_attr_values = [item['ns1:DeleteValue'] = 'true' for item in list_attr_values if item['ns1:Id'] == val]
            for item in list_attr_values:
                if item['ns1:Id'] == val:
                    print('Found key and substituting')
                    item['ns1:DeleteValue'] = 'true'

prepare_payload('1', 'Yes', 'WSpace', 'RProj', 'RInit', 'Open', ['RallySync','RalWspace'])