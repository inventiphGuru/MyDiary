from unittest import TestCase
import json
import MyDiary
from MyDiary import create_app

ADD_ENTRY_URL = '/api/v1/user/my_entries'
SINGLE_ENTRY_URL = '/api/v1/my_entries/1'
MY_ENTRIES_URL = '/api/v1/my_entries'
ENTRY_DELETE_URL = '/api/v1/my_entries/1'
ENTRY_UPDATE_URL = '/api/v1/my_entries/1'
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
        
        self.app = create_app(config_name="test_MyDiary")
        self.client = self.app.test_client()
        self.data = {
            'id': 1,
            'title': u'challenge One',
            'description': u'UI design is not as simple as it looks',
            'Date_Created': '20-06-2018',
            'last_update': '27-06-2018'
}
    def test_get_all_entries(self):
        #result= MyDiary.get_all_entries
        #self.assertEqual(result, all_entries)
        response = self.client.get(MY_ENTRIES_URL)
        self.assertEqual(response.status_code, 200)


    def get_one_entry(self):
        #result = MyDiary.get_one_entry(1)
        #my_entry = [my_entry for my_entry in all_entries if my_entry['id'] == 1]
        #self.assertEqual(result, my_entry)
        response = self.client.post(SINGLE_ENTRY_URL, data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_c = self.client.get(SINGLE_ENTRY_URL)
        self.assertEqual(response_c.status_code, 200)

    def test_add_new_entry(self):
        response = self.client.post(ADD_ENTRY_URL, data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_update_task(self):
        response = self.client.post(MY_ENTRIES_URL, data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(response.status_code, 201)


