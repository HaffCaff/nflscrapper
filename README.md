# nflscrapper
Using praw, scrape game threads for popular buzzwords and create bar graph to visualize

![Alt text](scrapperscreenshot.png?raw=true "screenshot")


*A user at my schools programming club made something similar to this summer semester of 2022 for soccer. I remember them posting about it in our club discord. They day of the championships I thought it would be cool to write while I watched but I wanted to try and keep my process as original as possible so I did not go back and look at their post. Now that I have this fleshed out, I am going to backtrack and see if they have their own repo with their implementation! tl;dr: This idea is not mine, the scraping was done following the guide below, the logic for cleaning the scaped data is what I came up with!*

I cannot take credit for the scraping, I followed this awesome guide on praw: https://www.geeksforgeeks.org/scraping-reddit-using-python/
You need to create a reddit app in order to fill out client_id, client_secret, and the user id


# How to Use:

URL: This is important, fill this with URL of the reddit thread that you are going to scrape. I wrote this during the AFC and NFC championships, and plan to tune it and use again during superbowl!

Buzzwords: You can technically use any reddit thread you want! Until I optimize it a bit, I use a pre determined list of keywords to look for. Depending on what you want to use it for, you can change it to match your needs!

