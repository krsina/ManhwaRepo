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
driver.get("https://www.asurascans.com/manga/4569947261-genius-of-the-unique-lineage/")

# Wait for the latest chapter link to appear
chapter_locator = (By.CSS_SELECTOR, ".lastend .inepcx:last-child a")
latest_chapter_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(chapter_locator))

# Get the href attribute of the latest chapter link
latest_chapter = latest_chapter_link.get_attribute("href")

# Extract the chapter number from the link
chapter_number = ""
for i in range(len(latest_chapter) - 1, 0, -1):
    if latest_chapter[i] == "-":
        chapter_number = latest_chapter[i + 1: len(latest_chapter) - 1]
        break

# Print the latest chapter link
print("Latest chapter:", latest_chapter)
print("Chapter number:", chapter_number)

# Quit the driver
driver.quit()