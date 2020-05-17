# WB-WB: Whatsapp Birthday Wishing Bot.

WB-WB is a Python Script for dealing with Birthdays. After a while, it gets difficult to wish everyone with unique birthday wishes. This script has been made to deal with that. 

The script will automatically fetch the birthdays from the database you enter in, and select a randomised birthday message from the ones pre-entered in the database.

## Installation

Clone the git project onto your computer. 

```bash
git clone https://github.com/sralli/WB-WB-Whatsapp-Birthday-Wishing-Bot.git
```

## Requirements:
- Selenium v3.141.0
- Python 3.6+
- ChromeDriver/GeckoDriver


## Setup

* Fill in the details of birthdays in: ```Birthdays_Database.csv```

* The fields are: (**All the fields are required**)
   - **Name**: Contact Name as present in Whatsapp.
   - **Birthday**: Day/Month of the contact.
   - **Already_Sent**: To be **ignored**, required to keep a track of the people already sent the messages to. 
   - **Nickname**: Nickname the script will use for the person. 
* Create Birthday wishes in ```.txt``` format in the ```messages``` folder. 
   - Format: 
        - Script automatically enters: ```"Hi {NickName}"``` while sending.
        - Thus, ***Message format***: Continuation after ```Hi {Nickname,}```
        - Sample Template has been provided.

 
* Setting up the script: 
     - **Driver Path**: Enter the driver/profile path in webdriver.py
     


## How to Run:

``` python main.py ```

**To run everyday automatically at midnight, enter in crontab-e**: ```00 00 * * * python path/to/main.py```

## Execution Workflow:
- The script fetches the birthdays from the database and checks whose birthday is today.
- The randomised message is selected.
- The script opens a new browser window, opens whatsapp web in your default profile and sends the message to the contact.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)