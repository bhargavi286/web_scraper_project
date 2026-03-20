import schedule
import time
from scraper import scrape_data

def job():
    print("Running scraper...")
    scrape_data()

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)