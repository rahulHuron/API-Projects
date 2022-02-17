import requests
import json
response = requests.get("http://216.10.245.166/Library/GetBook.php",params={
'AuthorName':'Brian Hawk'
},)

response_json = response.json()
# print(response_json)
assert response.status_code == 200
# print(response.headers)
for each in response_json:
    if each["isbn"] == "zqr":
        actual_response = each
        print(actual_response)


expected_response = {
        "book_name": "Python_SDET",
        "isbn": "zqr",
        "aisle": "2134"
    }

if(actual_response == expected_response):
    print("It's Matching")