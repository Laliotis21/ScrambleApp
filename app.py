import cfscrape
from bs4 import BeautifulSoup

def anti_bot_scraping():

    target_url = "https://www.spitogatos.gr/"   # replace url with anti-bot protected website
    scraper = cfscrape.create_scraper()
    html_text = scraper.get(target_url).text
    parsed_html = BeautifulSoup(html_text, 'html.parser')
    print(parsed_html)

if __name__ == '__main__':
    anti_bot_scraping()