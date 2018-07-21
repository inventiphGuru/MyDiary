from typing import Dict, List
from flask import Flask, jsonify, request, abort
from flask_api import FlaskAPI, status

from instance.config import app_config

import _datetime



all_entries = [
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

def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=True)

    app.config.from_object(app_config[config_name])

  
# '''class MyDiary:

 #   ''''@app.route('/all_entries', methods=['GET'])
 #   def get_all_entries():
  #              return jsonify({'Entries': my_entries})
  #  '''
    

    @app.route('/MyDairy/api/v1/my_entries', methods=['GET'])
    def get_all_entries():
        result= all_entries
        return jsonify({'My entries': result})
        

    @app.route('/MyDairy/api/v1/my_entries/<int:entry_id>', methods=['GET'])
    def get_one_entry( entry_id):
        entry=[entry for entry in all_entries if entry['id'] == entry_id]
        if len(entry)== 0:
            abort(404)
        return jsonify({'entry':entry[0]})

    @app.route('/MyDairy/api/v1/my_entries', methods=['POST'])
    def add_new_entry():
        New_id = all_entries[-1]['id'] + 1
        title = request.args.get('title')
        description = request.args.get('description')
        Date_Created = request.args.get(_datetime.date.today())
        last_update = request.args.get(_datetime.date.today())
        if title and description:
            my_entry = MyDairy.add_new_entry(New_id, title,description,Date_Created,last_update)
            if not my_entry:
                response = jsonify(message='Bad request. Similar entry exists'), 400
            else:
                response = jsonify({'entry added' :{'title' : title,'description' : description,'Date_Created' : Date_Created,
                    'last_update': last_update}})

            response.status_code = 201

    @app.route('/MyDairy/api/v1/my_entries/<int:entry_id>', methods=['PUT'])
    def update_entry(entry_id):
                my_entry = [my_entry for my_entry in all_entries if my_entry['id'] == entry_id]
                if len(my_entry) == 0:
                    abort(404)

                if not request.json:
                    abort(400)

                if 'title' in request.json and type(request.json['title']) != str:
                    abort(400)
                if 'description' in request.json and type(request.json['description']) is not str:
                    abort(400)
                if 'done' in request.json and type(request.json['done']) is not bool:
                    abort(400)

                if request.method == 'PUT':
                    my_entry[0]['title'] = request.json.get('title', my_entry[0]['title'])
                    my_entry[0]['description'] = request.json.get('description', my_entry[0]['description'])
                    my_entry[0]['Date_Created'] = request.json.get('Date_Created', my_entry[0]['Date_Created'])
                    my_entry[0]['last_update'] = request.json.get('last_update', my_entry[0]['last_update'])
                response = jsonify({'task': my_entry[0]})
                response.status_code = 201
                return 'Entry updated successfully'


    @app.route("/signup")
    def sign_up(self):
                return "Get started"


    @app.route("/sign_in")
    def login(self):
                return "Welcome, please sign-in"


    if __name__ == '__main__':
        app.run(debug=True)

    return app