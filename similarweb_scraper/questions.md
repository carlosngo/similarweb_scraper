Questions & Answers
1. Open the websites that we scrapped for you in a browser, you’ll notice that there are more details on the screen than there are in the HTML provided. Where does that extra data come from? How would you extract that information?

The extra data comes from the CSS and JavaScript files generated during the production build of React. 
The HTML file fetches these files through `<script>` and `<style>` tags, so one way we could 
extract this information is to crawl the files specified by the `src` attribute of the said tags.

2. Many website operators put preventions in place to prevent websites from being scraped. One such prevention is to return a 429 status code; what does this mean and how could it be circumvented?

The 429 HTTP response is sent if the server detects that we have sent too many requests in quick succession. This is a 
security feature to prevent spam from bad actors. Correctly set up servers send a Retry-After HTTP header along with the
response; this indicates how long should we wait to send a follow-up request. To circumvent this, we can retry 
sending the request after the amount of time indicated by the Retry-After header.    

3. We run scrapes continuously, both on the same websites as data changes over time and on new websites that we find interesting. How would you monitor the activity of the scrapers to make sure they were functioning and functioning correctly?

To check if our scrapers are functioning and functioning correctly, we can set up a monitoring platform like Sentry to 
check for errors. We can alternatively set up logging in our application and monitor the logs to ensure every core
workflow is working as expected.

4. To scale we need website scrapes to fetch data automatically. How would you organise your code to fetch data automatically? How would you update your database? What would you need to watch out for?

If we want to fetch data automatically, we can set up triggers that will execute the code if certain 
conditions are met or in an interval. 

Currently, the one-to-many relationships, such as the top countries, are flattened to fit in one csv file. 
Without the constraint of using only one csv file, we can set up a more complex schema to handle one-to-many and 
many-to-many relationships, as well as complex queries, better.

Currently, the code does not correctly handle dynamic dates in the website; if the graphs show other months besides 
October-December 2022, the code will not work as expected. Moreover, if the shape of the "data" object that the code 
extracts data from changes (i.e. a developer changes the name of a key), the code will not work as expected. A lot of
things can go wrong with systems we have no direct control over, and this further emphasizes the importance of 
establishing proper infrastructure to monitor our scrapers if we want to scale. 




