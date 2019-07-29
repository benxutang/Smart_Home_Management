

from flask import make_response, abort

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
			'timestamp': get_timestamp()
		}
		return make_response('successfully created')

	# Otherwise, they exist, that's an error
	else:
		abort(406,'already exists')




