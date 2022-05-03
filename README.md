# CS32 Final Project - Programming a Smart Thermostat
Created by: Oriana Gjini

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

The scope of the project will remain as outlined in **The Computational Subtask**. We will have seven major parts.

**Part 1:** Webscrapping in preparation for data collection. This is where we go to ComEd's website, identify the links of interest, open these links, so that we will be ready to extract and store the data in the next part. We will access two links on ComEd's page. One is the live 5 min pricing and the second is the live average current hour pricing.

**Part 2:** Collecting the current price. This is the first major piece of data to be used in the final calculation. We will get this information, updated every 5 min, from ComEd's live 5 min pricing link. 

**Part 3:** Collecting the average current hour price and average past hour price. The change between these prices will be calculated in a following part. Part 3 is collecting all the data necessary to get the second major piece of data to be used in the final calculation. This part will be broken down into 3 steps.

* Step 1: Collect average current hour price (similarly to current price) by getting data from ComEd's live average current hour pricing link. 

* Step 2: Collect past hour prices by gathering 12 prices (each posted at 5 min intervals for the hour), utilizing a custom url. One of the reports ComEd can provide is given by a link that will open a json file with prices for a set start and end date/time. In the url, one must provide the start and end date/time in a specific format. Before we can use this link, we have to determine what the start and end date/time is.

  - Because ComEd operates only in Northern Illinois, it makes sense to base date/time in CST/CDT. Since we are in EDT, we have to covert the current date/time to match CST/CDT. We can do this a few substeps.

    1. Get current date/time (EDT) in milliseconds and subtract two hours. Subtracting 1 hour gives us the current date/time in CDT. Subtracting a second hour gives us the past hour in CDT.
    2. Covert past hour date/time (CDT) to a datetime format. The reason for this is because ComEd's pricing reports are json files which are refereced by milliseconds UTC and because we need to recognize 5 min or hourly intervals of time, any date/time we use needs to be rounded. Specifically, since we are looking for the start and end of the past hour, we need to have the date/time we already got, rounded down to the hour. Right now, the raw date/time has hour, minutes, and seconds. We only want the hour.
    3. Once we have the date/time in a datetime format, we strip off the minutes and seconds. We are now ready to convert the date/time back to milliseconds.
    4. Convert date/time indicating start of the past hour (on the hour) to milliseconds. Because datetime format uses dashes and colons, we have to replace them by removing them. Additionally, numbers for hours and minutes must be added to the datetime since ComEd needs the date start and date end to be in YYYYMMDDHHMM.
    5. Repeat substeps 1-4 to get date/time for the end of the past hour. The only difference is that in substep 1, we only subtract 1 hour (not 2) since the end of the past hour is the start of the current hour.
    6. With date/time for the start and end of the past hour ready, we insert them into the ComEd custom url. There should be 12 prices in the json file given by this link (12 prices since these prices are posted every 5 min for the hour).
    7. Finally, we collect all 12 prices into an array to eventually be averaged to produce an average past hour price.

**Part 4:** Calculate average past hour price. The array with all 12 prices for the past hour is reformatted as a list with float values (each price is rounded to one decimal place). This list goes through a function called "Average" and returns the average past hour price.

**Part 5:** Collect average hourly prices for today.

  - First, we get the date/time for CST/CDT and strip off the time to leave us with the date. Then, the dashes from the date are removed. To get YYYYMMDDHHMM format, we add in "0000" to indicate hour 0 or midnight. To get the end of the day's last 5 min price, we add "2355" to the date.
  - These date start and date ends are inserted into the custom url much like how we did this to get prices for the past hour. The only difference is that this custom url will give 288 prices by the end of the day, one for every 5 min in the 24 hours.

**Part 6:** Create a line graph of today's average hourly prices. The graph will depict prices vs. hour, up to 24 hours.

  - Because we want to create a line graph no matter what time of day it is, we create a loop that keeps adding prices from the json file given by our custom link. 
  - The prices are stored in a hourly price array. Once the array has 12 values (aka prices), we take the average and store that value (avgerage price of that hour) in to a separate array for the day's average hourly prices. This loop keeps running all day and the temporary hourly price array resets itself once it reaches 12 values.
  - This way, the day's average hourly price array collects the average hour price for every hour completed in the day so far. It thereby indicates how many hours have been recorded (number of prices determines should match how many hours have passed today). Another loop does this matching to ensure the number of x values (hours) matches the number of y values (prices).
  - The graph is created with a blue line, the appropriate headings, and will illustrate how the prices are changing throughout the day. Instead of just providing calculations, this graph makes it easy for the user to have a sense of how dynamically prices are fluctuating.

