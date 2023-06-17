from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
    latest_chapter_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(chapter_locator))

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
    print()

# Quit the driver
driver.quit()
