from flask import Flask, jsonify
import config

# Constant BASE_URL is prefixed to each route
BASE_URL = '/MyDiary/api/v1'

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

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
@app.route('{}/entries/'.format(BASE_URL), methods=['GET'])
    def get_all_entries(self):
    	
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

@app.route('/entries/<int:entry_id>', methods=['GET'])
    def get_one_entry(self, entry_id):
            my_entry = [my_entry for my_entry in my_entries if my_entry['id'] == entry_id]
            if len(my_entry) == 0:
                abort(404)
            
            response = jsonify({'Entry': my_entry[entry_id]})
            response.status_code = 200