**Part 7:** Final Calculations to determine state of the thermostat.

  - The current price is assigned a weight depending on the range in which the prices falls. Any price below 5 cents gets weighted at 1.7 times it's value. Any price including 5 and below 10 cents gets weighted at 1.3 times it's value. Any price at or above 10 cents gets weighted at 1.7 times. The reason for the weighting is that any price below 5 cents is quite low and no matter what the change in hourly price is, this price is low enough to keep the thermostat on. Likewise, if the price is at or above 10 cents, that is quite high and is the priority consideration in turning the thermostat off. Whatever the current price is, it gets weighted accordingly and becomes `value_1`.
  - The change between average current hour price and average past hour price is calculated. This value is compared between 8 ranges. Depending on where the price falls, it gets assigned a value (0-7) with increasing weight as the slope is greater. Whatever the assigned value is, this number becomes `value_2`.
  - The final calculation adds `value_1` with `value_2`. The sum either is below 10 or at/above 10. If the sum matches the former, the thermostat is ON. The latter indicates the thermostat is OFF.
  
### Part 1: Webscrapping ###

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

After importing all the necessary libraries, we establish a connection to ComEd's page of pricing reports. The line `print("Response status:", check_connection)` ensures a connection to the server was successfully made. When running this code, we get `Response status: <Response [200]>` meaning the connection is established.

From there, we utilize HTML from the webpage, locating all instances of an indicator '<a'. This is a tag which precedes every link on the page. Since we are looking for the live 5 min pricing link and the live average current hour pricing link, we capture every link on the page and then index to get each respective link. As seen in the code, an index of "32" corresponds to the 5 min pricing link while an index of "43" corresponds to the average current hour pricing link. Each of these links is collected starting from "href" and this gives us both links as a url, respectively as `link_min` and `link_hour`. 

When printing `link_min` we get the appropriate link: https://hourlypricing.comed.com/api?type=5minutefeed

When printing `link_hour` we also get the correct link: https://hourlypricing.comed.com/api?type=currenthouraverage

### Part 2: Collecting the Current Price ###

```
while True:

    # DATA 1 -- current price

    # open 5 min pricing link
    response_min = urlopen(link_min)
    # store JSON response from 5 min pricing link as data
    pricing_min_json = json.loads(response_min.read())
    # current price -- from 5 min pricing
    current_price = pricing_min_json[0]['price']
    print("Current 5min price:", current_price)
```

To get the current price, we use the 5 min pricing link, opening a json file. To use the contents of this file, `json.loads(response_min.read())` returns a python dictionary from which we can index `[0]` under the key `['price']` to get the most recent value off. This gives us the most recent 5 min price.

For the user's information, we `print("Current 5min price:", current_price)` and get, for instance, `Current 5min price: 9.5`.

### Part 3: Collecting Average Current Hour Price and Average Past Hour Price ###

**Step 1: Collect Average Current Hour Price**
```
# NOTE: everything is included in the "while True:" loop at start of Part 2

    # DATA 2a -- current hour avg price

    # open current hour pricing link
    response_hour = urlopen(link_hour)
    # store JSON response from current hour pricing link as data
    pricing_hour_json = json.loads(response_hour.read())
    # current hour price -- from hourly current pricing
    current_hr_price = pricing_hour_json[0]['price']
    print("Current hour price:", current_hr_price)
```

These steps are identical to the code for **Part 2** except we use the current hour pricing link instead of the 5 min one. We also print the average current hour price for the user to view: `Current hour price: 7.4`

