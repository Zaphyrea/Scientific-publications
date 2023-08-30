from pymongo import MongoClient

class MongoAccess : 
    __USER = "root"
    __PW = "example"
    __DB_NAME = "DBLP"
    # __PORT = 27018  and {cls.__PORT} are also good


    @classmethod
    def connect(cls) :
        cls.client = MongoClient(f"mongodb://{cls.__USER}:{cls.__PW}@127.0.0.1:27018")

        cls.db = cls.client[cls.__DB_NAME]

        return cls.db

    @classmethod
    def disconnect(cls) :
        cls.client.close()

