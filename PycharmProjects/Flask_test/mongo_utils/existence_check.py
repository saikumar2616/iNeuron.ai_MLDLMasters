

def checkExistence_COL(COLLECTION_NAME, DB_NAME, db):
    """It verifies the existence of collection name in a database"""
    collection_list = db.list_collection_names()

    if COLLECTION_NAME in collection_list:
        print(f"Collection:'{COLLECTION_NAME}' in Database:'{DB_NAME}' exists")
        return True

    print(f"Collection:'{COLLECTION_NAME}' in Database:'{DB_NAME}' does not exists OR \n\
    no documents are present in the collection")
    return False


def checkExistence_DB(DB_NAME, client):
    """It verifies the existence of DB"""
    DBlist = client.list_database_names()
    if DB_NAME in DBlist:
        print(f"DB: '{DB_NAME}' exists")
        return True
    print(f"DB: '{DB_NAME}' not yet present OR no collection is present in the DB")
    return False