**Step 2: Collect Average Past Hour Price**
```
# NOTE: everything is included in the "while True:" loop at start of Part 2

    # DATA 2b -- past hour avg price

    # NOTE: CHECKS DATETIME CST/CDT TO VERIFY FOLLOWING BLOCK
    tz_CT = pytz.timezone('US/Central') 
    datetime_CT = datetime.now(tz_CT)
    print("Time in IL :", datetime_CT.strftime("%H:%M:%S"))

    # convert current time (uses local tz aka EST/EDT) to ms
    # subtract 2 hours to get past hour in CST/CDT
    past_hour_rawms = int(round((time.time() * 1000)-7200000))
    print("1 hr before - time in ms:", past_hour_rawms)

    # convert start of past hour from ms to datetime
    past_hour_datetime = datetime.fromtimestamp(round(past_hour_rawms/1000))
    print("1 hr before - datetime from ms:", past_hour_datetime)

    # get start of past hour
    past_hour_string = str(past_hour_datetime)
    past_hour = datetime.strptime(past_hour_string, "%Y-%m-%d %H:%M:%S")
    print("1 hr before - hour:", past_hour.hour)

    # get start of past hour in ms rounded down to the hour
    past_hour_strpstring = past_hour_string[0:13]
    sdt_obj = datetime.strptime(f'{past_hour_strpstring}', '%Y-%m-%d %H')
    past_hour_ms = int(sdt_obj.timestamp() * 1000)
    print("Start of past hour:", past_hour_ms)
    
    # get prices from 5 min pricing from start of past hour 
    # until start of current hour's price

    # get datetime start of past hour into correct format
    date_start_edit1 = past_hour_strpstring.replace('-', '')
    date_start_edit2 = date_start_edit1.replace(' ', '')
    date_start = f'{date_start_edit2}00'
    print("Date start:", date_start)

    # get end of past hour (same steps as getting start of past hour)
    end_of_past_hour_rawms = int(round((time.time() * 1000)-3600000))
    print("End of past hour - time in ms:", end_of_past_hour_rawms)
    end_of_past_hour_datetime = datetime.fromtimestamp(round(end_of_past_hour_rawms/1000))
    print("End of past hour - datetime from ms:", end_of_past_hour_datetime)
    end_of_past_hour_string = str(end_of_past_hour_datetime)
    end_of_past_hour = datetime.strptime(end_of_past_hour_string, "%Y-%m-%d %H:%M:%S")
    print("End of past hour - hour:", end_of_past_hour.hour)
    end_of_past_hour_strpstring = end_of_past_hour_string[0:13]
    edt_obj = datetime.strptime(f'{past_hour_strpstring}', '%Y-%m-%d %H')
    end_of_past_hour_ms = int(edt_obj.timestamp() * 1000)
    print("End of past hour:", end_of_past_hour_ms)

    # get datetime end of past hour into correct format
    date_end_edit1 = end_of_past_hour_strpstring.replace('-', '')
    date_end_edit2 = date_end_edit1.replace(' ', '')
    date_end = f'{date_end_edit2}00'
    print("Date end:", date_end)
    
    # custom url for 12, 5 min prices from past hour
    get_url_past_hour= urllib.request.urlopen(f'https://hourlypricing.comed.com/api?type=5minutefeed&datestart={date_start}&dateend={date_end}')
    pricing_past_hour_json = json.loads(get_url_past_hour.read())

    # collect 12, 5 min prices from past hour into array
    past_hour_prices = []
    i = 0
    while i < 12:
        price_pt = pricing_past_hour_json[i]['price']
        past_hour_prices.append(price_pt)
        i += 1
    print("12 prices of past hour:", past_hour_prices)
```

The first block that begins with a comment `# NOTE...` is solely present to check that the according blocks are getting the correct date/times. This block tells us the time currently in Illinois (CST/CDT). For example, `Time in IL : 17:14:52`

The next block finds the time in milliseconds of 1 hour ago in CST/CDT. The two subsequent blocks convert milliseconds to datetime. Then, from the datetime format, we strip to capture just the hour. We print it, to confirm we have the correct hour (aka the start of the past hour in CST/CDT).

From the full datetime, we then capture the date and just the hour. This is coverted back to milliseconds so it can be used to locate values from the json file of prices, keyed by milliseconds UTC.

For both the start of the past hour (on the hour) until the end of the past hour (aka start of current hour), we reformat the date/time into YYYYMMDDHHMM. Both the `date_start` and `date_end` are inserted in line 287 to get a report of all 5 min prices from the past hour.

As there are 12 prices in the json file, 1 per every 5 min, all 12 values are stored in an array `past_hour_prices`. 

To display each step in progress, below is an example of what the print statements return:

