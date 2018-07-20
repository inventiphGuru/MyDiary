from typing import Dict, List, Union

from flask import Flask, jsonify, request, abort

import _datetime

'''BASE_URL = '/MyDiary/api/v1' '''

app = Flask(__name__)


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


# '''class MyDiary:

''''@app.route('/all_entries', methods=['GET'])
def get_all_entries():
            return jsonify({'Entries': my_entries})
'''


@app.route('/my_entries', methods=['GET'])
def get_all_entries():
    if len(all_entries) == 0:
        result = {
            'message': 'No entries yet.'
        }
        response = jsonify(result)
        return response
    else:
        result = all_entries
        response = jsonify(result)
        response.status_code = 200
        return response


@app.route('/my_entries/<int:entry_id>', methods=['GET'])
def get_one_entry(entry_id):
    for my_entry in all_entries:
        if my_entry['id'] == entry_id:
            response = jsonify('Entry', my_entry)
            response.status_code = 200
            return response
        else:
            return jsonify(' No entry found', 304)


@app.route('/Add_entries', methods=['POST'])
def add_new_entry(entry_id):
    for my_entry in all_entries:
        if my_entry['id'] != entry_id:
            my_entry = {
                    'id': all_entries[-1]['id'] + 1,
                    'title': request.json['title'],
                    'description': request.json.get('description', ""),
                    'Date_Created': request.json.get(_datetime.date.today()),
                    'last_update': request.json.get(_datetime.date.today())
                 }
            all_entries.append(my_entry)
            result = {'message': 'Added successfully'}
            response = jsonify(result)
            response.status_code = 201
            return jsonify({'Entry': my_entry}), 201


@app.route('/my_entries/<int:entry_id>', methods=['PUT'])
def update_task(entry_id):
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

        my_entry[0]['title'] = request.json.get('title', my_entry[0]['title'])
        my_entry[0]['description'] = request.json.get('description', my_entry[0]['description'])
        my_entry[0]['Date_Created'] = request.json.get('Date_Created', my_entry[0]['Date_Created'])
        my_entry[0]['last_update'] = request.json.get('last_update', my_entry[0]['last_update'])
        return jsonify({'task': my_entry[0]})


@app.route("/MyDiary/api/v1/signup")
def sign_up():
        return "Get started"


@app.route("/MyDiary/api/v1/sign_in")
def login():
        return "Welcome, please sign-in"


if __name__ == '__main__':
    app.run(debug=True)
