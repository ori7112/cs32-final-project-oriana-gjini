# CS32 Final Project - Programming a Smart Thermostat

## Context of the Problem ##

The idea for this project came out of a situation my family often discusses. Like many households, we have AC supplied by a local energy provider. We live in Northern Illinois where ComEd is the prominent energy provider. ComEd is a unit of the Chicago-based Exelon Corporation: the largest electric utility in Illinois<sup>1</sup>. For my area code and many nearby, ComEd is the main energy provider.

Like any energy provider, ComEd is concerned about maintaining their electrical grid. They make a commitment to customers that they will supply energy whenever needed. However when high loads on the grid occur, ComEd must find ways to lower the load (lower energy usage) or else the grid will be overloaded and nobody will be able to receive electricity.

The main culprit of high loads are during the summer, particularly during the hottest days, at the hottest hours. Unlike heating which can be supplied by natural gas, AC must be supplied by electricity. On sweltering summer days, everybody turns on the AC and this is problematic for ComEd, again, because the high load puts strain on the grid.

It's a question of supply and demand but also a constraint of the electrical grid. Of course, ComEd can invest in a grid that can carry a greater electrical load, but such an investment isn't valuable when the risk of overloading the grid only occurs a handful of times a year during the hottest summer days.

ComEd's solution is creating two billing plans on electricity for customers to choose between.
* Option 1: Fixed-Price Rate

  - "With ComEd’s fixed-price rate, Rate BES (Basic Electric Service), you pay a fixed price for your electricity supply. This price varies by season; it is adjusted periodically but it does not change from hour to hour or from day to day. You pay the same price for electricity no matter what time of day or which day you use it.<sup>2</sup>"

* Option 2: Hourly Pricing Rate

  - "ComEd’s Hourly Pricing program, Rate BESH (Basic Electric Service Hourly Pricing), allows customers to pay an hourly price for electricity based on wholesale market prices. The price varies by the hour, and customers can manage their costs by shifting some of their electricity use to times when prices are lower (typically during night and weekend hours). Since most EV drivers charge overnight enrolling in ComEd's Hourly Pricing program allows customers to take advantage of lower prices and reduce your electric vehicle's fueling costs.<sup>2</sup>"

## Exploring the Problem ##

ComEd's hourly pricing rate is meant to incentivize saving energy by giving customers the opportunity to follow the load trends. Using 5 minute and hourly pricing charts avaliable on thier website, customers are encouraged to use electricity (e.g. turning on AC) when the load is down (lower price) and limiting energy consumption when loads are high (higher price).

My family was part of the program for many years, but it was difficult to keep monitoring prices and adjusting the thermostat as necessary. In the summer, before running the AC or running any high-energy consuming appliance/task, we would check the current pricing and the pricing predictions for the the upcoming hours. We would accordingly adjust our usage of electricity. Despite our efforts to follow the load trends, we could not overcome one detail of the hourly pricing rate plan. ComEd chooses a small selection of hours from the hottest days of the year, tracks your electricity usage from those hours, and creates a coefficient applied to your pricing on every monthly bill.

The idea is to encourage customers to lower energy usage during peak load times. To avoid a large coefficient to your energy bill, you'd like to avoid using electricity as much as possible during these peak times. The issue is, how does one predict these hours ComEd uses to calculate the coefficient? The other option would be to constantly keep an eye on the latest pricing updates every 5 minutes, but that is quite unreasonable.

ComEd's initiative is to save energy just as many people also try to be energy conscientious. While the hourly pricing program is theoretically made to reward saving energy, the introduction of significant coefficents created based on just a few hours from the peak load times has deincentivized the program because, despite good energy habits, a handful of hours from the hottest days when nearly everybody has the AC on determines your pricing for the entire year.

What was meant to be a win-win situation (ComEd keeps regulates the load on the grid and customers are rewarded with lower energy bills for following load trends)
has become a win-lose situation (ComEd regulates the load and makes extra money while hourly pricing rate customers attempt to save money but still pay higher bills than fixed price rate customers). What is more concerning is the increasing trend toward a lose-lose situation. As more customers are switching away from the hourly pricing rate to the fixed price rate plan, customers will not be as energy conscientious, ComEd will be at higher risk for grid overload, and profits will go down eventually causing increasing prices for customers.

