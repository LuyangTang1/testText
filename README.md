# testText
Project introduction:

    Using Scrapy spider to get information from www.awwwards.com website.

Tools:

    Scrapy spider, Python

Source website:

    https://www.awwwards.com/websites/css3

Content of scrapy:

    All webpage items contained in the first 5 pages of the source website
    
	Each item include:
	
	(1) web_name: The name of each example website of best design with CSS
	
        (2) web_tag: The tag of each example website
	
        (3) web_author: The author of each example website
	
        (4) web_date: The build date of each example website
	
        (5) web_URL: The URL of each example website
	
	

Output format:

    An csv file called "output.csv"

Operational process:

    (1) Open the prompt or terminal
    
    (2) Direct to the "testText" folder (cd C:\xxxxx\...\xxxxx\testText)
    
    (3) Run:"scrapy crawl awwwards -o output.csv"
    
    (4) Complete scrapy and get the output.csv file
