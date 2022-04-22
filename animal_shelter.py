from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:50527' % (username, password))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD. 
    def read_all(self,data):
        cursor = self.database.animals.find(data, {'_id':False})
        return cursor
                                                  
    def read(self,data):
        return self.database.animals.find_one(data)
    
# Create the method to implement the U in CRUD
    def update(self, data,new_data):
        if data is not None:
        # return if number of records updated is greater than zero else no results found
            result = self.database.animals.update_one(data,new_data)
            return result.matched_count>0
        else:
            updateException = "No results found"
            raise Exception(updateException)
             

# Create the method to implement the D in CRUD
    def delete(self,data):
        if data is not None:
       # return if number of records deleted is greater than zero else nothing to delete
           result = self.database.animals.delete_one(data)
           return result.deleted_count>0  
        else:
            deleteException = "Nothing to delete."
            raise Exception("deleteException")