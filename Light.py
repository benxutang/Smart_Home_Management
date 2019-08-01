from datetime import datetime

from flask import make_response, abort

def get_timestamp():
	return datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))
	
LIGHT = {
    'One': {
        'Light': 'test',
		'State': '1',
		'Timestamp': get_timestamp()
    },
	'Two': {
        'Light': 'test',
		'State': '1',
		'Timestamp': get_timestamp()
    },
	'Three': {
        'Light': 'test',
		'State': '1',
		'Timestamp': get_timestamp()
    },
}


def read():


	# Create the list from our data
	return [LIGHT[key] for key in sorted(LIGHT.keys())]


def create(Light):

	Light = Light.get("Light", None)
	State = Light.get("State", None)
	LIGHT[Light] = {
			"Light": Light,
			"State": State,
			'Timestamp': get_timestamp()
		}
	return make_response('successfully created')



		
