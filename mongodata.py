import pymongo
class connect():

    #服务器地址 端口 数据库名 集合名
    def __init__(self,host,port,database,coll_name):
        self.host = host
        self.port = port
        self.database = database
        self.coll_name = coll_name
    def connet_to_Database(self):
        client = pymongo.MongoClient(host=self.host,port=self.port)
        db = client[self.database]
        collection = db[self.coll_name]
        return collection
    def Write_Data(self,data,collection):
        result = collection.insert_one(data)
        print(result.inserted_id)
    def Read_Data(self,condition,collection):
        result = collection.find_one(condition)
        print(result)

