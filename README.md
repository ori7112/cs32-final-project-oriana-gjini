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

My goal will be to interact with ComEd's website (https://hourlypricing.comed.com/hp-api/), retreive data from the 5 minute live pricing report through communicating back and forth from my server to theirs, store this data locally, and compare the data (as it comes in) to a threshold price. If the price exceeds the threshold value, an output message is produced which would tell the thermostat to turn off. When the price returns below the threshold price, an output message will be produced which would tell thermostat to turn on.

This captures the idea of the system I previously outlined, but it is a simplified version taking one type of data and analyzing it by comparison to a threshold value. 

Sources:

<sup>1</sup> https://www.comed.com/AboutUs/Pages/CompanyInformation.aspx

<sup>2</sup> https://www.comed.com/SmartEnergy/InnovationTechnology/Pages/RateOptions.aspx

## Prototype Outline ##

The scope of the project will remain as outlined in **The Computational Subtask**. We will have two major parts. **Part 1** is webscrapping, data collection, and data storage. This is where we go to ComEd's website, identify the link of interest, open this link, extract the data, and store the data. We will store a data for what the price of electricity is at what time. Then, **Part 2** is analysis of data and outputing on/off result. Based on the data stored of times and prices, we will do a comparison against a benchmark price. If the price is equal to or greater than the benchmark price, the output will be "off" to turn off the thermostat. If the price is below benchmark, the output will be "on", indicating the thermostat should be on.

### Part 1: Webscrapping ###
**Step 1:** Connect to URL of ComEd page.
```
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# designate website to collect data from
url = 'https://hourlypricing.comed.com/hp-api/'

# establish connection to website
response = requests.get(url)

# check that we get 'response 200' to ensure successful connection
print(response) 
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
