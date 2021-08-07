
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from webdriver_manager.chrome import ChromeDriverManager

# # Scrape website to get NASA Mars News science


def scrape_all():
    # Setup splinter and initialize Chrome broswer
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    web_content={}

    # # Scrape website to get NASA Mars News science

    #URL of page to be scraped
    article_url='https://redplanetscience.com/'
    browser.visit(article_url)



    #create BeautifulSoup object;parse with 'html.parser'
    html=browser.html
    soup=bs(html,'html.parser')

    Title=soup.body.find_all('div',class_='content_title')[0].get_text()
 
    Article=soup.body.find_all('div',class_='article_teaser_body')[0].get_text()
    Article


    # # Scrape website spaceimages-mars

    #URL of page to be scraped
    fullimage_url='https://spaceimages-mars.com/'
    browser.visit(fullimage_url)



    html=browser.html
    soup=bs(html,'html.parser')

    button = browser.links.find_by_partial_text('FULL IMAGE')
    # Interact with elements
    button.click()


    link=soup.find('img', class_='headerimage fade-in')['src']
    featured_image_url=fullimage_url+link
    # print(featured_image_url)


    # # Scrape Mars Facts


    #connet to Mars Facts
    facts_url = "https://galaxyfacts-mars.com/"
    browser.visit(facts_url)

    #start to scrap the table from Mars Facts
    html = browser.html
    soup = bs(html, "html.parser")
    mars_facts = pd.read_html("https://space-facts.com/mars/")[1]
    # print(mars_facts)



    # mars_facts.set_index(['Mars - Earth Comparison'])
    mars_facts= mars_facts.set_index(['Mars - Earth Comparison'])
    # print(mars_facts)

    facts = mars_facts.to_html()
    # print(facts)

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
        
        #  find image urls  
            image_urls="https://marshemispheres.com/"+soup.find('img', class_='wide-image')['src']

        # find image titles     
            title=soup.find('h2').get_text()

        
            hemisphere_image_url={"title":title,"image_url":image_urls}  
        # print (hemisphere_image_url)
        
        # set up a dictionarie and store title and img_url
            hemispheres = {"title": title,"img_url": image_urls}        

        # append individual hemispheres into a list
            hemisphere_image_urls.append(hemispheres )
        

        #  click back to the initial website
            browser.back()
    
        except:
            print("item is not found")



    # web_content =   {
    #         "news_title": Title,
    #         "news_paragraph": Article,
    #         "featured_image": featured_image_url,
    #         "facts": facts,
    #         "hemispheres": hemisphere_image_urls
    # }
    
    web_content['news_title'] = Title
    web_content['news_paragraph'] = Article
    web_content['image_url'] = featured_image_url
    web_content['table'] = facts
    web_content['hemisphere_image'] = hemisphere_image_urls
    
    # stop webdriver and return data
    browser.quit()
    
    # browser.quit()
    
    return web_content