```
1 hr before - time in ms: 1651610288378
1 hr before - datetime from ms: 2022-05-03 16:38:08
1 hr before - hour: 16
Start of past hour: 1651608000000
Date start: 202205031600
End of past hour - time in ms: 1651613888392
End of past hour - datetime from ms: 2022-05-03 17:38:08
End of past hour - hour: 17
End of past hour: 1651608000000
Date end: 202205031700
12 prices of past hour: ['5.5', '6.3', '9.4', '8.4', '9.1', '7.5', '13.0', '8.0', '12.9', '8.5', '7.1', '7.2']
```

### Part 4: Calculate Average Past Hour Price ###

```
# NOTE: everything is included in the "while True:" loop at start of Part 2

# reformat to a list of float values
    past_hour_price_list = [float(i) for i in past_hour_prices]

    # take average of 12 prices to get avg past hour price
    def Average(past_hour_price_list):
        return sum(past_hour_price_list) / 12
    avg_past_hr_calc = Average(past_hour_price_list)
    avg_past_hour = round(avg_past_hr_calc, 1)
    print("Avg past hr price:", avg_past_hour)
```
Now that we have all our data to find the average past hour price, we first convert the array to a list of floats. Then, we create a function that returns the average of the 12 prices, rounded to 1 decimal place.

We return a value such as: `Avg past hr price: 8.6`

### Part 5: Collect Average Hourly Prices for Today ###

```
# NOTE: everything is included in the "while True:" loop at start of Part 2

    # Gather pricing data to create a line graph

    # collect 5 min prices from custom link for today
    # set today's date start and date end
    tz_CT = pytz.timezone('US/Central') 
    datetime_CT = datetime.now(tz_CT)
    date_CT_string = (str(datetime_CT))[0:10]
    today = date_CT_string.replace('-', '')
    today_datestart = f'{today}0000'
    today_dateend = f'{today}2355'
    print("Today Start:", today_datestart)
    print("Today End:", today_dateend)

    # use today's date start & end to get all prices for the day so far
    get_url_today  = urllib.request.urlopen(f'https://hourlypricing.comed.com/api?type=5minutefeed&datestart={today_datestart}&dateend={today_dateend}')
    # NOTE: USE BELOW AS TEST FOR ONE EXTREME: 24 hours of data. Uncomment line below and comment the line above.
    #get_url_today  = urllib.request.urlopen('https://hourlypricing.comed.com/api?type=5minutefeed&datestart=202205020000&dateend=202205022355')
    today_prices_json = json.loads(get_url_today.read())

    # capture 5 min prices in sets of 12 up until last full hour
    hrly_price = []
    avg_hrly_price = []
    i = 0
    while i < 288:
        if i >= len(today_prices_json):
            break
        
        if i < len(today_prices_json) :
            price_of_hour = today_prices_json[i]['price']
            hrly_price.append(price_of_hour)
            i += 1

        if len(hrly_price) == 12:
            hrly_price_list = [float(i) for i in hrly_price]
            def Average(hrly_price_list):
                return sum(hrly_price_list) / 12
            avg_hour_calc = Average(hrly_price_list)
            avg_hour_price = round(avg_hour_calc, 1)
            avg_hrly_price.append(avg_hour_price)
            hrly_price.clear()

        else:
            pass
```

Before continuing with calculations using the data we've collected so far, we also want to create a graph of the average prices per hour for the current day. To do this, we identify the current time in Illinois. By just capturing the date, we remove the dashes and attatch `0000` in HHMM format to the end of the date making this the start time (aka midnight of the current day). We also want an end time, so we get the last 5 min price which would be 5 min before midnight of the upcoming day. We indicated this by attaching `2355` in HHMM format to the end of the date.

Similarly to previous parts, the `today_datestart` and `today_dateend` are inserted into the custom link to get all prices for the current day. Even if the current day isn't over, we get as many prices as have been reported in the day so far. Again, these prices are posted every 5 min, so by the end of the day, there should be 288 prices in the file.

An example of the datestarts and dateends: 

```
Today Start: 202205030000
Today End: 202205032355
```

Throughout the day, as prices comes in starting with the first price from midnight, they are first appended to `hrly_price`. Once the array contains 12 prices (signaling 1 hour of prices has been recorded), these values are averaged and the returned value for average hour price is stored in `avg_hrly_price`. The array `hrly_prices` is cleared and the process starts once again. Every hour's average price for the day will be recorded.

