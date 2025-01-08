import BaseScraper
import threading
# Define the configuration for AsuraScraper
configs = [
    {
        'book_links_file': 'books.txt',
        'book_desc_css': 'div.relative.z-10.grid.grid-cols-12.gap-4.pt-4.pl-4.pr-4.pb-12',
        'book_title_css': 'span.text-xl.font-bold',
        'chapter_link_css': 'div.pl-4.py-2.border.rounded-md.group.w-full.hover\\:bg-\\[\\#343434\\].cursor-pointer.border-\\[\\#A2A2A2\\]\\/20.relative'
    },
    {
        'book_links_file': 'books2.txt',
        'book_desc_css': 'div.relative.z-10.grid.grid-cols-12.gap-4.pt-4.pl-4.pr-4.pb-12',
        'book_title_css': 'span.text-xl.font-bold',
        'chapter_link_css': 'div.pl-4.py-2.border.rounded-md.group.w-full.hover\\:bg-\\[\\#343434\\].cursor-pointer.border-\\[\\#A2A2A2\\]\\/20.relative'
    }
]

def run_scraper(config):
    scraper = BaseScraper.AsuraScraper(config)
    scraper.scrape()
    scraper.close()


# Create and start a thread for each configuration
threads = []
for config in configs:
    thread = threading.Thread(target=run_scraper, args=(config,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()