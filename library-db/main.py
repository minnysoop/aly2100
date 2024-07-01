# Import pymongo module
import pymongo

# Establish client
client = pymongo.MongoClient("localhost", 27017)

# Create a library database 
db = client["library"]

# Initialize a book collection
book = db["book"]

# Adding a sample book
lord_of_the_flies = {
    "Author": "William Golding",
    "Title": "Lord of the Flies",
    "Print": "Paperback",
    "Year_Published": 1955
}

# NOTE: The view book function here has been modified as the document was created. This view function will cause a missing key error if you try and run this from scratch again!
def viewBooks():
    for i in book.find({}):
        print("Author: " + i["Author"])
        print("Book: " + i["Title"])
        print("Print: " + i["Print"])
        print("Year_Published: " + str(i["Year_Published"]))
        print("Number_of_pages: " + str(i["Number_of_pages"]))
        print("Borrowed: " + str(i["Borrowed"]))
        print("----------")

def viewDVDs():
    for i in dvd.find({}):
        print("DVD: " + i["Title"])
        print("Released_Date: " + str(i["Released_Date"]))
        print("Blue Ray?: " + str(i["Blue-ray"]))
        print("Duration: " + str(i["Duration"]))
        print("----------")

# Views what collections exist
def viewCollections():
    for collections in db.list_collection_names():
        print("Collection: " + collections)
        print("----------")

# Inserting the sample book into the collection
book.insert_one(lord_of_the_flies)

# Updating the document to have the correct information
book_to_change = { "Author": "William Golding", "Title": "Lord of the Flies" }
book_new_values = { "$set": { "Year_Published": 1954 } }

# Execute the query to update the document
book.update_one(book_to_change, book_new_values)

# Adding a field
book_new_field = { "$set": { "Number_of_pages": 307 } }
book.update_one(book_to_change, book_new_field)

# ---- Assignment 10
# Another book we can add
farenheit451 = {
    "Author": "Ray Bradbury",
    "Title": "Farenheit 451",
    "Print": "Paperback",
    "Year_Published": 1953,
    "Number_of_pages": 158
}

# Inserting the book in our book collection
book.insert_one(farenheit451)

# Updating every field in the books collection
target_books = {}
newvalues = {"$set" : {"Borrowed": False}}
book.update_many(target_books, newvalues)

# Creating a DVD collection
dvd = db["dvd"]

# Creatinga sample dvd
star_trek = {
    "Title": "Star Trek",
    "Blue-ray": True,
    "Duration": 127,
    "Released_Date": 2009
}

# Inserting a dvd into the dvd collection
dvd.insert_one(star_trek)

# Delete a book from the book collection
book.delete_one({"Title": "Lord of the Flies"})
viewBooks()
