from datetime import datetime

from flask import make_response, abort

def get_timestamp():
	return datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))
	
LIGHT = {
    'One': {
        'Ligcon': 'test',
		'State': '1',
		'Timestamp': get_timestamp()
    },
}


def read():


	# Create the list from our data
	return [LIGHT[key] for key in sorted(LIGHT.keys())]


def create(Light):

	Ligcon = Light.get("Ligcon", None)
	State = Light.get("State", None)
	LIGHT[Ligcon] = {
		"Ligcon": Ligcon,
		"State": State,
		'Timestamp': get_timestamp()
	}	


	return make_response('successfully created')

