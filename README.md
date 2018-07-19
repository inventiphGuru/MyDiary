# MyDiary

this is an Api that allows CRUD functionilty to the Mydiary app.
 The following are the http verbs and end points of the Api.

#http methods:
HTTP Method	URI	Action
GET	http://[hostname]/MyDiary/api/v1/Entries	Retrieve list of Entries
GET	http://[hostname]/MyDiary/api/v1/Entries/[Entry_id]	Retrieve a Entry
POST	http://[hostname]/MyDiary/api/v1/Entries	Create a new Entry
PUT	http://[hostname]/MyDiary/api/v1/Entries/[Entry_id]	Update an existing Entry
DELETE	http://[hostname]/MyDiary/api/v1/Entries/[Entry_id]	Delete a entry

#functions implemented (End points):
Get all diary entries.  --- method [GET]
Get a specific diary entry. --- method [GET]
Add an entry  --- Method [POST]
Modify an entry. --- method [PUT]

