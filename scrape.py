from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient

uri = "mongodb+srv://krisna:raZK8PYUDJK7aFu@cluster0.kyxkdkz.mongodb.net/?retryWrites=true&w=majority"
# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(uri)

# Access the 'library' database (replace 'library' with the name of your database)
db = client['library']

# Access the 'books' collection (replace 'books' with the name of your collection)
collection = db['books']

def insertBook_Document(book_title, book_link, latest_chapter, chapter_number):
    # Prepare the book document
    book_document = {
    "_id": book_title,
    "book_link": book_link,
    "latest_chapter": latest_chapter,
    "chapter_number": chapter_number
    }

    # Insert the document into the collection   
    collection.insert_one(book_document)

def updateBook_Document(book_title, book_link, latest_chapter, chapter_number):
    query = {"_id": book_title} 
    book = collection.find_one(query)   
    db_chapter_number = book.get("chapter_number")
    db_book_link = book.get("book_link")
    isUpdated = False;
    if(chapter_number != db_chapter_number):
        print("New chapter found, updating latest_chapter and chapter_number...")
        update_data = {"$set": {"latest_chapter": latest_chapter, "chapter_number": chapter_number}}
        collection.update_one(query, update_data)
        isUpdated = True;
    if(db_book_link != book_link):
        print("New link found, updating book_link...")
        update_data = {"$set": {"book_link": book_link}}
        collection.update_one(query, update_data)
        isUpdated = True;
    if(isUpdated):
        print("Update Complete!")
    else:
        print("Book information is already up to date!")
        
    
# Set up Chrome options for running in headless mode
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--headless=new")

# Read the book links from the books.txt file
with open("books.txt", "r") as file:
    book_links = file.read().splitlines()

# Set up the driver with the Chrome options
driver = webdriver.Chrome(options=chrome_options)

# Iterate over the book links
for book_link in book_links:
    # Load the book page
    driver.get(book_link)

    # Wait for the latest chapter link to appear
    chapter_locator = (By.CSS_SELECTOR, ".lastend .inepcx:last-child a")
    latest_chapter_link = WebDriverWait(driver, 5).until(EC.presence_of_element_located(chapter_locator))

    # Find and print the book title element
    book_title_locator = (By.XPATH, "//h1[@class='entry-title' and @itemprop='name']")
    book_title_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located(book_title_locator))
    book_title = book_title_element.text
    print("Book Title:", book_title)

    # Get the href attribute of the latest chapter link
    latest_chapter = latest_chapter_link.get_attribute("href")

    # Remove the trailing slash from the latest_chapter
    latest_chapter = latest_chapter[:-1]

    # Extract the chapter number from the link
    chapter_number = latest_chapter.split("-")[-1]

    # Print the latest chapter link and number
    print("Book:", book_link)
    print("Latest chapter:", latest_chapter)
    print("Chapter number:", chapter_number)

    try:
        insertBook_Document(book_title, book_link, latest_chapter, chapter_number)
    except Exception as e:
        print("Insertion failed:", book_title ,"is already in database")
        print("Checking if book_document is up to date...")
        updateBook_Document(book_title, book_link, latest_chapter, chapter_number)

    print()

# Quit the driver
driver.quit()


