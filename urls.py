from handlers.foo import FooHandler
from handlers.main import MainHandler
from handlers.DynamoDBHandler import DynamoDBFetchData
from handlers.DynamoDBHandler import DynamoDBWriteData
from handlers.DynamoDBHandler import DynamoDBScan

url_patterns = [
    (r"/", MainHandler),
    (r"/foo", FooHandler),
    (r"/dynamoDBFetchData", DynamoDBFetchData),
    (r"/dynamoDBWriteData", DynamoDBWriteData),
    (r"/dynamoDBScan", DynamoDBScan)
]
