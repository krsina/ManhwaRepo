from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from typing import List
from typing import Dict
import re

def get_latest_chapters(links: List[str]) -> Dict[str, Dict[str, str]]:
    # initialize the dictionary to store the results
    latest_chapters = {}

    # set up the driver
    driver = webdriver.Chrome()

    # loop through each link in the array
    for link in links:
        # get the title of the manhwa from the link
        title = link.split("/")[-2]
        
        # Use regular expression to remove any digits and dashes from the title
        title = re.sub(r'[-\d]+', ' ', title).title().lstrip();


        # navigate to the manhwa's page
        driver.get(link)

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

        # add the latest chapter number and link to the dictionary
        latest_chapters[title] = {"latest_chapter_number": chapter_number, "latest_chapter_link": latest_chapter}

    # quit the driver
    driver.quit()

    # return the dictionary
    return latest_chapters

links = ["https://www.asurascans.com/manga/1672760368-genius-of-the-unique-lineage/",
         "https://www.asurascans.com/manga/1672760368-existence/"]

latest_chapters = get_latest_chapters(links)

for title, chapter_info in latest_chapters.items():
    print(title)
    print("Latest chapter number:", chapter_info["latest_chapter_number"])
    print("Latest chapter link:", chapter_info["latest_chapter_link"])
    print()