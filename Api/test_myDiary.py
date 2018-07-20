from unittest import TestCase
from flask import jsonify
from MyDiary import MyDiary


class TestMyDiary(TestCase):
    def test_get_all_entries(self):
        result = MyDiary.get_all_entries()
        if len(result) > 0:
            self.assertEqual(result['Message'], jsonify(result))
        else:
            self.assertEqual(result['Message'], 'No entries yet')

    def get_one_entry(self):
        result = MyDiary.get_one_entry(MyDiary.get_one_entry, 2)
        if len(result) > 0:
            response = jsonify(result)
            self.assertEqual(result['Message'], MyDiary.get_one_entry(MyDiary.get_one_entry, 2))
            self.assertEqual(response.status_code, 200)
        else:
            self.assertEqual(result['Message'], 'No entries yet')

    def test_add_new_entry(self):
        #get record count
        res = MyDiary.get_all_entries()

        #add new record
        result = MyDiary.add_new_entry()
        response= jsonify(result)

        #get current record count after adding
        res1 = MyDiary.get_all_entries()

        #check if the count of res is less than res1
        if len(res) < len(res1):

            self.assertTrue(result['message'], 'added successfully')
            self.assertTrue(response.status_code, 201)
        else:
            self.assertTrue(response.status_code, 304)



    def test_update_task(self):
        self.fail()

    def test_sign_up(self):
        self.fail()

    def test_login(self):
        self.fail()
