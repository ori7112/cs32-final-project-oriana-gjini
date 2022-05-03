# this version only returns necessary outputs
# emulating how it would function for a user

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

# gathering all data
while True:

    # DATA 1 -- current price

    # open 5 min pricing link
    response_min = urlopen(link_min)
    # store JSON response from 5 min pricing link as data
    pricing_min_json = json.loads(response_min.read())
    # current price -- from 5 min pricing
    current_price = pricing_min_json[0]['price']
    print("Current 5min price:", current_price)

    # DATA 2a -- current hour avg price

    # open current hour pricing link
    response_hour = urlopen(link_hour)
    # store JSON response from current hour pricing link as data
    pricing_hour_json = json.loads(response_hour.read())
    # current hour price -- from hourly current pricing
    current_hr_price = pricing_hour_json[0]['price']
    print("Current hour price:", current_hr_price)

    # DATA 2b -- past hour avg price

    # convert current time (uses local tz aka EST/EDT) to ms
    # subtract 2 hours to get past hour in CST/CDT
    past_hour_rawms = int(round((time.time() * 1000)-7200000))

    # convert start of past hour from ms to datetime
    past_hour_datetime = datetime.fromtimestamp(round(past_hour_rawms/1000))

    # get start of past hour
    past_hour_string = str(past_hour_datetime)
    past_hour = datetime.strptime(past_hour_string, "%Y-%m-%d %H:%M:%S")

    # get start of past hour in ms rounded down to the hour
    past_hour_strpstring = past_hour_string[0:13]
    sdt_obj = datetime.strptime(f'{past_hour_strpstring}', '%Y-%m-%d %H')
    past_hour_ms = int(sdt_obj.timestamp() * 1000)

    # get prices from 5 min pricing from start of past hour 
    # until start of current hour's price

    # get datetime start of past hour into correct format
    date_start_edit1 = past_hour_strpstring.replace('-', '')
    date_start_edit2 = date_start_edit1.replace(' ', '')
    date_start = f'{date_start_edit2}00'

    # get end of past hour (same steps as getting start of past hour)
    end_of_past_hour_rawms = int(round((time.time() * 1000)-3600000))
    end_of_past_hour_datetime = datetime.fromtimestamp(round(end_of_past_hour_rawms/1000))
    end_of_past_hour_string = str(end_of_past_hour_datetime)
    end_of_past_hour = datetime.strptime(end_of_past_hour_string, "%Y-%m-%d %H:%M:%S")
    end_of_past_hour_strpstring = end_of_past_hour_string[0:13]
    edt_obj = datetime.strptime(f'{past_hour_strpstring}', '%Y-%m-%d %H')
    end_of_past_hour_ms = int(edt_obj.timestamp() * 1000)

    # get datetime end of past hour into correct format
    date_end_edit1 = end_of_past_hour_strpstring.replace('-', '')
    date_end_edit2 = date_end_edit1.replace(' ', '')
    date_end = f'{date_end_edit2}00'
    
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
    
    # reformat to a list of float values
    past_hour_price_list = [float(i) for i in past_hour_prices]

    # take average of 12 prices to get avg past hour price
    def Average(past_hour_price_list):
        return sum(past_hour_price_list) / 12
    avg_past_hr_calc = Average(past_hour_price_list)
    avg_past_hour = round(avg_past_hr_calc, 1)
    print("Avg past hr price:", avg_past_hour)

    # collect 5 min prices from custom link for today
    # set today's date start and date end
    tz_CT = pytz.timezone('US/Central') 
    datetime_CT = datetime.now(tz_CT)
    date_CT_string = (str(datetime_CT))[0:10]
    today = date_CT_string.replace('-', '')
    today_datestart = f'{today}0000'
    today_dateend = f'{today}2355'

    # use today's date start & end to get all prices for the day so far
    get_url_today  = urllib.request.urlopen(f'https://hourlypricing.comed.com/api?type=5minutefeed&datestart={today_datestart}&dateend={today_dateend}')
    # NOTE: USE BELOW AS TEST FOR ONE EXTREME: 24 hours of data
    #get_url_today  = urllib.request.urlopen('https://hourlypricing.comed.com/api?type=5minutefeed&datestart=202205020000&dateend=202205022355')
    today_prices_json = json.loads(get_url_today.read())
    
    # Gather pricing data to create a line graph
    
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
            

    # comparison test & applying weight -- current price
    while True:
        if float(current_price) < 5:
            value_1 = float(current_price) * 1.7
            
        if 5 <= float(current_price) < 10:
            value_1 = float(current_price) * 1.3
        
        if float(current_price) > 10:
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
        if delta_price_past_to_present_hr > 4:
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
