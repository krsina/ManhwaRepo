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
from datetime import datetime
from message import DiscordBot
import json

# Load the secret.json file
with open('secret.json') as f:
    secrets = json.load(f)
# Access the uri
uri = secrets['MONGODB_URI']
# Create a connection using MongoClient
client = MongoClient(uri)
# Access the 'library' database
db = client['library']
# Access the 'books' collection
collection = db['books']
# List of books based on operation
books = []
# Book Object
class Book:
    def __init__(self):
        self.book_title = ""
        self.latest_chapter = "" 
        self.image_url = ""
        self.message = ""

#Inserts a book document into the database
def insertBook_Document(book_title, book_link, latest_chapter, chapter_number,image_url):
    # Prepare the book document
    date_time = datetime.now()
    book_document = {
    "_id": book_title,  
    "book_link": book_link,
    "latest_chapter": latest_chapter,
    "chapter_number": chapter_number,
    "date_time": date_time,
    "image_url": image_url
    }

    # Insert the document into the collection   
    collection.insert_one(book_document)
    new_book = Book()
    new_book.book_title = book_title
    new_book.latest_chapter = latest_chapter
    new_book.image_url = image_url
    new_book.message = book_title + " has been added."
    books.append(new_book);

def updateBook_Document(book_title, book_link, latest_chapter, chapter_number):
    query = {"_id": book_title} 
    book = collection.find_one(query)   
    db_chapter_number = book.get("chapter_number")
    db_book_link = book.get("book_link")
    isUpdated = False;
    if(chapter_number != db_chapter_number):
        date_time = datetime.now()
        print("New chapter found, updating latest_chapter, chapter_number, and date_time...")
        update_data = {"$set": {"latest_chapter": latest_chapter, "chapter_number": chapter_number, "date_time": date_time}}
        collection.update_one(query, update_data)
        isUpdated = True;
        new_book = Book()
        new_book.book_title = book_title
        new_book.latest_chapter = latest_chapter
        new_book.image_url = image_url
        new_book.message = " A new chapter has been released!"
        books.append(new_book)
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

    # Wait for the div with class "thumb" to appear
    div_locator = (By.CSS_SELECTOR, "div.thumb")  
    div_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(div_locator))
    img_element = div_element.find_element(By.TAG_NAME, "img")
    image_url = img_element.get_attribute("src").replace('https://img.asuracomics.com/unsafe/fit-in/720x936/', '')
    # Get the href attribute of the latest chapter link
    latest_chapter = latest_chapter_link.get_attribute("href")
    # Remove the trailing slash from the latest_chapter
    latest_chapter = latest_chapter[:-1]
    # Extract the chapter number from the link
    
    chapter_number = latest_chapter.split("-")[-1]
    print("Book:", book_link)
    print("Latest chapter:", latest_chapter)
    print("Chapter number:", chapter_number)

    try:
        insertBook_Document(book_title, book_link, latest_chapter, chapter_number, image_url)
        print("Book inserted into database")
    except Exception as e:
        print("Insertion failed:", book_title ,"is already in database")
        print("Checking if book_document is up to date...")
        updateBook_Document(book_title, book_link, latest_chapter, chapter_number)

    print()

if(books):
    TOKEN = secrets['DISCORD_KEY'];
    MANHWA_CHANNEL_ID = secrets['DISCORD_CHANNEL_ID'];
    # Create an instance of the DiscordBot class
    bot = DiscordBot(TOKEN, MANHWA_CHANNEL_ID, books)
    # Start the client
    bot.client.run(TOKEN)

driver.quit()