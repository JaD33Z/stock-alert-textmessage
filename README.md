# stock-alert-textmessage
App for tracking stock prices daily that sends text notifications with info and current news articles regarding chosen companies.

The text message you recieve includes and compares differences between info regarding closing price, percentages in rise/drop in the companies
you choose and the links to the recent news articles involving those companies.

You will need an alphavantage api key for the stock data access and an news api key for the related articles.

Use https://www.alphavantage.co/ api to access data feeds of companies and their stock market info.
In Alpha Vantage, many of the top technical indicators used by professional traders can be accessed with a basic structure.

"Backed by the prestigious Y Combinator and composed of a tight-knit community of researchers, engineers,
and business professionals, Alpha Vantage Inc. has partnered with major exchanges and institutions around the world
to become a leading provider of stock APIs as well as forex (FX) and digital/crypto currency data feeds. 
Our success is driven by rigorous research, cutting edge technology,
and a disciplined focus on democratizing access to data."
                                                         - https://www.alphavantage.co/

Twilio is what we will use to send the SMS notifications from our program.

Twilio allows software developers to programmatically make and receive phone calls, send and receive text messages, and perform other communication functions using its web service APIs


The steps this particular app performs: 
		
		- Get yesterday's closing stock price. perform list comprehensions on Python dictionaries.
        e.g. [new_value for (key, value) in dictionary.items()]          
		
		- Get the day before yesterday's closing stock price,
		    the positive difference between both days
			
		- Work out the percentage difference in price between 
        closing price yesterday and closing price the day before yesterday.
		
		- Use the News API to get articles related to the COMPANY_NAME.
		
		- Use Python slice operator to create a list that contains the first 3 articles.
		
		- Create a new list of the first 3 article's headline and description

		- Send each article as a separate message via Twilio.
    
    (steps are also documemented in main.py)
    
    
    
    
    
    
    
    
