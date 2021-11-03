# Telegram members scraping
You want to create a new Telegram group and add users from on other group ?  
This program allows you to do it.  

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)  ![badge-telegram-program](https://github.com/pierre-vignoles/telegram_scrapping_multiple_accounts/blob/master/img/telegram-program.svg)

## Description 
All of your accounts will add multiple users on the group of your choice. The delay between each add is random to mimic organic use. You can choose the source of the members by only put the link of the telegram group you want to scrap.

## ⚠️ Recommandations 
If you add too much users, your accounts risk to be banned. To avoid that I recommand some things :  
* Never add more than 50 users per account per day
* Never add more than 200 users per group per day
* Always wait 3 days at minimum after the creation of your account to start to add users with it.
* During these 3 days minimum, use [this program](https://github.com/pierre-vignoles/telegram_send_messages) I made it to increase the authority of your accounts.

## Getting Started
* You need one or multiple Telegram accounts.
* You need the api_id and the api_hash of your accounts. To do that, you have to create an api key here for each account : [Create your api key here](https://my.telegram.org/auth?to=apps)
* Install requirements - `pip install -r requirements.txt`

## Change settings
Some variables must be configured in order to make this program work in the file `myconfig.py`.  
* `api_list` : Enter the `api_id` and `api_hash` for each account
* `number_of_adds_per_session` : The number of users add per account. I recommand a maximum of 30.
* `split_by` : *(For multiple accounts)* Number of times the accounts will be switching during the add of the users. (to avoid an adding of X users in a row with the same account)
* `number_of_seconds_to_wait_between_every_add` : Maximum number of seconds to wait between 2 adds of users.
* `number_of_seconds_min_to_wait_between_every_add` : Minimum number of seconds to wait between 2 adds of users.
* `path_csv` : Path where you want to save the csv files.
* `bool_send_message` : Set it to `True` if you want your account send messages to mimic an organic use.
* `number_of_adds_between_every_message` : Number of adds between every message sent.
* `link_channel_to_add_members` : The invitation link of your telegram group.
* `link_channel_you_want_to_scrape` : The invitation link of the telegram group you want to scrape.

## Launch 
Execute the following command in a terminal : `python main.py`

![screen](https://github.com/pierre-vignoles/telegram_scrapping_multiple_accounts/blob/master/img/screen.png)
