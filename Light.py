from datetime import datetime

from flask import make_response, abort

def get_timestamp():
	return datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))
	
LIGHT = {
    'One': {
        'Light': '0',
		'Timestamp': get_timestamp()
    },
	'Two': {
        'Light': '0.5',
		'Timestamp': get_timestamp()
    },
	'Three': {
        'Light': '1',
		'Timestamp': get_timestamp()
    },
}


def read():


	# Create the list from our data
	return [LIGHT[key] for key in sorted(LIGHT.keys())]


def create(Light):

	Light = Light.get("Light", None)

	# Does the person exist already?
	if Light not in LIGHT and Light is not None:
		LIGHT[Light] = {
			"Light": Light,
			'Timestamp': get_timestamp()
		}
		return make_response('successfully created')

	# Otherwise, they exist, that's an error
	else:
		abort(406,'already exists')
