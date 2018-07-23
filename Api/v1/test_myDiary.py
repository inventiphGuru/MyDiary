from unittest import TestCase
from MyDiary import create_app
import json
import MyDiary
import os

ADD_ENTRY_URL = '/MyDairy/api/v1/my_entries'
SINGLE_ENTRY_URL = '/MyDairy/api/v1/my_entries/1'
MY_ENTRIES_URL = '/MyDairy/api/v1/my_entries'
ENTRY_DELETE_URL = '/MyDairy/api/v1/my_entries/1'
ENTRY_UPDATE_URL = '/MyDairy/api/v1/my_entries/1/content'
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


class TestMyDiary(TestCase):

    def setUp(self):
        
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.data = {
            'id': 1,
            'title': u'challenge One',
            'description': u'UI design is not as simple as it looks',
            'Date_Created': '20-06-2018',
            'last_update': '27-06-2018'
            }

    def test_get_all_entries(self):
        response = self.client.get(MY_ENTRIES_URL)
        self.assertEqual(response.status_code, 200)
        
    def test_get_one_entry(self):
        #result = MyDiary.get_one_entry(1)
        #my_entry = [my_entry for my_entry in all_entries if my_entry['id'] == 1]
        #self.assertEqual(result, my_entry)
        response = self.client.get(SINGLE_ENTRY_URL)
        self.assertEqual(response.status_code, 200)
   

    def test_add_new_entry(self):
        response = self.client.post(ADD_ENTRY_URL, data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(response.status_code, 201)


    def test_update_task(self):
        response = self.client.post(ENTRY_UPDATE_URL, data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(response.status_code, 201)


