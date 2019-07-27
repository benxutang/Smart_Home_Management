
ENVIRONMENT = {
    'One': {
        'Tem': '30',
        'Hum': '25',
		'Pre': '1'
    },
	'Two': {
        'Tem': '25',
        'Hum': '70',
		'Pre': '2'
    },
	'Three': {
        'Tem': '28',
        'Hum': '',
		'Pre': '1'
    },
}



def read():
    '''
    This function responds to a request for /api/environment
    with the complete lists of environment

    :return:        sorted list of environment
    '''
    # Create the list of environment from our data
    return [ENVIRONMENT[key] for key in sorted(ENVIRONMENT.keys())]