import pymongo
import ssl

from mongo_utils.existence_check import *


def get_mongo_client():
    user = 'root'
    password = 'Models2021'
    global client_cloud
    client_cloud = pymongo.MongoClient(
        f"mongodb+srv://{user}:{password}@cluster0.q940z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
        ssl_cert_reqs=ssl.CERT_NONE)

    return client_cloud


def insert_user_details(register_form):
    try:
        client_cloud = get_mongo_client()
        database = 'website'
        collection_name = 'user_details'

        db = client_cloud[database]
        collection = db[collection_name]

        json_data = json_from_form(register_form)

        doc_id = collection.insert_one(json_data).inserted_id
        message = f"User registered successful with id {doc_id}"
    except Exception as e:
        message = f"Failed with exception : {e}"
    return message


def json_from_form(register_form):
    print(f"Data from form is {register_form}")
    json_data = {}
    for each in register_form:
        json_data[each] = register_form[each]
    return json_data
