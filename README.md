# ManhwaRepo

## Overview
Python script that scrapes information from AsuraScans and stores it in a MongoDB database. Integrated with Discord to send notifications when there are updates to the scraped data.

## Screenshots

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">

  <div style="flex-basis: 48%;">
    <img src="https://github.com/krsina/ManhwaRepo/blob/main/demo/added.PNG?raw=true" alt="Screenshot 1">
    <p>Message displayed when a book is added to the MongoDB database.</p>
  </div>

  <div style="flex-basis: 48%;">
    <img src="https://raw.githubusercontent.com/krsina/ManhwaRepo/main/demo/newchapter.png" alt="Screenshot 2">
    <p>Message displayed when a new chapter is found.</p>
  </div>

</div>


## Dependencies
- `discord.py`: Discord API wrapper for Python
- `selenium`: Web browser automation tool
- `pymongo`: MongoDB driver for Python
- `chromedriver`: Driver for Selenium

## Setup

1. **Install Dependencies:**
   - Download ChromeDriver from [here](https://sites.google.com/chromium.org/driver/).
   - Add file to project root.
   - Run this command in project root.
     ```bash
     pip install discord.py selenium pymongo
     ```

2. **Create a MongoDB Database:**
   - Install MongoDB and create a new database named 'library' with a collection named 'books'.

3. **Set Up Discord Bot:**
   - Create a Discord bot on the [Discord Developer Portal](https://discord.com/developers/applications).
   - Obtain the bot token and the channel ID where notifications will be sent.

4. **Configure `secret.json`:**
   - Create a file named `secret.json` in the project root.
   - Add the following content:

     ```json
     {
       "MONGODB_URI": "YOUR_MONGODB_URI",
       "DISCORD_KEY": "YOUR_DISCORD_BOT_TOKEN",
       "DISCORD_CHANNEL_ID": "YOUR_DISCORD_CHANNEL_ID"
     }
     ```

5. **Prepare Book Links:**
   - Create a file named `books.txt` containing AsuraScans book URLs, with each URL on a new line.
   - All file to project root.

6. **Run the Script:**
   - Execute the script by running the following command:

     ```bash
     python scrape.py
     ```
