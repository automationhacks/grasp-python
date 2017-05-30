expected = [{
		'data' : {
			'description' : 'Auto_Design (PPL+1) Description_2017-01-03_13:46:57_390724',
			'name' : 'Auto_Design (PPL+1)_2017-01-03_13:46:57_390724',
			'children' : [{
					'data' : {
						'description' : 'Auto_Understand Design (PPL+2) Description_2017-01-03_13:46:58_908605',
						'name' : 'Auto_Understand Design (PPL+2)_2017-01-03_13:46:58',
						'children' : [{
								'data' : {
									'description' : 'Auto_Understand Design (PPL+2) Description_2017-01-03_13:46:58_908605',
									'name' : 'Auto_Understand Design (PPL+2)_2017-01-03_13:46:58',
									'children' : []
								},
								'id' : 44198
							}
						]
					},
					'id' : 44195
				}
			]
		},
		'id' : 44194
	}
]

actual = [{
		'data' : {
			'description' : 'Auto_Design (PPL+1) Description_2017-01-03_13:46:57_390724',
			'name' : 'Auto_Design (PPL+1)_2017-01-03_13:46:57_390724',
			'children' : [{
					'data' : {
						'description' : 'Auto_Understand Design (PPL+2) Description_2017-01-03_13:46:58_908605',
						'name' : 'Auto_Understand Design (PPL+2)_2017-01-03_13:46:58',
						'children' : [{
								'data' : {
									'description' : 'Auto_Understand Design (PPL+2) Description_2017-01-03_13:46:58_908605',
									'name' : 'Auto_Understand Design (PPL+2)_2017-01-03_13:46:58',
									'children' : []
								},
								'id' : 44195
							}
						]
					},
					'id' : 44195
				}
			]
		},
		'id' : 44194
	}
]

list_status = []

def verify_pve_wbs(expected, actual):
    list_of_dict_expected = expected.copy()
    list_of_dict_actual = actual.copy()

    if len(list_of_dict_expected) == len(list_of_dict_actual):
        for e_dct in list_of_dict_expected:
            for a_dct in list_of_dict_actual:
                if e_dct['id'] == a_dct['id']:
                    print('Found matching dict for PP ID: %s.. Starting comparison' % e_dct['id'])

                    expected = e_dct['data']
                    actual = a_dct['data']
                    print('After match. Checking Data \n Expected: %s \n Actual: %s' % (expected, actual))

                    for key, value in expected.items():
                        print('\n Innermost', key, value)
                        if value != actual[key]:
                            list_status.append(False)
                            print('\n Values do not match \n Expected: %s \n Actual: %s' % (value, a_dct[key]))
                        else:
                            print('Values matched for %s' % value)

                        if not expected['children']:
                            print('Now returning')
                            return
                        else:
                            print('About to recurse')
                            input('Should i recurse now?')
                            verify_pve_wbs(expected['children'], actual['children'])
                else:
                    print('Skipping to next')
    else:
        print('Length does not match for expected and actual dict')
    return all(list_status)


print(verify_pve_wbs(expected, actual))