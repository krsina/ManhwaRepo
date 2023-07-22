from pymongo import MongoClient

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   uri = "mongodb+srv://krisna:raZK8PYUDJK7aFu@cluster0.kyxkdkz.mongodb.net/?retryWrites=true&w=majority"

 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(uri)
 
   # Access the 'library' database (replace 'library' with the name of your database)
   db = client['library']

   # Prepare the book document
   book_document = {
    "_id": "unique_link_to_book",
    "latest_chapter": "link_to_chapter",
    "chapter_number": "Chapter 10"
   }

