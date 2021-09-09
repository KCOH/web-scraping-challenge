from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

# --- Mars News ---
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()

    # --- Visit Mars News site ---
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    news_title = soup.find("div",class_="content_title").text
    news_paragraph = soup.find("div", class_="article_teaser_body").text
    print(f"Title: {news_title}")
    print(f"Para: {news_paragraph}")


    
# --- Visit JPL site for featured Mars image ---
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)      

def featured_image(browser):

    url_image = 'https://spaceimages-mars.com'
    browser.visit(url_image)

    # Scrape page into Soup
    html_image = browser.html
    soup_image = BeautifulSoup(html_image, 'html.parser')

    # Search for image source
    image = soup_image.find_all('img', class_='headerimage fade-in')[0]['src']
    featured_image_url = f'{url_image}/{image}'
    featured_image_url


# --- Use Pandas to scrape Mars Space Facts ---
    tables = pd.read_html('https://galaxyfacts-mars.com')

    # Take second table for Mars facts
    mars_facts = tables[1]

    # Rename columns and set index
    mars_facts.columns=['Mars', 'Parameters']
    
    # Convert table to html
    mars_facts_table = mars_facts.to_html(classes='data table table-borderless', index=False, header=False, border=0)
    mars_facts_table

# --- Mars Hemispheres
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)     

def hemisphere(browser):
    # Visit the USGS Astrogeology Science Center Site
    url = 'https://marshemispheres.com'
    browser.visit(url)
    mars_hemisphere_html = browser.html
    mars_hemisphere_soup = BeautifulSoup(mars_hemisphere_html, 'html.parser')

    items = mars_hemisphere_soup.find_all('div', class_='item')
    hemisphere_image_url = []

    for item in items:
        image_title = item.h3.text
        image_description = item.p.text
        image_href = item.a['href']
        browser.visit(f'{mars_hemisphere_url}/{image_href}')
        image_html = browser.html
        image_soup = BeautifulSoup(image_html, 'html.parser')
        image_url = image_soup.find('div', class_='wide-image-wrapper').img['src']
        full_image_url = f'{mars_hemisphere_url}/{image_url}'
        d = {'title': image_title, 'img_url': image_url}
        hemisphere_image_url.append(d)
    hemisphere_image_url
  