import requests
import jsonpath


def test_add_new_data():
    app_url = "http://thetestingworldapi.com/api/studentsDetails"
    request_json = {
        "first_name": "Testing",
        "middle_name": "M",
        "last_name": "World",
        "date_of_birth": "11/11/2000"
    }
    response = requests.post(app_url, request_json)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    tech_json = {
        "id": 148622,
        "language": ["Java", "C#"],
        "yearexp": "2",
        "lastused": "2019",
        "st_id": "148622"
    }
    response2 = requests.post(tech_api_url, tech_json)
    print(response2.text)
