# Psychometric Analysis of Tweets

For one of my writing class, I analyzed world leaders and their online behaviors. 

## How and why I came up with the project:
I was intrigued how world leaders are putting out random tweets and blurring the idea of online/Twitter diplomacy. The idea later led to full story on how world leaders are ruining Twitter diplomacy by showcasing and engaging in verbal spat on Twitter. I took three world leaders for the story. Narendra Modi, Donald Trump and Pope Francis ~believe me they are the best when it comes to tweeting~. 

## How did I scrape off Tweets?

No tricks, just usual selenium script. I have attached the Selenium script here. You can use the same just add your API credentials and the Twitter username of the person you want to scrape. 

Use Tweet dumper to extract tweets of any user of Twitter, make sure to enter dates within the file. 
Also, set the API keys before going ahead.

## But what after scraping?

Well, that is easy. Just read this before I start off with jargons: 
(LIWC Analysis)[http://journals.sagepub.com/doi/pdf/10.1177/0261927X09351676]

In short, Language Inquiry and Word Count is a type of psychometric analysis. The analysis allows user to categorize words in accordance to psychological meaning. The end result obtained from the analysis is used to demonstrate a wide variety of experimental emotional and behavioral settings, including to show attentional focus, emotionality, social relationships, thinking styles, and individual differences.

### After extracting tweets follow this:
After, you've extracted the tweets use the extracted csv file in sentiment.py.

In the end you should get a .csv file with values 0 and 1 assingning to the corresponding LIWC categories. Use the csv file to merge with the LIWC dictionary. 


## If you think this was useless, always remember some things said and tweeted have no meaning:

In the tweets of Donald Trump:

> Despite the constant negative press covfefe
