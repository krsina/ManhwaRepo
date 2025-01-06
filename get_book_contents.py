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

# Set up Chrome options for running in headless mode
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--headless=new")

# Set up the driver with the Chrome options
driver = webdriver.Chrome(options=chrome_options)

# Read the book links from the books.txt file
with open("books.txt", "r") as file:
    book_links = file.read().splitlines()


# Iterate over the book links
for book_link in book_links:
    # Load the book page
    driver.get(book_link)

    # Wait for the latest chapter link to appear
    chapter_div_locator = (By.XPATH, "//div[h3[text()='New Chapter']]")
    chapter_div_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located(chapter_div_locator))
    chapter_number = chapter_div_element.find_element(By.CSS_SELECTOR, "span.pl-\\[1px\\]").text
    print("Chapter Number:", chapter_number)
    print()

    # Find the specific div element
    book_description_div_locator = (By.CSS_SELECTOR, "div.relative.z-10.grid.grid-cols-12.gap-4.pt-4.pl-4.pr-4.pb-12")
    book_description_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located(book_description_div_locator))

    # Find and print the text within the specific span element inside the div
    book_title_locator = (By.CSS_SELECTOR, "span.text-xl.font-bold")
    book_title = book_description_element.find_element(By.CSS_SELECTOR, "span.text-xl.font-bold").text
    print("Book Title:", book_title)
    print()

driver.quit()