## A Solution ##

A proposed solution is to create a program that can factor load and price to control when your thermostat is turned on or off. We can take a variety of data provided by ComEd and perhaps even weather data, store this data, analyze it, and subsequently determine when to turn your thermostat on/off. The program would be targeted the historically hottest months of June, July, and August. It would also specifically target hours of the daytime when temperatures reach their peak for the day.

The system can become quite complex, and just to give an idea of how sophisticated the system could become, here are some aspects that could go into the creating this system:

* Data Collection:
  - Take live data from hourly or 5 minute pricing from ComEd website
  - Take historical data (past years' pricing trends) from ComEd website
  - Historical Load data from ComEd website
  - Weather data (e.g. present, predictive, historically on this day)
* Store data in an efficient manner, keeping track of it and readily being able to access that data
* Algorithim for making meaningful conclusions from data
  - We could compare data to a threshold value and determine whether or not to turn the thermostat on/off
  - We could give different data types varying weight in the overall calculation
  - We could take derivatives of varying frequency of pricing data and/or load data and set parameters for turning the thermostat on/off based on severity of positive/negative slope or repeated slope increases/decreases
  - Using purely predictive data using weather forecasts and pricing predictions for the upcoming day, make an alogorithim that predicts a plan of when to turn the thermostat on/off for the day
 * Integrating AI
    - Utilizing Google's AI search engine to support better data collection
    - Making the system itself one that learns from its past actions
      - How successful was the system in past days with saving energy based on monitoring trends?
      - Was there a common pattern/situation that the system failed to account?
      - How can the system improve its abilites by learning from past errors and improving?
 * Creating graphs, charts, and reports for the user to view
 * Creating a GUI to make the program more interactive for the user
 * Making a "smarter" program that tries to regulate the temperature in the home by determining strategic times to turn on AC to compensate for upcoming high loads where the thermostat will be turned off
 * Connecting the program to the thermostat over WIFI

Clearly, there are many ways to improve and customize this concept. I hope this final project will give me a start in exploring the possibilities of creating such a system, one that has promising benefits to a real-world problem I have personally faced.

*Fun Fact: Smart Grids are being developed to solve the problem of managing load on grids. While very expensive and not overwhelmingly in use yet, they have great potential for saving energy, lowering costs for consumers and providers, preventing peak loads, and reducing CO2 levels due to the lowered consumption of energy. The system I outlined tries to accomplish similar goals to the smart grid but does it by controlling the thermostat rather than managing at the grid level.*

## The Computational Subtask ##

My goal will be to interact with ComEd's website (https://hourlypricing.comed.com/hp-api/), retreive data from pricing reports through communicating back and forth from my server to theirs, store this data locally, and analyze the data (as it comes in) to signal a thermostat to stay/turn on or off. In addition to gathering and producing the current price, the average current hour price, and the average past hour price for the user to view, the data gathered will be visualized through a line graph tracking the changes in price by the hour for the entire day.

The data used to determine what state the thermostat is in will depend on 2 main pieces of information.

* One, is the current price which is taken from ComEd's live 5 min pricing reports. The current price collected by our code will update every 5 min to have the most up-to-date pricing. 
* Second, is the change in price between the average current hour price and the average past hour price. 
  - The current hour price is taken from ComEd's live hourly pricing report. 
  - The past hour average must be calculated manually. 
  - Through a custom link where one sets the date and time, we can get 5 min pricing reports for specific intervals of time. By keeping track of the time in Illinois (CST/CDT), we can determine when the past hour starts/end and set an algorithm to calculate averages of 12 (5 min) prices to get the hourly average. 
 
Both the **current price** and the **change in price between the past hour versus the current hour** provide two factors to consider when assessing whether it is better to turn the thermostat on or off. These respective values will also be weighted based on how influential that information should be in determining the state of the thermostat. The 2 weighted values will ultimately be added together. The final score will be judged on a range, so depending on where the score lies, this will indicate a response of "THERMOSTAT IS: ON" or "THERMOSTAT IS: OFF".

Besides giving the user information on where the price is at, how it has changed over time, and giving an output after analyzing both types of data, we will also help visualize the prices through a line graph. Each day, average hourly prices are continually stored in order to produce a line graph that depicts prices over time. Every hour's average prices is plotted, eventually producing a 24 hour graph of how the prices changed throughout the day. It is a convenient way for the user to see how significantly the prices are changing, if they tend to be rising/droping, and may assist in predicting where the prices seem to be going.

In the end, my hope is that the scale of the project should challenge me in a variety of areas. I will have to webscrap, store data (e.g. dictionaries, arrays, lists), covert between the different objects, communicate with servers, utilize json files, convert HTML to python, create algorithms, carefully construct looping structures, monitor time, convert dates/times between timezones and milliseconds, create a line graph, and have the program run on a timed system which monitors itself.

Looking to the future, I hope that the scale of this project will capture the potential of a program that can utilize data to help us be better energy consumers by the simple, but powerful, method of predicting when to turn one's thermostat on or off.

Sources:

<sup>1</sup> https://www.comed.com/AboutUs/Pages/CompanyInformation.aspx

<sup>2</sup> https://www.comed.com/SmartEnergy/InnovationTechnology/Pages/RateOptions.aspx

## Prototype Outline ##

The scope of the project will remain as outlined in **The Computational Subtask**. We will have five major parts.

**Part 1** is webscrapping in preparation for data collection. This is where we go to ComEd's website, identify the links of interest, open these links, so that we will be ready to extract and store the data in the next part. We will access two links on ComEd's page. One is the live 5 min pricing and the second is the live average current hour pricing.

**Part 2** is collecting the current price. This is the first major piece of data to be used in the final calculation. We will get this information, updated every 5 min, from ComEd's live 5 min pricing link. 

**Part 3** is collecting the average current price and average past hour price. The change between these prices will be calculated in a following part. Part 3 is collecting all the data necessary to get the second major piece of data to be used in the final calculation. This part will be broken down into 3 steps.
* Step 1: Collect average current hour price (similarly to current price) by getting data from ComEd's live average current hour pricing link. 
* Step 2: Collect past hour prices by gathering 12 prices (each posted at 5 min intervals for the hour), utilizing a custom url. One of the reports ComEd can provide is given by a link that will open a json file with prices for a set start and end date/time. In the url, one must provide the start and end date/time in a specific format. Before we can use this link, we have to determine what the start and end date/time is. 
  - Because ComEd operates only in Northern Illinois, it makes sense to base date/time in CST/CDT. Since we are in EDT, we have to covert the current date/time to match CST/CDT. We can do this a few substeps.
    - 1. Get current date/time (EDT) in milliseconds and subtract two hours. Subtracting 1 hour gives us the current date/time in CDT. Subtracting a second hour gives us the past hour in CDT.
    - 2. Covert past hour date/time (CDT) to a datetime format. The reason for this is because ComEd's pricing reports are json files which are refereced by milliseconds UTC and because we need to recognize 5 min or hourly intervals of time, any date/time we use needs to be rounded. Specifically, since we are looking for the start and end of the past hour, we need to have the date/time we already got, rounded down to the hour. Right now, the raw date/time has hour, minutes, and seconds. We only want the hour.
    - 3. Once we have the date/time in a datetime format, we strip off the minutes and seconds. We are now ready to convert the date/time back to milliseconds.
    - 4. Convert date/time indicating start of the past hour (on the hour) to milliseconds. Because datetime format uses dashes and colons, we have to replace them by removing them. Additionally, numbers for hours and minutes must be added to the datetime since ComEd needs the date start and date end to be in YYYYMMDDHHMM.
    - 5. Repeat substeps 1-4 to get date/time for the end of the past hour. The only difference is that in substep 1, we only subtract 1 hour (not 2) since the end of the past hour is the start of the current hour.
    - 6. With date/time for the start and end of the past hour ready, we insert them into the ComEd custom url. There should be 12 prices in the json file given by this link (12 prices since these prices are posted every 5 min for the hour).
    - 7. Finally, we collect all 12 prices into an array to eventually be averaged to produce an average past hour price.
* Step 3: Calculate average past hour price. The array with all 12 prices for the past hour is reformatted as a list with float values (each price is rounded to one decimal place). This list goes through a function called "Average" and
  
  - Based on the data stored of times and prices, we will do a comparison against a benchmark price. If the price is equal to or greater than the benchmark price, the output will be "off" to turn off the thermostat. If the price is below benchmark, the output will be "on", indicating the thermostat should be on.

### Part 1: Webscrapping ###
**Step 1:** Connect to URL of ComEd page.
```
import requests
import json
import matplotlib.pyplot as plt
import pytz
import time
import urllib.request 

from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from urllib.request import urlopen

# designate website to collect data from
url = 'https://hourlypricing.comed.com/hp-api/'

# establish connection to website & check for 'response 200'
check_connection = requests.get(url)
print("Response status:", check_connection) 

# parse HTML and locate every 'a' which find every instance
# of '<a' which is the tag for a link
soup = BeautifulSoup(check_connection.text, 'html.parser')
soup.findAll('a')

# assign the line with the 5 min pricing link
get_link_min = soup.findAll('a')[32]

# specifically assign the 5 min pricing link
# by identifying it from the HTML line
link_min = get_link_min['href']

# assign the line with the current hour price link
get_link_hour = soup.findAll('a')[43]

# specifically assign the current hour pricing link
# by identifying it from the HTML line
link_hour = get_link_hour['href']
```
The last line `print(response)` is a check to make sure the connection was successful. When running this code, we get `<Response [200]>` which means we have successfully connected.

**Step 2:** Parse HTML script to locate link of interest (link contains 5 min pricing data). Then, assign the link for use in next step.
```
# parse HTML and locate every 'a' which find every instance
# of '<a' which is the tag for a link
soup = BeautifulSoup(response.text, 'html.parser')
soup.findAll('a')

# show every code line that contains a link
print(soup.findAll('a'))

# assign the line with the link we want as link_tag
link_tag = soup.findAll('a')[33]

# show link_tag to verify this line contains the link we want
print(link_tag)

# specifically assign the link by identifying it from the HTML line
link = link_tag['href']

# show the link to make sure we have the right one
print(link)

```
This portion correctly meets the 3 print statement checkpoints. The first print `print(soup.findAll('a'))` produces every link from the website's HTML. The second print `print(link_tag)` correctly gives the HTML line that contains the link of interest. Finally, the third print `print(link)` takes the link of interest out of the HTML line. We get `https://hourlypricing.comed.com/api?type=5minutefeed&format=text` printed and this is the link we want to extract data from.

**Step 3:** Open the link to the 5 min pricing data. Reproduce all the data so it is ready for analysis. The link should be opened every 5 minutes to extract the updated data.
```
#PLACE EVERYTHING IN A LOOP

# every 5 min start at the beginning of the loop -- use time.sleep 

# open the link, access data, print data
f = urlopen(link)
myfile = f.read()
print(myfile)

# delete all data in previously created array (array should be created before loop)
# store new data into an array
   # data comes in a set of UTC millis and price, and should be stored accordingly

```
Currently, the code above prints all the data from the file once. **Step 3** needs to incorporate a loop to access the link with the data every 5 min (5 min is how often the link is updated with new data). Every 5 min, the new data will go into an array for storage and any previous data will be deleted. Now that we have our necessary data stored, we will be able to analyze in **Part 2**.

### Part 2: Data Analysis ###

In **Part 2**, we will do comparison tests with the data we stored in **Part 1**. Specifically, every 5 min when new data comes in, we will conduct a test with a threshold price value. If the price at the most recent time recorded is *at or above* a benchmark value, the output will be "off" indicating the thermostat should be turned off. If a real thermostat was connected, this output would signal for the thermostat to be turned off automatically. If the price at the most recent time recorded is *below* a benchmark value, the output will be "on". 

The code can utilize `pop` to take the last value in the array and use it in a series of if/elif/else blocks to see if the value is greater than, equal to, or less than the benchmark value. Based on which block is entered, the code will produce an output, either "on" or "off".



The intention of taking two types of input (current price and slope between current and past hour prices) is to begin emulating the importance of factoring in multiple types of data. Using some basic algorithms and calculations also begins to demonstrate the importance of effective analysis of data. While the calculations used are not terribly sophisticated and the weighing system is not supported by much data other than my personal experience of how the pricing tends to work, I believe working with calculations revealed to me how powerful they can be. Additionally, I realized that creating an algorithm that accurately makes sense of data and uses it effectively is very tricky. It takes a lot of consideration, research, and trial and error. 
