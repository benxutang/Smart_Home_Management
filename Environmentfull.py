from datetime import datetime

from flask import make_response, abort

def get_timestamp():
	return datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))
	
ENVIRONMENT = {
    'One': {
        'Tem': '30',
        'Hum': '25',
		'Pre': '1',
		'Timestamp': get_timestamp()
    },
	'Two': {
        'Tem': '25',
        'Hum': '70',
		'Pre': '2',
		'Timestamp': get_timestamp()
    },
	'Three': {
        'Tem': '28',
        'Hum': '',
		'Pre': '1',
		'Timestamp': get_timestamp()
    },
}


def read():
	'''
	This function responds to a request for /api/people
	with the complete lists of people

	:return:        sorted list of people
	'''
	# Create the list from our data
	return [ENVIRONMENT[key] for key in sorted(ENVIRONMENT.keys())]


def create(Enviroment):

	Tem = Enviroment.get("Tem", None)
	Hum = Enviroment.get("Hum", None)
	Pre = Enviroment.get("Pre", None)

	# Does the person exist already?
	if Tem not in ENVIRONMENT and Tem is not None:
		ENVIRONMENT[Tem] = {
			"Hum": Hum,
			"Pre": Pre,
			"Tem": Tem,
			'Timestamp': get_timestamp()
		}
		return make_response('successfully created')

	# Otherwise, they exist, that's an error
	else:
		abort(406,'already exists')




