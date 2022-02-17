import requests
import configparser
from Payload import *
from utilities.resources import *
from utilities.configurations import *

url_add = getConfig()['API']['endpoint'] + APIResources.addBook
url_del = getConfig()['API']['endpoint'] + APIResources.deleteBook
add_BookResponse = requests.post(url_add, json=addBookPayload("199", "90")
                                 , headers={"Content-Type": "application/json"})
if add_BookResponse.status_code == 404:
    raise Exception("Please re enter the book")
else:
    print(f"The status code after adding book is {add_BookResponse.status_code}")
response = add_BookResponse.json()
print(response)
print(add_BookResponse.status_code)
id = response['ID']

# DELETE BOOK
del_BookResponse = requests.post(url_del, json=
{

    "ID": id
}
                                 )
del_book = del_BookResponse.json()
print(del_book["msg"])
assert del_BookResponse.status_code == 200
if del_BookResponse.status_code ==

