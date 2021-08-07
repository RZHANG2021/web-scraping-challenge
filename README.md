# web-scraping-challenge
web-scraping


Step 1 - Scraping
Utilizing Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter to complete the initial scraping
A Jupyter Notebook file called mission_to_mars.ipynb was created and used to complete all of the scraping and analysis tasks. 
Four websites were scrapped: 
1.1 NASA Mars News 
Scrape the Mars News Site and collect the latest News Title and Paragraph Text. 
1.2 JPL Mars Space Images – Featured Image
•	the url for the Featured Space Image site is here.
•	Splinter function was used to navigate the site and find the image url for the current Featured Mars Image,  and the url string was assigned to a variable called  featured_image_url.
1.3 Mars Facts 
•	the Mars Facts webpage is here 
•	Pandas was used to scrape the table containing facts about the planet including Diameter, Mass, etc.
•	The data then was converted to a HTML table string.
•	1.3 Mars Facts 
1.4 Mars Hemispheres
•	the astrogeology site here , high resolution images for each of Mar's hemispheres were obtained by clicking on each of the links to the hemispheres in order to find the image url to the full resolution image.
•	Both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name were stored in a dictionary using the keys img_url and title.
•	A list then was created to append the dictionary with the image url string and the hemisphere title . This list contains one dictionary for each hemisphere.

________________________________________
Step 2 - MongoDB and Flask Application
A new HTML page was created using MongoDB with Flask templating, which displays all of the information that was scraped from the URLs 
•	the Jupyter notebook was converted into a Python script called scrape_mars.py with a function called scrape that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.
•	a route called /scrape was created to import scrape_mars.py script and call the scrape function.
•	the return value was stored in Mongo as a Python dictionary.
•	a root route / was also created to query Mongo database and pass the mars data into an HTML template to display the data.
•	a template HTML file called index.html was created which take the mars data dictionary and display all of the data in the appropriate HTML elements. 
The final web site looks like the below:
