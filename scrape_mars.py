
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests
from webdriver_manager.chrome import ChromeDriverManager

# # Scrape website to get NASA Mars News science

def scrape_all():
    # Setup splinter and initialize Chrome broswer
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    Title,Article = mars_news(browser)
    featured_image_url = featured_image(browser)
    facts = mars_facts()
    hemisphere_image_urls = hemispheres(broswer)

    #run all scraping functions and store results in a dictionary
    web_content={
        "news_title": Title,
        "news_paragraph": Article,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": hemispheres(broswer)
    }

    # stop webdriver and return data
    browser.quit()

def mars_news(browser):

    #URL of page to be scraped
    article_url='https://redplanetscience.com/'
    browser.visit(article_url)

    #convert the broswer html to a soup object ;parse with 'html.parser'
    html=browser.html
    soup=bs(html,'html.parser')

    Title=soup.body.find_all('div',class_='content_title')[0].get_text()

    Article=soup.body.find_all('div',class_='article_teaser_body')[0].get_text()


    return Title, Article



# # Scrape website spaceimages-mars

def featured_image(browser):

    #URL of page to be scraped
    fullimage_url='https://spaceimages-mars.com/'
    browser.visit(fullimage_url)

    html=browser.html
    soup=bs(html,'html.parser')
    
    # Interact with elements
    button = browser.links.find_by_partial_text('FULL IMAGE')
    
    button.click()

    link=soup.find('img', class_='headerimage fade-in')['src']
    featured_image_url=fullimage_url+link
    
    return featured_image_url


# # Scrape Mars Facts

def mars_facts():

    #connet to Mars Facts
    facts_url = "https://galaxyfacts-mars.com/"
    browser.visit(facts_url)

    #start to scrap the table from Mars Facts
    html = browser.html
    soup = bs(html, "html.parser")
    mars_facts = pd.read_html("https://space-facts.com/mars/")[1]
    mars_facts.set_index(['Mars - Earth Comparison'])
    facts = mars_facts.to_html()
    return facts

# #  Scrape website marshemispheres

def hemispheres(broswer):


    #URL of page to be scraped
    marshemispheres_url="https://marshemispheres.com/index.html"
    browser.visit(marshemispheres_url)

    html=browser.html
    soup=bs(html,'html.parser')

    links=soup.find_all('h3')
    len(links)


    # set up a empty list to store individual dictionaries
    hemisphere_image_urls = []

    # loop through the website to collect each link and image url
    for i in range(len(links)):

        try:
            images=browser.find_by_tag('h3')
            images[i].click()
            html=browser.html
            soup=bs(html,'html.parser')

            # find image urls  
            image_urls="https://marshemispheres.com/"+soup.find('img', class_='wide-image')['src']

            # find image titles     
            title=soup.find('h2').get_text()


            hemisphere_image_url={"title":title,"image_url":image_urls}  
            print (hemisphere_image_url)

            # set up a dictionarie and store title and img_url
            hemispheres = {"title": title,"img_url": image_urls}        

            # append individual hemispheres into a list
            hemisphere_image_urls.append(hemispheres )


            #click back to the initial website
            browser.back()

        except:
            print("item is not found")



    return hemisphere_image_urls




