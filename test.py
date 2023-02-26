from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# set up the driver
driver = webdriver.Chrome()
driver.get("https://www.asurascans.com/manga/1672760368-genius-of-the-unique-lineage/")

# wait for the latest chapter link to appear
chapter_locator = (By.CSS_SELECTOR, ".lastend .inepcx:last-child a")
latest_chapter_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(chapter_locator))

# get the href attribute of the latest chapter link
latest_chapter = latest_chapter_link.get_attribute("href")

# extract the chapter number from the link
chapter_number = ""
for i in range(len(latest_chapter)-1, 0, -1):
    if latest_chapter[i] == "-":
        chapter_number = latest_chapter[i+1:len(latest_chapter)-1]
        break

# print the latest chapter link
print("Latest chapter:", latest_chapter)
print("Chapter number:", chapter_number)

# quit the driver
driver.quit()