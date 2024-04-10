from pymongo import MongoClient

def mongoConnection():
    """
        Establishes a connection with the mongoDB and returns a MongoClient Object
    """

    mongoHost = "localhost"
    mongoPort = 27017

    client = MongoClient(mongoHost, mongoPort)

    try:
        client.admin.command('ping')
        print("[SERVER]: Pinged your deployment. You successfully connected to MongoDB!")    
        return client
    except Exception as e:
        print(f'[SERVER]: {e}')