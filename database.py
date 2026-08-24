from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

#connecting database from MongoDB

def get_database():
    client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)

    try: 
        client.admin.command('ismaster')
        print('Successfully connected to MongoDB')

        return client['my_closet']
    
    except (ConnectionFailure, ServerSelectionTimeoutError) as e:
        print(f'Could not connect to MongoDB: {e}')
        return None
    
if __name__ == '__main__':
    db = get_database()

    if db is not None:
        print('Database is ready to use.')
    else:
        print('Connection failed. Please check your MongoDB server.')

