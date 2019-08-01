from datetime import datetime

from flask import make_response, abort

def get_timestamp():
	return datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))
	
FAN = {
    'One': {
        'Speed': '1',
		'Timestamp': get_timestamp()
    },
	'Two': {
        'Speed': '2',
		'Timestamp': get_timestamp()
    },
	'Three': {
        'Speed': '3',
		'Timestamp': get_timestamp()
    },
}


def read():


	# Create the list from our data
	return [FAN[key] for key in sorted(FAN.keys())]


def create(Fan):

	Speed = Fan.get("Speed", None)
	FAN[Speed] = {
			"Speed": Speed,
			'Timestamp': get_timestamp()
		}
	return make_response('successfully created')



		
