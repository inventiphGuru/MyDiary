from flask import Flask, jsonify
import config

# Constant BASE_URL is prefixed to each route
BASE_URL = '/MyDiary/api/v1'

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

@app.route('{}/entries/'.format(BASE_URL), methods=['GET'])
    def get_all_entries(self):
           

     # fetch all entries end point
		my_entries = [
			        {
			            'id': 1,
			            'title': u'challenge One',
			            'description': u'UI design is not as simple as it looks',
			            'Date_Created': '20-06-2018',
			            'last_update': '27-06-2018'
			        },
			        {
			            'id': 2,
			            'title': u'challenge Two',
			            'description': u'Api design and development',
			            'Date_Created': '25-06-2018',
			            'last_update': '26-06-2018'
			        },
			        {
			            'id': 3,
			            'title': u'challenge three',
			            'description': u'Database design with more Api functions',
			            'Date_Created': '29-06-2018',
			            'last_update': '1-07-2018'
			        }
			]

			if len(all_entries)==0:
				result = {
            	'message': 'No entries yet.'

            	}
            	response = jsonify(result)
            else:
            	result = all_entries

 		response = jsonify(result)
    	response.status_code = 200
		return response