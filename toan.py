from pymongo import MongoClient

client = MongoClient("mongodb://mobio_etl:mobio_etl789@192.168.5.23:27017/mobio_etl?authSource=mobio_etl")
db = client["mobio_etl"]
collection = db["product_holding"]

# Mở Change Stream
with collection.watch() as stream:
    for change in stream:
        print(change)  # Xử lý dữ liệu thay đổi1
