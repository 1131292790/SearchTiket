import pymongo
class Connect():

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
    #写入数据
    def Write_Data(self,data,collection):
        result = collection.insert_one(data)
        print(result.inserted_id)
    #读取数据
    def Read_Data(self,collection,condition):
        result = collection.find(condition)
        for i in result:
            print(i)

