from datetime import datetime

from flask import make_response, abort

def get_timestamp():
	return datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))
	
ENVIRONMENT = {
    'One': {
        'Tem': 'test',
        'Hum': 'test',
		'Pre': 'test',
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


	ENVIRONMENT[Tem] = {
		"Hum": Hum,
		"Pre": Pre,
		"Tem": Tem,
		'Timestamp': get_timestamp()
	}
	return make_response('successfully created')






