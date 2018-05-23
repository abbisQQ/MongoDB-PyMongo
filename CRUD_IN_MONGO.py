from pprint import pprint
from pymongo import MongoClient
from pymongo import ReturnDocument
from bson.objectid import ObjectId


class MongoDBManagement:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['mongoDatabaseDemo']
        self.collection_employees = self.db["employees"]

    def insert_one_employee(self):
        self.collection_employees.insert_one({
            "name": "Babis",
            "age": 30,
            "email": " chartheodorou@hotmail.com"
        })

    def insert_many_employees(self):
        self.collection_employees.insert_many([{
            "name": "Babis",
            "age": 30,
            "email": " chartheodorou@hotmail.com"
        },
            {
                "name": "Kate",
                "age": 34,
                "email": " kate@hotmail.com"
            },
            {
                "name": "John",
                "age": 27,
                "email": " john@hotmail.com"
            }]
        )

    def update_a_employee(self):
        self.collection_employees.find_one_and_update(
            {'_id': ObjectId("5b059d1a92d3a53ed663a896")
             },
            {
                "$set": {"name": "Mike"}
             },
            projection={"seq": True, "_id": False},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )


    def find_all_employee(self):
        all_employees = self.collection_employees.find({})
        print("Number of records: " + str(all_employees.count()))
        for student in all_employees:
            pprint(student)


    def del_an_employee(self):
        self.collection_employees.delete_many({"name":"Babis"})


if __name__ == "__main__":

    mongoDB = MongoDBManagement()

    mongoDB.insert_one_employee()

    mongoDB.insert_many_employees()

    mongoDB.find_all_employee()

    mongoDB.del_an_employee()

    mongoDB.update_a_employee()