*Note: I noticed later that, ideally, I should have provided code so that `avg_hrly_price` clears and resets by the end of the day. This way the user doesn't have the restart the entire program once every day.*

### Part 6: Create a Line Graph of Today's Average Hourly Prices ###

```
# NOTE: everything is included in the "while True:" loop at start of Part 2

  # create line graph depicting hrly prices of the day
    hour = []
    j = len(avg_hrly_price)
    k = 0
    while True:
        if j in range(0,25):
            # append numbers as hours using k as counter
            # k < j since current hour isn't calculated yet
            # and we want number of x values equal to y values
            while k < j:
                hour.append(k)
                k += 1
            
            # produce line graph
            if k >= j:
                plt.plot(hour, avg_hrly_price, color='blue', marker='o')
                plt.title('Average Hourly Prices Today', fontsize=12)
                plt.xlabel('Hour', fontsize=12)
                plt.ylabel('Average Price', fontsize=12)
                plt.grid(True)
                break
            
            # if during the hour starting at midnight
            # there is no avg hrly price yet so
            # waiting at 5 min intervals before checking for
            # 1st avg hrly price
            elif j is None:
                break
```

In order to create a line graph with average price vs. hour, we need all the values for average prices and all values for hours. We already have `avg_hrly_price` which contains every average hourly price for the day so far. Since the number of values for prices depends on the time of day, we cannot preset the number of hours that should go on this graph. What we can do is use the number of values in `avg_hrly_price` to dictate how many hours (starting from "0") should be appended to `hour`. Naturally, however many hourly prices we have should correspond to number of hours recorded.

While this condition is met, a plot with the appropriate headings, titles, and values will be created. The plot is produced at the end of the program using `plt.show()` (see **Part 7**).

![Alt text](Image URL)
![Average Hourly Prices for Today](/images/FP_graph.png)

The last elif statement is in place in case the program runs during the hour starting at midnight. Since a full hour has not been completed yet, there are no hourly prices meaning `avg_hrly_price` is empty. In this case, we can break from this block since a graph cannot be made yet. We would need at least one average hourly price.

### Part 7: Final Calculations to Determine State of the Thermostat ###

```
# NOTE: everything is included in the "while True:" loop at start of Part 2

    # comparison test & applying weight -- current price
    while True:
        if float(current_price) < 5:
            value_1 = float(current_price) * 1.7
            
        if 5 <= float(current_price) < 10:
            value_1 = float(current_price) * 1.3
        
        if float(current_price) >= 10:
            value_1 = float(current_price) * 1.7

        break
            
    # block for comparison test of delta (past hour price & current hour price)
    while True:

        delta_price_past_to_present_hr = float(avg_past_hour) - float(current_hr_price)
        
        if delta_price_past_to_present_hr < -5:
            value_2 = 0
        if -5 <= delta_price_past_to_present_hr < -3:
            value_2 = 1
        if -3 <= delta_price_past_to_present_hr < 0:
            value_2 = 2
        if 0 <= delta_price_past_to_present_hr < 1:
            value_2 = 3
        if 1 <= delta_price_past_to_present_hr < 2:
            value_2 = 4
        if 2 <= delta_price_past_to_present_hr < 3:
            value_2 = 5
        if 3 <= delta_price_past_to_present_hr < 4:
            value_2 = 6
        if delta_price_past_to_present_hr >= 4:
            value_2 = 7
        
        break

    # final product -- return whether thermostat should remain/be turned
    # on or off based on current price and change in price from past to current hour
    while True:

        final_calculation = value_1 + value_2

        if final_calculation < 10:
            print("THERMOSTAT IS: ON")
            
        if final_calculation >= 10:
            print ("THERMOSTAT IS: OFF")
            
        plt.show()
        break

    # NOTE: REPLACE WITH time.sleep(300)
    break
```

## Concluding Thoughts ##

The intention of taking two types of input (current price and slope between current and past hour prices) is to begin emulating the importance of factoring in multiple types of data. Using some basic algorithms and calculations also begins to demonstrate the importance of effective analysis of data. While the calculations used are not terribly sophisticated and the weighing system is not supported by much data other than my personal experience of how the pricing tends to work, I believe working with calculations revealed to me how powerful they can be. Additionally, I realized that creating an algorithm that accurately makes sense of data and uses it effectively is very tricky. It takes a lot of consideration, research, and trial and error. 
